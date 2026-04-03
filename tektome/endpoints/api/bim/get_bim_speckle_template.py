from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_post_out import ErrorResponsePostOut
from ...models.get_bim_speckle_template_response import GetBimSpeckleTemplateResponse
from ...types import Response


def _get_kwargs(
    object_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/resource-groups/bim/bim-templates/{object_type}/".format(
            object_type=quote(str(object_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponsePostOut | GetBimSpeckleTemplateResponse | None:
    if response.status_code == 200:
        response_200 = GetBimSpeckleTemplateResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponsePostOut.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponsePostOut | GetBimSpeckleTemplateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponsePostOut | GetBimSpeckleTemplateResponse]:
    r"""Get Speckle BIM object template

     Return a Speckle-compatible JSON object for the requested geometry type. The returned JSON can be
    saved to a `.json` file and loaded directly into the Speckle viewer.

    ## Colour / material convention

    All colour integers are **signed 32-bit ARGB**: `(A<<24)|(R<<16)|(G<<8)|B` (values ≥ 0x80000000 wrap
    negative). The viewer unpacks each channel with a bit-shift (`r = (c >> 16) & 0xFF` etc.).

    The viewer's material priority per geometry type:

    | Geometry | 1st choice | 2nd choice | 3rd choice |
    |----------|------------|------------|------------|
    | mesh | vertex colors | renderMaterial | displayStyle |
    | line | displayStyle | renderMaterial | — |
    | text | displayStyle | — | — |

    When a mesh has **both** `colors` and `renderMaterial`, vertex colours **replace** the diffuse
    colour in the shader while PBR properties (opacity, roughness, metalness) still come from
    `renderMaterial`. To use only PBR material, set `colors` to `[]`.

    ## Supported types

    ### `mesh` — Unit box (Objects.Geometry.Mesh)

    Returns a 1000 mm cube centred at the origin.

    **Geometry fields:**

    - **vertices** — flat `[x0,y0,z0, x1,y1,z1, …]` list in mm. Every consecutive triplet is one vertex
    position. The box has 8 vertices (24 floats).
    - **faces** — run-length encoded triangle list. Each face begins with the vertex count (`3` for a
    triangle), followed by that many indices into the vertices array. Example: `[3, 0, 3, 2]` = triangle
    with vertices 0, 3, 2. The box has 12 triangles (48 ints).
    - **colors** — one signed 32-bit ARGB integer per vertex. Must have exactly `len(vertices) // 3`
    entries (one per vertex). When non-empty, the viewer sets `vertexColors = true` on the Three.js
    material and the shader **replaces** the `renderMaterial.diffuse` colour with the per-vertex value.
    To use only `renderMaterial` for colour, set this to `[]`.

    **Material fields (renderMaterial):**

    - **renderMaterial.diffuse** — surface colour as a signed 32-bit ARGB int.
    - **renderMaterial.emissive** — emissive colour (usually black = `−16777216`).
    - **renderMaterial.opacity** — `0.0`–`1.0` (`1` = fully opaque, `0.25` = glass-like).
    - **renderMaterial.roughness** — PBR roughness `0.0`–`1.0` (`1` = fully rough / matte).
    - **renderMaterial.metalness** — PBR metalness `0.0`–`1.0` (`0` = dielectric, `1` = metal).
    - **renderMaterial.name** — human-readable material label.
    - **renderMaterial.speckle_type** — must be `Objects.Other.RenderMaterial`.

    **Common fields:**

    - **id** — unique object identifier (any string).
    - **speckle_type** — must be `Objects.Geometry.Mesh`.
    - **units** — coordinate unit system (`mm`, `m`, `cm`, `ft`, `in`). The viewer multiplies all
    coordinates by the corresponding conversion factor.
    - **name** — optional display name shown in the object inspector.

    ### `line` — Line segment (Objects.Geometry.Line)

    Returns a single line from the origin to (5000, 5000, 0) mm.

    **Geometry fields:**

    - **start / end** — 3-D point objects with `x`, `y`, `z` floats and their own `units` field. The
    viewer converts each point to a Float32 position and draws a line segment between them.

    **Style fields (displayStyle):**

    - **displayStyle.diffuse** — stroke colour as a signed 32-bit ARGB int.
    - **displayStyle.lineweight** — stroke width in the unit given by `displayStyle.units`.
    - **displayStyle.units** — unit for lineweight.

    **Common fields:** **id**, **speckle_type** (`Objects.Geometry.Line`), **units**, **name** — same
    semantics as mesh.

    ### `text` — SDF text (Objects.Other.Text)

    Returns \"hello, world\" rendered by the viewer's built-in troika-three-text engine (GPU SDF fonts).
    No mesh geometry is needed.

    **Text fields:**

    - **value** — the text string to display.
    - **height** — font size in world units (mm).
    - **maxWidth** — line-wrapping width in world units; text longer than this wraps to the next line.
    - **alignmentH** — horizontal alignment: `0` = left, `1` = centre, `2` = right.
    - **alignmentV** — vertical alignment: `0` = top, `1` = middle, `2` = bottom.
    - **screenOriented** — when `true` the text always faces the camera (billboard mode); when `false`
    it is fixed in world space according to the **plane**.
    - **plane** — defines position and orientation:
      - **origin** — 3-D point where the text is placed.
      - **xdir** — unit vector for the text's horizontal axis.
      - **ydir** — unit vector for the text's vertical axis.
      - **normal** — unit vector perpendicular to the text plane (cross product of xdir × ydir).

    **Style fields (displayStyle):**

    - **displayStyle.diffuse** — text colour as a signed 32-bit ARGB int.
    - **displayStyle.lineweight** — set to `0` (not applicable to text, but required by the schema).
    - **displayStyle.units** — unit for lineweight.

    **Common fields:** **id**, **speckle_type** (`Objects.Other.Text`), **units**, **name** — same
    semantics as mesh.

    Args:
        object_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponsePostOut | GetBimSpeckleTemplateResponse]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponsePostOut | GetBimSpeckleTemplateResponse | None:
    r"""Get Speckle BIM object template

     Return a Speckle-compatible JSON object for the requested geometry type. The returned JSON can be
    saved to a `.json` file and loaded directly into the Speckle viewer.

    ## Colour / material convention

    All colour integers are **signed 32-bit ARGB**: `(A<<24)|(R<<16)|(G<<8)|B` (values ≥ 0x80000000 wrap
    negative). The viewer unpacks each channel with a bit-shift (`r = (c >> 16) & 0xFF` etc.).

    The viewer's material priority per geometry type:

    | Geometry | 1st choice | 2nd choice | 3rd choice |
    |----------|------------|------------|------------|
    | mesh | vertex colors | renderMaterial | displayStyle |
    | line | displayStyle | renderMaterial | — |
    | text | displayStyle | — | — |

    When a mesh has **both** `colors` and `renderMaterial`, vertex colours **replace** the diffuse
    colour in the shader while PBR properties (opacity, roughness, metalness) still come from
    `renderMaterial`. To use only PBR material, set `colors` to `[]`.

    ## Supported types

    ### `mesh` — Unit box (Objects.Geometry.Mesh)

    Returns a 1000 mm cube centred at the origin.

    **Geometry fields:**

    - **vertices** — flat `[x0,y0,z0, x1,y1,z1, …]` list in mm. Every consecutive triplet is one vertex
    position. The box has 8 vertices (24 floats).
    - **faces** — run-length encoded triangle list. Each face begins with the vertex count (`3` for a
    triangle), followed by that many indices into the vertices array. Example: `[3, 0, 3, 2]` = triangle
    with vertices 0, 3, 2. The box has 12 triangles (48 ints).
    - **colors** — one signed 32-bit ARGB integer per vertex. Must have exactly `len(vertices) // 3`
    entries (one per vertex). When non-empty, the viewer sets `vertexColors = true` on the Three.js
    material and the shader **replaces** the `renderMaterial.diffuse` colour with the per-vertex value.
    To use only `renderMaterial` for colour, set this to `[]`.

    **Material fields (renderMaterial):**

    - **renderMaterial.diffuse** — surface colour as a signed 32-bit ARGB int.
    - **renderMaterial.emissive** — emissive colour (usually black = `−16777216`).
    - **renderMaterial.opacity** — `0.0`–`1.0` (`1` = fully opaque, `0.25` = glass-like).
    - **renderMaterial.roughness** — PBR roughness `0.0`–`1.0` (`1` = fully rough / matte).
    - **renderMaterial.metalness** — PBR metalness `0.0`–`1.0` (`0` = dielectric, `1` = metal).
    - **renderMaterial.name** — human-readable material label.
    - **renderMaterial.speckle_type** — must be `Objects.Other.RenderMaterial`.

    **Common fields:**

    - **id** — unique object identifier (any string).
    - **speckle_type** — must be `Objects.Geometry.Mesh`.
    - **units** — coordinate unit system (`mm`, `m`, `cm`, `ft`, `in`). The viewer multiplies all
    coordinates by the corresponding conversion factor.
    - **name** — optional display name shown in the object inspector.

    ### `line` — Line segment (Objects.Geometry.Line)

    Returns a single line from the origin to (5000, 5000, 0) mm.

    **Geometry fields:**

    - **start / end** — 3-D point objects with `x`, `y`, `z` floats and their own `units` field. The
    viewer converts each point to a Float32 position and draws a line segment between them.

    **Style fields (displayStyle):**

    - **displayStyle.diffuse** — stroke colour as a signed 32-bit ARGB int.
    - **displayStyle.lineweight** — stroke width in the unit given by `displayStyle.units`.
    - **displayStyle.units** — unit for lineweight.

    **Common fields:** **id**, **speckle_type** (`Objects.Geometry.Line`), **units**, **name** — same
    semantics as mesh.

    ### `text` — SDF text (Objects.Other.Text)

    Returns \"hello, world\" rendered by the viewer's built-in troika-three-text engine (GPU SDF fonts).
    No mesh geometry is needed.

    **Text fields:**

    - **value** — the text string to display.
    - **height** — font size in world units (mm).
    - **maxWidth** — line-wrapping width in world units; text longer than this wraps to the next line.
    - **alignmentH** — horizontal alignment: `0` = left, `1` = centre, `2` = right.
    - **alignmentV** — vertical alignment: `0` = top, `1` = middle, `2` = bottom.
    - **screenOriented** — when `true` the text always faces the camera (billboard mode); when `false`
    it is fixed in world space according to the **plane**.
    - **plane** — defines position and orientation:
      - **origin** — 3-D point where the text is placed.
      - **xdir** — unit vector for the text's horizontal axis.
      - **ydir** — unit vector for the text's vertical axis.
      - **normal** — unit vector perpendicular to the text plane (cross product of xdir × ydir).

    **Style fields (displayStyle):**

    - **displayStyle.diffuse** — text colour as a signed 32-bit ARGB int.
    - **displayStyle.lineweight** — set to `0` (not applicable to text, but required by the schema).
    - **displayStyle.units** — unit for lineweight.

    **Common fields:** **id**, **speckle_type** (`Objects.Other.Text`), **units**, **name** — same
    semantics as mesh.

    Args:
        object_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponsePostOut | GetBimSpeckleTemplateResponse
    """

    return sync_detailed(
        object_type=object_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponsePostOut | GetBimSpeckleTemplateResponse]:
    r"""Get Speckle BIM object template

     Return a Speckle-compatible JSON object for the requested geometry type. The returned JSON can be
    saved to a `.json` file and loaded directly into the Speckle viewer.

    ## Colour / material convention

    All colour integers are **signed 32-bit ARGB**: `(A<<24)|(R<<16)|(G<<8)|B` (values ≥ 0x80000000 wrap
    negative). The viewer unpacks each channel with a bit-shift (`r = (c >> 16) & 0xFF` etc.).

    The viewer's material priority per geometry type:

    | Geometry | 1st choice | 2nd choice | 3rd choice |
    |----------|------------|------------|------------|
    | mesh | vertex colors | renderMaterial | displayStyle |
    | line | displayStyle | renderMaterial | — |
    | text | displayStyle | — | — |

    When a mesh has **both** `colors` and `renderMaterial`, vertex colours **replace** the diffuse
    colour in the shader while PBR properties (opacity, roughness, metalness) still come from
    `renderMaterial`. To use only PBR material, set `colors` to `[]`.

    ## Supported types

    ### `mesh` — Unit box (Objects.Geometry.Mesh)

    Returns a 1000 mm cube centred at the origin.

    **Geometry fields:**

    - **vertices** — flat `[x0,y0,z0, x1,y1,z1, …]` list in mm. Every consecutive triplet is one vertex
    position. The box has 8 vertices (24 floats).
    - **faces** — run-length encoded triangle list. Each face begins with the vertex count (`3` for a
    triangle), followed by that many indices into the vertices array. Example: `[3, 0, 3, 2]` = triangle
    with vertices 0, 3, 2. The box has 12 triangles (48 ints).
    - **colors** — one signed 32-bit ARGB integer per vertex. Must have exactly `len(vertices) // 3`
    entries (one per vertex). When non-empty, the viewer sets `vertexColors = true` on the Three.js
    material and the shader **replaces** the `renderMaterial.diffuse` colour with the per-vertex value.
    To use only `renderMaterial` for colour, set this to `[]`.

    **Material fields (renderMaterial):**

    - **renderMaterial.diffuse** — surface colour as a signed 32-bit ARGB int.
    - **renderMaterial.emissive** — emissive colour (usually black = `−16777216`).
    - **renderMaterial.opacity** — `0.0`–`1.0` (`1` = fully opaque, `0.25` = glass-like).
    - **renderMaterial.roughness** — PBR roughness `0.0`–`1.0` (`1` = fully rough / matte).
    - **renderMaterial.metalness** — PBR metalness `0.0`–`1.0` (`0` = dielectric, `1` = metal).
    - **renderMaterial.name** — human-readable material label.
    - **renderMaterial.speckle_type** — must be `Objects.Other.RenderMaterial`.

    **Common fields:**

    - **id** — unique object identifier (any string).
    - **speckle_type** — must be `Objects.Geometry.Mesh`.
    - **units** — coordinate unit system (`mm`, `m`, `cm`, `ft`, `in`). The viewer multiplies all
    coordinates by the corresponding conversion factor.
    - **name** — optional display name shown in the object inspector.

    ### `line` — Line segment (Objects.Geometry.Line)

    Returns a single line from the origin to (5000, 5000, 0) mm.

    **Geometry fields:**

    - **start / end** — 3-D point objects with `x`, `y`, `z` floats and their own `units` field. The
    viewer converts each point to a Float32 position and draws a line segment between them.

    **Style fields (displayStyle):**

    - **displayStyle.diffuse** — stroke colour as a signed 32-bit ARGB int.
    - **displayStyle.lineweight** — stroke width in the unit given by `displayStyle.units`.
    - **displayStyle.units** — unit for lineweight.

    **Common fields:** **id**, **speckle_type** (`Objects.Geometry.Line`), **units**, **name** — same
    semantics as mesh.

    ### `text` — SDF text (Objects.Other.Text)

    Returns \"hello, world\" rendered by the viewer's built-in troika-three-text engine (GPU SDF fonts).
    No mesh geometry is needed.

    **Text fields:**

    - **value** — the text string to display.
    - **height** — font size in world units (mm).
    - **maxWidth** — line-wrapping width in world units; text longer than this wraps to the next line.
    - **alignmentH** — horizontal alignment: `0` = left, `1` = centre, `2` = right.
    - **alignmentV** — vertical alignment: `0` = top, `1` = middle, `2` = bottom.
    - **screenOriented** — when `true` the text always faces the camera (billboard mode); when `false`
    it is fixed in world space according to the **plane**.
    - **plane** — defines position and orientation:
      - **origin** — 3-D point where the text is placed.
      - **xdir** — unit vector for the text's horizontal axis.
      - **ydir** — unit vector for the text's vertical axis.
      - **normal** — unit vector perpendicular to the text plane (cross product of xdir × ydir).

    **Style fields (displayStyle):**

    - **displayStyle.diffuse** — text colour as a signed 32-bit ARGB int.
    - **displayStyle.lineweight** — set to `0` (not applicable to text, but required by the schema).
    - **displayStyle.units** — unit for lineweight.

    **Common fields:** **id**, **speckle_type** (`Objects.Other.Text`), **units**, **name** — same
    semantics as mesh.

    Args:
        object_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponsePostOut | GetBimSpeckleTemplateResponse]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponsePostOut | GetBimSpeckleTemplateResponse | None:
    r"""Get Speckle BIM object template

     Return a Speckle-compatible JSON object for the requested geometry type. The returned JSON can be
    saved to a `.json` file and loaded directly into the Speckle viewer.

    ## Colour / material convention

    All colour integers are **signed 32-bit ARGB**: `(A<<24)|(R<<16)|(G<<8)|B` (values ≥ 0x80000000 wrap
    negative). The viewer unpacks each channel with a bit-shift (`r = (c >> 16) & 0xFF` etc.).

    The viewer's material priority per geometry type:

    | Geometry | 1st choice | 2nd choice | 3rd choice |
    |----------|------------|------------|------------|
    | mesh | vertex colors | renderMaterial | displayStyle |
    | line | displayStyle | renderMaterial | — |
    | text | displayStyle | — | — |

    When a mesh has **both** `colors` and `renderMaterial`, vertex colours **replace** the diffuse
    colour in the shader while PBR properties (opacity, roughness, metalness) still come from
    `renderMaterial`. To use only PBR material, set `colors` to `[]`.

    ## Supported types

    ### `mesh` — Unit box (Objects.Geometry.Mesh)

    Returns a 1000 mm cube centred at the origin.

    **Geometry fields:**

    - **vertices** — flat `[x0,y0,z0, x1,y1,z1, …]` list in mm. Every consecutive triplet is one vertex
    position. The box has 8 vertices (24 floats).
    - **faces** — run-length encoded triangle list. Each face begins with the vertex count (`3` for a
    triangle), followed by that many indices into the vertices array. Example: `[3, 0, 3, 2]` = triangle
    with vertices 0, 3, 2. The box has 12 triangles (48 ints).
    - **colors** — one signed 32-bit ARGB integer per vertex. Must have exactly `len(vertices) // 3`
    entries (one per vertex). When non-empty, the viewer sets `vertexColors = true` on the Three.js
    material and the shader **replaces** the `renderMaterial.diffuse` colour with the per-vertex value.
    To use only `renderMaterial` for colour, set this to `[]`.

    **Material fields (renderMaterial):**

    - **renderMaterial.diffuse** — surface colour as a signed 32-bit ARGB int.
    - **renderMaterial.emissive** — emissive colour (usually black = `−16777216`).
    - **renderMaterial.opacity** — `0.0`–`1.0` (`1` = fully opaque, `0.25` = glass-like).
    - **renderMaterial.roughness** — PBR roughness `0.0`–`1.0` (`1` = fully rough / matte).
    - **renderMaterial.metalness** — PBR metalness `0.0`–`1.0` (`0` = dielectric, `1` = metal).
    - **renderMaterial.name** — human-readable material label.
    - **renderMaterial.speckle_type** — must be `Objects.Other.RenderMaterial`.

    **Common fields:**

    - **id** — unique object identifier (any string).
    - **speckle_type** — must be `Objects.Geometry.Mesh`.
    - **units** — coordinate unit system (`mm`, `m`, `cm`, `ft`, `in`). The viewer multiplies all
    coordinates by the corresponding conversion factor.
    - **name** — optional display name shown in the object inspector.

    ### `line` — Line segment (Objects.Geometry.Line)

    Returns a single line from the origin to (5000, 5000, 0) mm.

    **Geometry fields:**

    - **start / end** — 3-D point objects with `x`, `y`, `z` floats and their own `units` field. The
    viewer converts each point to a Float32 position and draws a line segment between them.

    **Style fields (displayStyle):**

    - **displayStyle.diffuse** — stroke colour as a signed 32-bit ARGB int.
    - **displayStyle.lineweight** — stroke width in the unit given by `displayStyle.units`.
    - **displayStyle.units** — unit for lineweight.

    **Common fields:** **id**, **speckle_type** (`Objects.Geometry.Line`), **units**, **name** — same
    semantics as mesh.

    ### `text` — SDF text (Objects.Other.Text)

    Returns \"hello, world\" rendered by the viewer's built-in troika-three-text engine (GPU SDF fonts).
    No mesh geometry is needed.

    **Text fields:**

    - **value** — the text string to display.
    - **height** — font size in world units (mm).
    - **maxWidth** — line-wrapping width in world units; text longer than this wraps to the next line.
    - **alignmentH** — horizontal alignment: `0` = left, `1` = centre, `2` = right.
    - **alignmentV** — vertical alignment: `0` = top, `1` = middle, `2` = bottom.
    - **screenOriented** — when `true` the text always faces the camera (billboard mode); when `false`
    it is fixed in world space according to the **plane**.
    - **plane** — defines position and orientation:
      - **origin** — 3-D point where the text is placed.
      - **xdir** — unit vector for the text's horizontal axis.
      - **ydir** — unit vector for the text's vertical axis.
      - **normal** — unit vector perpendicular to the text plane (cross product of xdir × ydir).

    **Style fields (displayStyle):**

    - **displayStyle.diffuse** — text colour as a signed 32-bit ARGB int.
    - **displayStyle.lineweight** — set to `0` (not applicable to text, but required by the schema).
    - **displayStyle.units** — unit for lineweight.

    **Common fields:** **id**, **speckle_type** (`Objects.Other.Text`), **units**, **name** — same
    semantics as mesh.

    Args:
        object_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponsePostOut | GetBimSpeckleTemplateResponse
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            client=client,
        )
    ).parsed

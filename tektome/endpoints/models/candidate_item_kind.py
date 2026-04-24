from enum import Enum


class CandidateItemKind(str, Enum):
    CREATE_UPDATE_BOOLEAN_ATTRIBUTES = "boolean_attributes"
    CREATE_UPDATE_COORDINATE_ATTRIBUTES = "coordinate_attributes"
    CREATE_UPDATE_DATETIME_ATTRIBUTES = "datetime_attributes"
    CREATE_UPDATE_DATE_ATTRIBUTES = "date_attributes"
    CREATE_UPDATE_FLOAT_ATTRIBUTES = "float_attributes"
    CREATE_UPDATE_INTEGER_ATTRIBUTES = "integer_attributes"
    CREATE_UPDATE_JSON_ATTRIBUTES = "json_attributes"
    CREATE_UPDATE_LIST_OBJECT_ATTRIBUTES = "list_object_attributes"
    CREATE_UPDATE_MULTI_SELECT_ATTRIBUTES = "multi_select_attributes"
    CREATE_UPDATE_POLYGON_ATTRIBUTES = "polygon_attributes"
    CREATE_UPDATE_SINGLE_SELECT_ATTRIBUTES = "single_select_attributes"
    CREATE_UPDATE_STRING_ATTRIBUTES = "string_attributes"
    CREATE_UPDATE_TABLE_ATTRIBUTES = "table_attributes"
    CREATE_UPDATE_TIME_ATTRIBUTES = "time_attributes"
    FILE_UPLOAD = "file_upload"

    def __str__(self) -> str:
        return str(self.value)

from dbapp.db import queries as dbq

from dbapp.config import (
    FAILED_COLUMNS, 
    FAILED_ROWS, 
)

def compare_queries(user_query: str, answer_query: str, check_mode="strict", rule=None):
    result = False
    message = ""
    if check_mode == "strict":
        pass
    elif check_mode == "loose":
        pass
    else:
        pass
    return result, message
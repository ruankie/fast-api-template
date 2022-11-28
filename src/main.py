import pandas as pd
from fastapi import FastAPI, HTTPException
from src.utils import DataQualityChecker

app = FastAPI()
dqc = DataQualityChecker()

DOCSTRING_EXAMPLE_PAYLOAD = """
{
    "a": [1,2,3,4],
    "b": [5,6,7,8]
}
"""


@app.get("/")
async def get_greeting():
    """Welcome screen."""
    return {"about": "Welcome to the data quality checker. Go to the /docs endpoint for help."}

@app.post("/quality-check/min-rows")
def min_rows(min_rows:int = 0, payload:dict = {}):
    """
    Check valid row count (more than minimum).

    Example payload:
    {
        "a": [1,2,3,4],
        "b": [5,6,7,8]
    }
    """
    # turn payload into pandas df
    try:
        df = pd.DataFrame(payload)
    except Exception as ex:
        raise HTTPException(status_code=201, detail=f"Could not convert payload to pandas DataFrame.")
    
    # check row quality
    validity = dqc.has_at_least_rows(df, min_rows=min_rows)
    return {"is_valid": validity}

@app.post("/quality-check/row-range")
def row_range(min_rows:int = 0, max_rows:int=9999, payload:dict = {}):
    """
    Check valid row count (within given range).

    Example payload:
    {
        "a": [1,2,3,4],
        "b": [5,6,7,8]
    }
    """
    # turn payload into pandas df
    try:
        df = pd.DataFrame(payload)
    except Exception as ex:
        raise HTTPException(status_code=201, detail=f"Could not convert payload to pandas DataFrame")
    
    # check row quality
    validity = dqc.has_valid_row_range(df, min_rows=min_rows, max_rows=max_rows)
    return {"is_valid": validity}
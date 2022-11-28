import pandas as pd

class DataQualityChecker():
    """
    Class that performs various data quality checks 
    on pandas DataFrames.
    """
    def __init__(self) -> None:
        pass

    def has_at_least_rows(self, df:pd.DataFrame, min_rows:int) -> bool:
        """
        Check wether the given data has at least the 
        minimum row count.

        Args:
            df (df:pd.DataFrame): Data to check for valid row count.
            min_rows (int): Minimum accepted number of rows.

        Return:
            bool: Whether the data has a valid row count or not.
        """
        if df.shape[0] >= min_rows:
            return True
        else:
            return False

    def has_valid_row_range(self, df:pd.DataFrame, min_rows:int, max_rows:int) -> bool:
        """
        Check wether the given data has a row count between
        the minimum and maximum allowed.

        Args:
            df (df:pd.DataFrame): Data to check for valid row count.
            min_rows (int): Minimum accepted number of rows.
            max_rows (int): Maximum accepted number of rows.

        Return:
            bool: Whether the data has a valid row count or not.
        """
        if (df.shape[0] >= min_rows) & (df.shape[0] <= max_rows):
            return True
        else:
            return False

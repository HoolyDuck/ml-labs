import pandas as pd

class CsvProcessor():

    def __init__(self, src) -> None:
        self.df = pd.read_csv(src)

    def get_df(self) -> pd.DataFrame:
        return self.df


import pandas as pd


class ExcelProcessor():

    def __init__(self, path, index_col, header, skiprows, skipfooter) -> None:
        self.df = pd.read_excel(
            path,
            index_col=index_col,
            header=header,
            skiprows=skiprows,
            skipfooter=skipfooter
        )

    def get_df(self):
        return self.df

    def get_row(self, row):
        return self.df.iloc[row]

    def get_quaters(self, row):
        return [self.df.iloc[row][i::4] for i in range(4)]

    def get_labels(self):
        return sorted(list(set(label[0] for label in self.df.columns)))

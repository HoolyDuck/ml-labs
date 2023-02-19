from processors.csv_processor import CsvProcessor
from processors.excel_processor import ExcelProcessor
from plot_builders.bar_builder import BarBuilder
from plot_builders.hist_builder import HistBuilder

import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

# COLORS
rc = '\033[91m'
wc = '\033[0m'
bc = '\033[94m'
gc = '\033[92m'

excel_processor = ExcelProcessor(
    "./(13.02.23) LAB-1/files/io_zp_15-23.xlsx",
    index_col=0,
    header=[3, 4],
    skiprows=[6],
    skipfooter=5
)

csv_processor = CsvProcessor(
    "./(13.02.23) LAB-1/files/TitanicSurvival.csv"
)


def task2():
    df = excel_processor.get_df()

    for i in range(5):
        print(f'\n{rc}## {df.index[i]} ##{wc}')
        series = pd.Series({
            "Середньоквадратичне відхилення": df.iloc[i].std(),
            "Математичне сподівання": df.iloc[i].mean(),
            "Дисперсія": df.iloc[i].var(),
            "Медіана": df.iloc[i].median(),
            "Мода": df.iloc[i].mode()[0]
        })
        print(series)


def task3():
    bar_builder = BarBuilder(5, excel_processor.get_labels())

    headers = excel_processor.get_df().index.tolist()

    for i in range(5):
        bar_builder.build_bar(
            i,
            headers[i],
            'Changes',
            excel_processor.get_labels(),
            excel_processor.get_labels(),
            excel_processor.get_quaters(i)
        )

    bar_builder.show_plot()


def task3_2():
    hist_builder = HistBuilder()

    for i in range(5):
        hist_builder.build_hist(
            i,
            excel_processor.get_df().index[i],
            excel_processor.get_row(i)
        )

    hist_builder.show_plot()


get_roman_num_quarter_regex = re.compile(r'([IV]+)')


def task4():
    # shorter column names
    df = excel_processor.get_df()
    df.columns.set_levels(df.columns.levels[1].map(
        lambda x: get_roman_num_quarter_regex.findall(x)[0]), level=1, inplace=True)

    series = pd.Series([i for i in range(1, 4)])

    # print series
    print(f'{gc}Series output: \n{wc}{series}')


    # series statistics
    print(f'\n{gc}Series statistics output: \n{wc}{series.describe()}')
    
    # series mean
    print(f'\n{gc}Series mean output: \n{wc}{series.mean()}')

    # create series without index
    series = pd.Series([i for i in range(1, 4)])
    print(f'\n{gc}Series without index output: \n{wc}{series}')

     # reference series index
    print(f'\n{gc}Series index output: \n{wc}{series[0]}')

    # series with index
    series = pd.Series([i for i in range(1, 4)], index=[f'index {i}' for i in range(1, 4)])
    print(f'\n{gc}Series with index output: \n{wc}{series}')

    # series with index but as map
    series = pd.Series({f'index {i}': i for i in range(1, 4)})
    print(f'\n{gc}Series with index as map output: \n{wc}{series}')

    # reference series index
    print(f'\n{gc}Series index output: \n{wc}{series["index 1"]}')

    
    # series with multiindex
    series = pd.Series(
        [i for i in range(1, 4)],
        index=pd.MultiIndex.from_tuples(
            [(f'index {i}', f'index {i}') for i in range(1, 4)]
        )
    )
    print(f'\n{gc}Series with multiindex output: \n{wc}{series}')

    # series dtype
    print(f'\n{gc}Series dtype output: \n{wc}{series.dtype}')

    # series values
    print(f'\n{gc}Series values output: \n{wc}{series.values}')

    # series with strings
    series = pd.Series(['asda', 'bfsa', 'cfsaf', 'dfafs', 'edad'])

    # series where string contains b
    print(f'\n{gc}Series where string contains b output: \n{wc}{series.str.contains("b")}')

    # series where all words are uppercase
    print(f'\n{gc}Series where all words are uppercase output: \n{wc}{series.str.upper()}')

    # --dataframe section--

    # change dataframe index
    print(f'\n{gc}Original dataframe index output: \n{wc}{df.iloc[:, :8]}')
    df.index = [f'Changed index {i + 1}' for i in range(len(df.index))]
    print(f'\n{gc}Changed dataframe index output: \n{wc}{df.iloc[:, :8]}')

    # reference column
    print(f'\n{gc}Reference column output: \n{wc}{df[2015]}')

    # reference multiindex column
    print(f'\n{gc}Reference multiindex column output: \n{wc}{df[2015, "I"]}')

    # single loc/iloc
    print(f'\n{gc}Single loc output: \n{wc}{df.loc["Changed index 1"]}')
    print(f'\n{gc}Single iloc output: \n{wc}{df.iloc[0]}')

    # multiple loc/iloc
    print(
        f'\n{gc}Multiple loc output: \n{wc}{df.loc["Changed index 1":"Changed index 5", 2015:2017]}')
    print(f'\n{gc}Multiple iloc output: \n{wc}{df.iloc[0:5, 0:3]}')

    # concrete value loc/iloc
    print(
        f'\n{gc}Concrete value loc output: \n{wc}{df.loc[["Changed index 2", "Changed index 4"], 2015]}')
    print(f'\n{gc}Concrete value iloc output: \n{wc}{df.iloc[[1, 3], 0]}')

    # boolean indexing
    print(
        f'\n{gc}Boolean indexing output: \n{wc}{df.iloc[1:5, :8][(df < -5) & (df > -10)]}')

    # cell value at/iat
    print(
        f'\n{gc}Cell value at output: \n{wc}{df.at["Changed index 1", (2015, "I")]}')
    print(f'\n{gc}Cell value iat output: \n{wc}{df.iat[0, 0]}')

    # change cell value
    df.at["Changed index 1", (2015, "I")] = 100
    print(
        f'\n{gc}Changed cell value at output: \n{wc}{df.at["Changed index 1", (2015, "I")]}')
    df.iat[0, 0] = 92
    print(f'\n{gc}Reverted cell value iat output: \n{wc}{df.iat[0, 0]}')

    # df statistics
    print(
        f'\n{gc}Dataframe statistics output: \n{wc}{df.iloc[1:, :8].describe()}')

    # statitics with precision 2
    print(
        f'\n{gc}Dataframe statistics with precision 2 output: \n{wc}{df.iloc[1:, :8].describe().round(2)}')

    # mean
    print(f'\n{gc}Dataframe mean output: \n{wc}{df.iloc[1:, :8].mean()}')

    # transpose
    print(f'\n{gc}Dataframe transpose output: \n{wc}{df.iloc[1:, :8].T}')

    # statistics with transpose
    print(
        f'\n{gc}Dataframe statistics with transpose output: \n{wc}{df.iloc[1:, :8].T.describe()}')

    # mean with transpose
    print(
        f'\n{gc}Dataframe mean with transpose output: \n{wc}{df.iloc[1:, :8].T.mean()}')

    # sort by index descending
    print(
        f'\n{gc}Dataframe sort by index descending output: \n{wc}{df.iloc[1:, :8].sort_index(ascending=False)}')

    # sort by values
    print(
        f'\n{gc}Dataframe sort by values output: \n{wc}{df.iloc[1, :8].sort_values(ascending=False)}')

    # sort and edit df
    df.sort_values(by=(2015, 'I'), inplace=True)
    print(f'\n{gc}Dataframe sort and edit output: \n{wc}{df.iloc[1:, :8]}')

    print(df)


def task5():
    # shorter column names
    df = excel_processor.get_df()
    df.columns.set_levels(df.columns.levels[1].map(
        lambda x: get_roman_num_quarter_regex.findall(x)[0]), level=1, inplace=True)

    # replace NaNs with average value
    for i in range(len(df.index)):
        df.iloc[i] = df.iloc[i].fillna(df.iloc[i].mean())

    print(df[2023])

    df[2023].hist(figsize=(10, 10))
    plt.show()


def task6():
    print(csv_processor.get_df())


def task7():
    # get csv by url:
    print(pd.read_csv(
        "https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv"))


titanic_df: pd.DataFrame = csv_processor.get_df()


def task8():
    # read head and tail
    print(titanic_df.head(5).round(2))
    print(titanic_df.tail(5).round(2))


def task9():
    # change column names:
    titanic_df.columns = ['name', 'survived', 'sex', 'age', 'class']
    task8()


def task10():
    # simple analysis
    titanic_df.columns = ['name', 'survived', 'sex', 'age', 'class']

    min_age = titanic_df["age"].min();
    print(f'{gc}Min age passenger: \n{wc}{titanic_df[titanic_df["age"] == min_age]}')

    max_age = titanic_df["age"].max();
    print(f'{gc}Max age passenger: \n{wc}{titanic_df[titanic_df["age"] == max_age]}')
    print(f'{gc}Average age: \n{wc}{titanic_df["age"].mean()}')

    female_1st_class = titanic_df[(titanic_df["sex"] == "female") & (titanic_df["class"] == "1st")].sort_index()
    print(
        f'{gc}Female 1st class: \n{wc}{female_1st_class}')
    
    min_age_female = female_1st_class["age"].min();
    print(f'{gc}Min age female: \n{wc}{female_1st_class[female_1st_class["age"] == min_age_female]}')

    max_age_female = female_1st_class["age"].max();
    print(f'{gc}Max age female: \n{wc}{female_1st_class[female_1st_class["age"] == max_age_female]}')

    alive_females = female_1st_class[female_1st_class["survived"] == "yes"]
    print(f'{gc}Females survived: \n{wc}{alive_females}')


def task11():
    titanic_df.columns = ['name', 'survived', 'sex', 'age', 'class']
    ages = titanic_df["age"]
    ages.hist()
    plt.show()


def main():
    # task2()
    #  task3()
    # task3_2()
    task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    # task10()
    # task11()


if __name__ == '__main__':
    main()

import pandas as pd
from pathlib import Path


def pd_read_file():
    # pd.set_option('display.max_columns', 3)
    work_path = Path.cwd()
    data_path = Path(work_path, 'datasets', 'bikes.csv')
    data = pd.read_csv(data_path, sep=',')
    print(data.head(10))
    print(data['Rachel1'].sum())


if __name__ == '__main__':
    pd_read_file()

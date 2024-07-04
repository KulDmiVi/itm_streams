# Рисовать графики сразу же
#
# %matplotlib inline
from pathlib import Path
import os

import pandas as pd
import matplotlib.pyplot as plt




def read_file():
    work_path = Path.cwd()
    data_path = Path(work_path, 'datasets', 'bikes.csv')
    fixed_df = pd.read_csv(data_path,
                           sep=',',
                           encoding='latin1',
                           parse_dates=['Date'],
                           dayfirst=True,
                           index_col='Date')

    return fixed_df




def draw_plt(data, image_size):
    plt.style.use('ggplot')  # Красивые графики
    data.plot(figsize=image_size)
    plt.show()


def lesson_1(fixed_df):
    print(fixed_df[:3])
    print(fixed_df['Berri 1'][:10])
    draw_plt(fixed_df['Berri 1'], (15, 5))
    draw_plt(fixed_df, (15, 10))

def lesson_3(bikes):
    berri_bikes = bikes[['Berri 1']].copy()
    print(berri_bikes[:5])
    print(berri_bikes.index)
    print(berri_bikes.index.day)
    print(berri_bikes.index.weekday)
    berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday
    print(berri_bikes[:5])

    weekday_counts = berri_bikes.groupby('weekday').sum()
    print(weekday_counts)
    weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(weekday_counts)
    weekday_counts.plot(kind='bar')
    plt.show()

def main():
    fixed_df = read_file()
    lesson_1(fixed_df)
    os.system('cls')
    lesson_3(fixed_df)


if __name__ == '__main__':
    main()

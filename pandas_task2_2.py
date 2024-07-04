# Рисовать графики сразу же
#
# %matplotlib inline
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

work_path = Path.cwd()
data_path = Path(work_path, 'datasets', '311-service-requests.csv')


def read_file():
    complaints = pd.read_csv(data_path)
    return complaints


def draw_plt(data, image_size, type):
    plt.style.use('ggplot')
    data.plot(figsize=image_size, kind=type)
    plt.show()


def part2():
    complaints = read_file()
    print(complaints[:5])
    print(complaints['Complaint Type'][:5])
    print(complaints[:5]['Complaint Type'])
    print(complaints[['Complaint Type', 'Borough']][:10])
    complaint_counts = complaints['Complaint Type'].value_counts()
    print(complaint_counts[:10])
    draw_plt(complaint_counts[:10], (10, 15), 'bar')

def part6():
    requests = read_file()
    print(requests['Incident Zip'].unique())
    na_values = ['NO CLUE', 'N/A', '0']
    requests = pd.read_csv(data_path, na_values=na_values, dtype={'Incident Zip': str})
    print(requests['Incident Zip'].unique())
    rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
    print(len(requests[rows_with_dashes]))
    print(requests[rows_with_dashes]['Incident Zip'])
    long_zip_codes = requests['Incident Zip'].str.len() > 5
    print(requests['Incident Zip'][long_zip_codes].unique())
    requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)
    requests[requests['Incident Zip'] == '00000']
    zero_zips = requests['Incident Zip'] == '00000'
    requests.loc[zero_zips, 'Incident Zip'] = np.nan
    unique_zips = requests['Incident Zip'].unique()
    print(unique_zips)
    zips = requests['Incident Zip']
    is_close = zips.str.startswith('0') | zips.str.startswith('1')
    is_far = ~(is_close) & zips.notnull()
    print(zips[is_far])
    print(requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort_values('Incident Zip'))
    print(requests['City'].str.upper().value_counts())


if __name__ == '__main__':
    # part2()
    part6()

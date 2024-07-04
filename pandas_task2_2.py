# Рисовать графики сразу же
#
# %matplotlib inline
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def read_file():
    work_path = Path.cwd()
    data_path = Path(work_path, 'datasets', '311-service-requests.csv')
    complaints = pd.read_csv(data_path)
    return complaints


def draw_plt(data, image_size, type):
    plt.style.use('ggplot')
    data.plot(figsize=image_size, kind=type)
    plt.show()


def main():
    complaints = read_file()
    print(complaints[:5])
    print(complaints['Complaint Type'][:5])
    print(complaints[:5]['Complaint Type'])
    print(complaints[['Complaint Type', 'Borough']][:10])
    complaint_counts = complaints['Complaint Type'].value_counts()
    print(complaint_counts[:10])
    draw_plt(complaint_counts[:10], (10, 15), 'bar')

if __name__ == '__main__':
    main()

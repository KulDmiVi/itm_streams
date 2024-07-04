from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок
work_path = Path.cwd()
data_path = Path(work_path, 'datasets', 'popularity-contest.txt')


popcon = pd.read_csv(data_path, sep=' ')[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']
print(popcon[:5])
popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)
popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')
print(popcon['atime'].dtype)
print(popcon[:5])
popcon = popcon[popcon['atime'] > '1970-01-01']
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]
print(nonlibraries.sort_values('ctime', ascending=False)[:10])
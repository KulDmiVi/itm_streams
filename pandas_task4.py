import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'
url_template = """http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"""


def demo_work():
    url = url_template.format(month=3, year=2012)
    weather_mar2012 = pd.read_csv(url, index_col=r'Date/Time (LST)', parse_dates=True)
    print(weather_mar2012[:3])
    weather_mar2012["Temp (°C)"].plot(figsize=(18, 6))
    weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')
    plt.show()
    print(weather_mar2012[:5])
    weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day'], axis=1)
    print(weather_mar2012[:5])
    temperatures = weather_mar2012[[u'Temp (°C)']].copy()
    temperatures.loc[:, 'Hour'] = weather_mar2012.index.hour
    temperatures.groupby('Hour').agg(np.median).plot()
    plt.show()


def download_weather_month(year, month):
    url = url_template.format(year=year, month=month)
    weather_data = pd.read_csv(url, index_col='Date/Time (LST)', parse_dates=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month'], axis=1)
    return weather_data


def save_df_to_csv():
    data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]
    weather_2012 = pd.concat(data_by_month)
    weather_2012.to_csv('weather_2012.csv')


def main():
    demo_work()
    print(download_weather_month(2012, 1)[:5])
    save_df_to_csv()


if __name__ == '__main__':
    main()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Calculate the moving average of a time series
def moving_average(series, window):
    return series.rolling(window=window).mean()

# --- Main Application ---
if __name__ == "__main__":
    # 1. Generate and Visualize Data
    file_path = 'stocks.csv'
    df = pd.read_csv(file_path)
    company = 'AAPL'
    format_string = "%Y-%m-%d"

    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].apply(lambda d: d.strftime(format_string))
    df = df[df['Company']==company]
    df2 = df.drop(columns=['Open','High','Low','Volume','Dividends','Stock Splits','Company'])
    df2 = df2.reset_index()
    df2 = df2.set_index(['Date'])
    appleStocks = pd.Series(df2['Close'])

    plt.figure(figsize=(12, 6))
    plt.plot(appleStocks, label='Original Data')
    plt.title('Apple (AAPL) Stock Price Movement')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig('time_series_plot.png')
    plt.show()

    # 2. Calculate and Plot Moving Average
    window_size = 100
    ma_series = moving_average(appleStocks, window_size)
    plt.figure(figsize=(12, 6))
    plt.plot(appleStocks, label='Original Data')
    plt.plot(ma_series, label=f'{window_size}-Day Moving Average', linestyle='--')
    plt.title('Apple (AAPL) Stock Price Movement with Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig('moving_average_plot.png')
    plt.show()

    # 3. Forecast the Next Value
    last_values = appleStocks.tail(window_size)
    forecast = last_values.mean()
    print(f"\n--- Forecasting ---")
    print(f"Last {window_size} values: \n{last_values.to_string()}")
    print(f"\nPredicted next value: {forecast:.2f}")

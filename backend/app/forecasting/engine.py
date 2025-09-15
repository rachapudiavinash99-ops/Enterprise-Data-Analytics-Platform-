import pandas as pd
import numpy as np

def run_simple_forecast(df: pd.DataFrame, date_col: str, metric_col: str, periods: int) -> pd.DataFrame:
    # Placeholder for a real forecasting model like Prophet or ARIMA
    # Here we just return a naive moving average prediction
    last_val = df[metric_col].iloc[-1] if not df.empty else 0
    forecast = []
    for i in range(periods):
        forecast.append({'period': i+1, 'prediction': last_val * (1 + 0.01 * i)})
    return pd.DataFrame(forecast)

from FinMind.data import DataLoader

dl = DataLoader()
future_data = dl.taiwan_futures_daily(futures_id="TX", start_date="2017-05-15")
future_data = future_data[(future_data.trading_session == "position")]
future_data = future_data[(future_data.settlement_price > 0)]
future_data = future_data[
    future_data["contract_date"]
    == future_data.groupby("date")["contract_date"].transform("min")
]

print(future_data)

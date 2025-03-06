import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define portfolio holdings with weights
portfolio = {
    "AAPL": 0.30,  # 30% in Apple stock
    "MSFT": 0.20,  # 20% in Microsoft stock
    "BND": 0.25,   # 25% in Bonds ETF (Vanguard Total Bond)
    "VNQ": 0.15,   # 15% in Real Estate (Vanguard REIT)
    "GLD": 0.10    # 10% in Gold
}

weights = np.array(list(portfolio.values()))
tickers = list(portfolio.keys())

start_date = "2020-01-01"
end_date = "2024-01-01"

prices = yf.download(tickers, start=start_date, end=end_date)
# print(prices)

# Check for 'Adj Close' or fallback to 'Close'
if "Adj Close" in prices:
    prices = prices["Adj Close"] # first choice
elif "Close" in prices:
    prices = prices["Close"]
else:
    raise ValueError("data missing.")

# Calculations
returns = prices.pct_change().dropna() # percentage change in price
# print(returns)
portfolio_returns = returns.dot(weights)
# print(portfolio_returns)
cumulative_returns = (1 + portfolio_returns).cumprod()
annual_return = portfolio_returns.mean() * 252

# Plot the cumulative returns graph
plt.figure(figsize=(10, 5))
plt.plot(cumulative_returns, label="Portfolio", linewidth=2, color='blue')
plt.title("Portfolio Cumulative Returns")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.grid()
plt.show()

print(f"Annual Return: {annual_return:.2%}")
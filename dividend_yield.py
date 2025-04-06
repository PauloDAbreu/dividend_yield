import yfinance as yf

ticker = yf.Ticker("PETR4.SA")

dy = ticker.info.get('dividendYield')

print(f"dividend yield PETR4: {dy * 100:.2f}%")

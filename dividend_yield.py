import yfinance as yf

ticker = yf.Ticker("PETR4.SA")

dy = ticker.info.get('dividendYield')
ultimo_fechamento = ticker.info['regularMarketTime']

print(f"dividend yield PETR4: {dy * 100:.2f}%")
print(f"Última atualização: {ultimo_fechamento}")
print("atualização feita")
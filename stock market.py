import yfinance as yf

company= input("enter the ticker symbol of a company(in caps) \n")

company_info_raw = yf.Ticker(company)

output = company_info_raw.info

print(output)
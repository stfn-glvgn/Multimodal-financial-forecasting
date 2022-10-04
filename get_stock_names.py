import pandas as pd
import json
import csv

if __name__ == '__main__':

    symbol_to_name = {}
    name_to_symbol = {}
    df_names_symbols = pd.read_csv("constituents_csv copia.csv")


    for index in range (0, len(df_names_symbols)):
        row = df_names_symbols.iloc[index]
        symbol = row["Symbol"]
        name = row["Name"]
        symbol_to_name[symbol] = name
        name_to_symbol[name] = symbol



    # with open("symbol_to_name_dic", "w") as fp:
    #     json.dump(symbol_to_name, fp)
    #
    # with open("name_to_symbol_dic", "w") as fp:
    #     json.dump(name_to_symbol, fp)

    df_stock = pd.read_csv("SP 500 Stock Prices 2014-2017 copia.csv")
    #mask = df_stock["date"].str.startswith("2017-")
    mask = (df_stock['date'] >= '2016-12-01') & (df_stock['date'] <= '2018-02-31')
    df_stock = df_stock[mask]
    #print(df_stock)

    df_stock["name"] = df_stock.apply(lambda row: symbol_to_name[row["symbol"]], axis = 1)
    df_stock["year"] = df_stock.apply(lambda row: row["date"].split("-")[0], axis = 1)
    df_stock["month"] = df_stock.apply(lambda row: row["date"].split("-")[1], axis=1)
    df_stock["day"] = df_stock.apply(lambda row: row["date"].split("-")[2], axis=1)

    df_stock.rename(columns={"symbol": "ticker"}, inplace=True)
    df_stock.reset_index(inplace=True)
    df_stock.drop(columns=["index"], inplace=True)

    df_stock.to_csv('stock_data.csv')

    #print(df_stock)

    # path = "AllRetPrices/"
    # for ticker in symbol_to_name.keys():
    #     mask = df_stock["ticker"] == ticker
    #     file_name = str(ticker)+".csv"
    #     df_stock[mask].to_csv(path+file_name)



    #####usare il nuovo dataset e vedere se fino al 31 12 2017 il numero di record è lo stesso. se cosi fosse allora si usa direttamente quello

    df_stock_2018 = pd.read_csv("historical_stock_prices copia.csv")
    # print(df_stock)
    mask = (df_stock_2018['date'] >= '2016-11-01') & (df_stock_2018['date'] <= '2018-02-31') & (df_stock_2018["ticker"].isin(symbol_to_name.keys()))
    df_stock_2018 = df_stock_2018[mask]
    df_stock_2018.reset_index(inplace=True)
    df_stock_2018["year"] = df_stock_2018.apply(lambda row: row["date"].split("-")[0], axis=1)
    df_stock_2018["month"] = df_stock_2018.apply(lambda row: row["date"].split("-")[1], axis=1)
    df_stock_2018["day"] = df_stock_2018.apply(lambda row: row["date"].split("-")[2], axis=1)

    #df_stock_2018.rename(columns={"Name": "ticker"}, inplace=True)

    #symbol_to_name.setdefault('missing_key', 'default value')
    #name_to_symbol.setdefault('missing_key', 'default value')
    df_stock_2018["name"] = df_stock_2018.apply(lambda row: symbol_to_name.get(row["ticker"], "DEFAULT"), axis=1)

    print(df_stock_2018)
    df_stock_2018.to_csv('stock_data2.csv')

    path = "AllRetPrices/"

    tickers_to_drop = ["BHF", "LUK", "BRK.B", "GGP", "WYN", "BF.B", "CSRA", "SBAC",
                       "CBG", "MON", "PCLN", "TWX", "RSG", "PFG", "HCN", "SNI"]

    for ticker in symbol_to_name.keys():
        if ticker not in tickers_to_drop:
            mask = df_stock_2018["ticker"] == ticker
            file_name = str(ticker) + ".csv"
            df_stock_2018[mask].to_csv(path + file_name)

    #mask = df_stock["name"] == "Aetna Inc"
    #print(len(df_stock[mask]["date"]))

import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':

    # df_stock = pd.read_csv("historical_stock_prices copia.csv")
    # mask = df_stock["date"].str.startswith("2018")
    # print(df_stock[mask]["date"].unique())
    #print(df_stock["date"].unique())

    #index = df_stock[df_stock['Date'] == "2017-02-02"].index.tolist()[0]
    #mask = df_stock["date"].str.startswith("2017-02-02")
    #mask = df_stock["year"] == 2018
    #print(df_stock[mask])



    onlyfiles = [f for f in listdir("AllRetPrices") if isfile(join("AllRetPrices", f))]

    # #for file in onlyfiles: #["BHF.csv"]:#onlyfiles:
    # for file in ["NWS.csv"]:
    #     path = "AllRetPrices/"+str(file)
    #     df_stock = pd.read_csv(path)
    #     #print(df_stock["date"].unique())
    #     #if len(df_stock) < 333:
    #         #print(str(file)+ ": "+str(len(df_stock)))
    #     print(df_stock)
    #     #break



        #a quanto pare ci sono degli stock marci con 332, 162, 32 o addirittura 0 record. va indagato cosa sono e perche non ci siano dati
        #se non sono tra quelli usati per il test e se non compaiono nel dataset si buttano nel cesso

        # R S G.csv: 32   !!!!! scelgo momentaneamente arbitrariamente di droppare l'unico ticker che ha effetticamente (ben) due cartelle di video


    #vol = np.log(np.sqrt(np.sum(np.square(list_tmp - mean_r)) / (duration)))

    df_stock = pd.read_csv("train_data.csv")

    print(df_stock.columns)
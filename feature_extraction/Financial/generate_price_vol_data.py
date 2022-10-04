import os 
import csv
import pandas as pd
import sys
import numpy as np
import calendar
import json
from pathlib import Path
import warnings
warnings.filterwarnings("error")

count = 0


def get_date(year,month,day):
    if(len(month)==1):
        month = "0"+month
    
    if(len(day)==1):
        day = "0"+day
        
    date = year+month+day
    return date

def volatality_past(list_val ,anchor ,duration ):

    list_tmp = list_val[anchor+1:anchor+duration+1]
    #print("suca")
    #print(list_tmp)
    mean_r = np.mean(list_tmp)
    #print(mean_r)
    if np.all(np.array(list_tmp) == list_tmp[0]): #vettore costante
        return 0
    try:
        vol = np.log(np.sqrt(np.sum(np.square(list_tmp - mean_r))/(duration)))
    except:
        print(list_val)
        print(dateee)
        print(ddd)
        print(stock_name)
        vol = 0

    return vol

def volatality_fut(list_val , anchor ,duration ):
    list_tmp = list_val[anchor-duration:anchor]
    mean_r = np.mean(list_tmp)

    if np.all(np.array(list_tmp) == list_tmp[0]):  # vettore costante
        return 0

    vol = np.log(np.sqrt(np.sum(np.square(list_tmp - mean_r))/(duration)))
    return vol
    

def remove_dollar(string):
    
    try :
        return float(string.replace('$',''))
    except AttributeError :
        return float(string)
        

def calculate_vol(data_frame):
    #list_val =np.asarray(data_frame.iloc[:,0].tolist())
    list_val = np.asarray(data_frame.loc[:, "close"].tolist())
    list_val = [remove_dollar(x)  for x in list_val]
    list_val_r = []  
    for i in range(0 , len(list_val)-1):
        try :
            list_val_r.append((list_val[i] - list_val[i+1])/list_val[i+1])
            
        except ZeroDivisionError :
            print(i,list_val[i] , list_val[i+1])
        
    #print(list_val_r)
    global ddd
    ddd = data_frame
    past_3 = volatality_past(list_val_r , 30 , 3)
    past_7 = volatality_past(list_val_r, 30 , 7)
    past_15 = volatality_past(list_val_r, 30 , 15)
    past_30 = volatality_past(list_val_r, 30 , 30)
    fut_3 = volatality_fut(list_val_r , 30 ,  3)
    fut_7 = volatality_fut(list_val_r , 30 ,  7)
    fut_15 = volatality_fut(list_val_r , 30 ,  15)
    fut_30 = volatality_fut(list_val_r , 30 ,30)

    if(list_val[27]>list_val[28]):
        lab_3 = 1
    else :
        lab_3 = 0

    if(list_val[23]>list_val[24]):
        lab_7 = 1
    else :
        lab_7 = 0

    if(list_val[15]>list_val[16]):
        lab_15 = 1
    else :
        lab_15 = 0

    if(list_val[0]>list_val[1]):
        lab_30 = 1
    else :
        lab_30 = 0                        

    
    
    return past_3 , past_7 , past_15 ,past_30 , fut_3 , fut_7 , fut_15 ,fut_30, lab_3,lab_7,lab_15,lab_30
    

def get_value(row):
    #file = os.path.join("../../data/AllRetPrices/",row.ticker+".csv")
    if row.year == 2018 or row.year == 2016:
        return [None, None, None, None, None, None]

    file = os.path.join("AllRetPrices/", row.ticker + ".csv")

    if file in tickers_to_drop:
        return [None, None, None, None, None, None]
    
    global stock_name
    stock_name = row.ticker

    try:
        df = pd.read_csv(file)
    except FileNotFoundError:
        #file = os.path.join("../../data/AllRetPrices/",row.ticker+".xls")
        file = os.path.join("AllRetPrices/", row.ticker + ".xls")
        try :
            df = pd.read_csv(file)
           
            
        except FileNotFoundError :
        
            print("File Not Found :",file)
            return [None , None , None, None, None, None]

    # mask = df['date'] >= '2017-12-30'
    # print(df[mask]['date'].unique())

    #df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = pd.to_datetime(df['date'])
    if(len(str(row.month))==1):
        month = "0"+str(row.month)
    else: 
        month = str(row.month)
    if(len(str(row.day))==1):
        day = "0"+str(row.day)
    else: 
        day = str(row.day)
        
    date = str(row.year)+'-'+month+'-'+day


    index = df[df['Date'] == date].index.tolist()[0]
    offset = 0 ####
   
      
    
    #data_frame_volatality = df.iloc[index -30:index + 32 , 1:2]
    data_frame_volatality = df.loc[index - 30: index + 32, ["Date", "close"]]
    #print(len(data_frame_volatality))

    # print("dio")
    # try:
    #     print(date, row.ticker)
    #     print(data_frame_volatality.iloc[index+offset]["Date"])
    #     print(data_frame_volatality.iloc[0, 0])
    # except:
    #     print("maledetto")
    #     print(index)
    #     print(data_frame_volatality)
    #
    # print("ladro")
    global dateee
    dateee = date
    past_3 , past_7 , past_15 ,past_30 , future_3 , future_7 , future_15 ,future_30,lab_3,lab_7,lab_15,lab_30 = calculate_vol(data_frame_volatality)
    
    
    return [past_3 , past_7 , past_15 ,past_30 , future_3 , future_7 , future_15 ,future_30,lab_3,lab_7,lab_15,lab_30 ]



if __name__ == '__main__':
    print("Giovanni")
    #data = pd.read_csv("../../data/stock_data.csv")
    #data = pd.read_csv("stock_data.csv")
    data = pd.read_csv("stock_data2.csv")

    tickers_to_drop = ["BHF.csv", "LUK.csv", "BRK.B.csv", "GGP.csv", "WYN.csv", "BF.B.csv","CSRA.csv", "SBAC.csv","CBG.csv","MON.csv", "PCLN.csv","TWX.csv", "RSG.csv","PFG.csv","HCN.csv","SNI.csv"]

    #data["text_file_name"] = data.apply(lambda row : str(row['name'])+"_"+get_date(str(row.year),str(row.month),str(row.day))+"/Text.txt" ,axis =1)
    data["text_file_name"] = data.apply(lambda row : str(row['name'])+"_"+get_date(str(row.year),str(row.month),str(row.day))+"/TextSequence.txt" ,axis =1)
    #mask = data['date'] >= '2017-11-13'
    #print(data[mask]['date'].unique())
    data_tmp = data.apply(lambda row : get_value(row) ,axis =1).tolist()
    data_tmp = pd.DataFrame(data_tmp , columns = ['past_3' , 'past_7' , 'past_15' ,'past_30' , 'future_3' , 'future_7' , 'future_15' ,'future_30',"lab_3","lab_7","lab_15","lab_30"])

    data_final = pd.concat([data , data_tmp] , axis  = 1)
    data_final = data_final.dropna()
    #data_final.to_csv('../../data/price_vol_data.csv',index=False)
    #data = pd.read_csv("../../data/price_vol_data.csv")
    data_final.to_csv('price_vol_data.csv',index=False)
    data = pd.read_csv("price_vol_data.csv")
    data['total_days'] = data.apply(lambda row : row.month*30 + row.day , axis = 1)

    data = data.sort_values(by = 'total_days')
    row = len(data)
    data = data.drop(columns=  ["total_days"])
    #train_split = int(row*0.6)
    train_split = int(row * 0.7) #cosi si dice nel paper
    #val_split =train_split+ int(row*0.2)
    val_split = train_split + int(row * 0.1)

    data_train = data[:train_split]
    data_val = data[train_split:val_split]
    data_test = data[val_split:]

    # data_train.to_csv('../../data/train_data.csv',index=False)
    # data_val.to_csv('../../data/val_data.csv')
    # data_test.to_csv('../../data/test_data.csv',index=False)

    data_train.to_csv('train_data.csv', index=False)
    data_val.to_csv('val_data.csv')
    data_test.to_csv('test_data.csv', index=False)




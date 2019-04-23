#import mod_initialize
import urllib3 as req
import json
import csv
from bs4 import BeautifulSoup as bs
import sys 

req.disable_warnings()

def ConnectToService(apikey):
    print (apikey) 
    print ("Connecting")
    conn_url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=DXC&apikey=' + apikey
    print (conn_url)
    con = req.PoolManager()
    resp = con.request('GET', conn_url)
    soup = bs(resp.data, 'html.parser')
    print ("received")
    print (soup)
    resp.close()
    resp.release_conn()
    return soup

def FormatData(soup):
    print ("Formatting")
    js = json.loads(str(soup))
    js2 = js['Global Quote']
    write_array = []
    for x, y in js2.items():
        write_array.append(y)    
    print(write_array)
    return write_array

def AppendToFile(write_array):
    print ("printing input")
    print (write_array)
    with open('StockQuotes.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(write_array)    

def CloseConToService(resp):
    resp.close()

if __name__ == "__main__":
    soup = ConnectToService(str(sys.argv[1]))
    aray = FormatData(soup)
    AppendToFile(aray)


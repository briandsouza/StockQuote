import urllib3 as req
import json
import csv
from bs4 import BeautifulSoup as bs
import sys 

req.disable_warnings()

def ConnectToService(cmpname, apikey):
    print ("-----------------------------Connecting---------------------------------------")
    conn_url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + cmpname + '&apikey=' + apikey
    con = req.PoolManager()
    resp = con.request('GET', conn_url)
    soup = bs(resp.data, 'html.parser')
    print ("---------------------------Quote Received----------------------------------------")
    resp.close()
    resp.release_conn()
    return soup

def FormatData(soup):
    js = json.loads(str(soup))
    js2 = js['Global Quote']
    write_array = []
    for x, y in js2.items():
        write_array.append(y)    
    return write_array

def AppendToFile(write_array):
    print ("---------------------Saving Output to File--------------------------")
    with open('StockQuotes.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(write_array)    
    print ("-----------------------Finished Writing File------------------------")

def CloseConToService(resp):
    resp.close()

if __name__ == "__main__":
    #To Do
    #Need to sanitize the URL and arguments
    soup = ConnectToService(str(sys.argv[1]),str(sys.argv[2]))
    aray = FormatData(soup)
    AppendToFile(aray)

import requests
from bs4 import BeautifulSoup
import time, csv, random, re, os
from multiprocessing import Process
import multiprocessing
session = requests.Session()
session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
page = 1
def upData(csvname, data):
    file = open(csvname + ".csv", "a", encoding="utf-8")
    writer = csv.writer(file, delimiter=",", lineterminator="\n")
    for list_ in data:
        writer.writerow(list_)
    file.close()
def getList(filename):
    with open(filename, 'r', errors='ignore') as file:
        reader = csv.reader(file)
        mlinks = list(reader)
        file.close()
    return mlinks
def getLabel(label, data):
    tresult = {}
    if 'WhoisSever:' in label:
        tresult['whoisserver'] = data
    if 'Email:' in label:
        tresult['email'] = data
    if 'Name:' in label:
        tresult['name'] = data
    if 'Address:' in label:
        tresult['address'] = data
    if 'Country:' in label:
        tresult['country'] = data
    if 'Telephone' in label:
        tresult['phone'] = data
    return tresult
def GetLinkDetail(mdata, pc, send_end):
    global csvname
    #global lines
    soup = makesoup(mdata)
    #print(mdata)
    #mdata = {'fname':lines[pc][0], 'lname':lines[pc][1]}
    ndata = []
    try:
        de = soup.find('div', {'id':'collapseTwelve'}).find('div', {'class':'panel-body'}).find('ul', {'class':'eachaccordionrst'}).findAll('li')
        #print (str(pc) + ' : ' + str(len(de)))
    except:
        pass
    try:
        for cde in de:
            try:
                res = {}
                country = '',
                address = '',
                whoisserver = '',
                email = ''
                name = ''
                phone = ''
                sname = ''
                domain = ''
                try:
                    sname = str(cde.find('h4').text).split('registered')[0]
                except:
                    pass
                try:
                    domain = str(cde.find('h4').text).split('"')[1]
                except:
                    pass
                cb = cde.findAll('p')
                for item in cb:
                    try:
                        label = item.text
                        data = item.find('span').text
                        res.update(getLabel(label, data))
                    except:
                        pass
                if 'email' in res:
                    email = res['email']
                if 'country' in res:
                    country = res['country']
                if 'address' in res:
                    address = res['address']
                if 'whoisserver' in res:
                    whoisserver = res['whoisserver']
                if 'name' in res:
                    name = res['name']
                if 'phone' in res:
                    phone = res['phone']
                data = [sname, domain, name, address, country, whoisserver, email, phone]
                ndata.append(data)
                #print(data)
                #print(data)
                #combineRows(data, pc)
            except:
                pass
    except:
        pass
    print('ndata: ' + str(len(ndata)))
    send_end.send(ndata)
def combineRows(data, pc):
    global resultRow
    resultRow.append(data)
    #print(data)
    print('in resultRow length of ' + str(len(resultRow)))
    if len(resultRow) > 10:
        print ('now length of rows in resultRow greater than 100')
        savelist(csvname, resultRow)
        resultRow = []
'''
def collDetails(soup):
    global pc
    try:
        de = soup.find('div', {'id':'collapseTwelve'}).find('div', {'class':'panel-body'}).find('ul', {'class':'eachaccordionrst'}).findAll('li')
        print (str(pc) + ' : ' + str(len(de)))
    except:
        pass
    try:
        for cde in de:
            cs(cde)
    except:
        pass
'''
def savelist(filename, flist):
    for row in flist:
        with open(filename + '.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(row)
            f.close()
def waitLong():
    time.sleep(random.uniform(2.5, 3.1))
def makesoup(mdata):
    soup = None
    #global lines
    url = 'https://cubib.com/search_results.php'
    #mdata = {'fname':lines[pc][0], 'lname':lines[pc][1]}
    try:
        s = requests.post(url, params=mdata)
        if s.status_code == 200:
            soup = BeautifulSoup(s.text, 'html.parser')
        else:
            print ('request not accept by website!!!!!!')
    except:
        print ("Internet connection problem...")
        #print (str(pc) + ' : ' + str(mdata))
        #waitLong()
    return soup

def formatString(data):
    data = data.replace("\t", " ")
    data = data.replace("\n", " ")
    data = " ".join(data.split())
    return data

def collectData(pc):
    global lines
    result = []
    lcounter = 0
    while pc < 199999:
        lcounter+=1
        tcounter = 0
        pipe_list = []
        procs = []
        for i in range(0, 5):
            tcounter+=1
            mdata = {'fname':lines[pc][0], 'lname':lines[pc][1]}
            recv_end, send_end = multiprocessing.Pipe(False)
            proc = Process(target=GetLinkDetail, args=(mdata, pc, send_end))
            procs.append(proc)
            pipe_list.append(recv_end)
            proc.start()
            pc += 1
            print ('Loop: ' + str(lcounter) + ' Thread: ' + str(tcounter) + ' pc: ' + str(pc))
        for proc in procs:
            proc.join()
        result = [x.recv() for x in pipe_list]
        #print (str(len(result)))
        #print(result)
        fresult = []
        for rows in result:
            fresult.extend(rows)
        #upData(csvname, result[0])
        print ('fdata: ' + str(len(fresult)))
        savelist(csvname, fresult)
if __name__ == "__main__":
    result = []
    ac = []
    tup = []
    resultRow = []
    #pc=200323
    pc=198271
    lines = getList('names.csv')
    csvname = "cubib_12"
    #CreateCSV(csvname)
    #session = requests.Session()
    #restoreLog()
    collectData(pc)
    #wholeState()
    #updateLog()

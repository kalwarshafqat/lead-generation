from proxyscrape import create_collector
import csv, re, time, random, json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver import Proxy
from selenium.webdriver.chrome.options import Options
import itertools
import operator
import datetime
import requests
import urllib
import warnings, sys, urllib
from fake_useragent import UserAgent
from lxml import html
session = requests.Session()
if not sys.warnoptions:
    warnings.simplefilter("ignore")
url = 'https://cubib.com/search_results.php'
#import pandas as pd
#lines = getList('walkerindustrial_00_4_links.csv')
pl=['181.225.213.227:999', '186.159.3.193:56861', '45.130.229.230:443', '1.10.188.78:45208', '103.27.160.239:3128', '43.241.141.28:35101', '190.145.200.126:53281', '211.24.95.49:47615', '103.241.227.110:6666', '188.156.240.240:8118', '46.0.203.186:8080', '31.43.180.68:8080', '103.80.61.79:8080', '59.125.123.129:81', '51.158.165.18:8811', '104.236.33.114:3128', '170.81.35.26:36681', '89.248.244.182:8080', '103.124.137.173:3127', '103.241.227.118:6666', '103.12.161.194:59777', '80.123.143.202:47362', '195.225.48.177:58302', '51.75.147.132:8888', '178.62.56.172:80', '161.35.4.201:80', '193.149.225.224:80', '51.75.147.33:3128', '192.109.165.108:80', '169.255.75.117:34403', '43.229.252.45:53281', '191.101.39.27:80', '162.214.92.202:80', '185.198.188.55:8080', '51.81.82.175:80', '103.218.240.75:80', '103.152.5.80:8080', '66.70.229.119:43567', '103.115.255.28:80', '103.157.116.199:8080', '3.25.29.231:3128', '1.20.103.196:42792', '159.65.154.238:80', '172.104.56.66:8899', '192.109.165.58:80', '96.9.69.164:53281', '172.104.160.11:8889', '181.196.254.202:53281', '159.203.25.49:3128', '119.82.252.29:46872', '208.80.28.208:8080', '61.29.96.146:80', '118.172.201.49:52111', '200.62.96.71:80', '187.111.160.6:8080', '125.26.7.124:61642', '34.203.142.175:80', '117.197.102.194:80', '173.212.202.65:80', '191.101.39.29:80', '182.52.51.10:61124', '54.151.132.183:3128', '54.156.164.61:80', '191.101.39.2:80', '5.9.104.170:80', '192.109.165.124:80', '5.189.133.231:80', '103.115.253.47:80', '74.143.245.221:80', '14.99.225.209:80', '14.99.225.212:80', '49.204.79.81:80', '136.233.215.139:80', '51.158.180.179:8811', '89.113.103.174:8080', '206.189.1.220:3128', '177.87.168.6:53281', '180.250.12.10:80', '103.134.168.81:80', '103.115.253.177:80']
pi=0
collector = create_collector('my-collector', ['socks4', 'socks5', 'http'])
successfullproxies = []
proxyCounter=0
def sd():
	global browser
	i = 0
	while i<3:
		scroll = browser.find_element_by_tag_name('body').send_keys(Keys.END)
		time.sleep(0.5)
		i+=1
	scroll = browser.find_element_by_tag_name('body').send_keys(Keys.UP)
	scroll = browser.find_element_by_tag_name('body').send_keys(Keys.UP)
def initBrowser(px):
	settings = {
        "httpProxy": px,
        "sslProxy": px
    }
	proxy = Proxy(settings)
	cap = DesiredCapabilities.CHROME.copy()
	cap['platform'] = "WINDOWS"
	cap['version'] = "10"
	proxy.add_to_capabilities(cap)
	driver = ChromeDriver(desired_capabilities=cap, executable_path='D:\Python37-32\chromedriver.exe')
	return driver
def getplupdate():
	global browser
	global pl
	pl = []
	#browser.get('https://free-proxy-list.net/')
	soup = bsoup(browser)
	de = soup.find('table', {'id':'proxylisttable'}).find('tbody').findAll('tr')
	for item in de:
		pl.append(item.findAll('td')[0].text + ':'+item.findAll('td')[1].text)
def performQuery(query, queryIndex):
	fc=1
	tc=1
	pc=1
	mrows = 0
	header = getList('D:\\workspace\\data\\faheem\\apollo linkedin title\\linkedin_person_Accounts Payable_Receivable Clerk_1.csv')
	header = header[0]
	nlines = []
	nlines.append(header)
	cfile = open('D:\\workspace\\data\\faheem\\apollo linkedin\\Apollo_V7_V5_per_all_fields.csv', 'r', encoding='utf-8-sig')
	while 1:
		line = cfile.readline()
		line = line.replace('\n', '')
		row = line.split('\t')
		crow = []
		try:
			if query in row[queryIndex]:
				crow = row
				pc+=1
		except:
			pass
		if len(crow) > 0:
			 nlines.append(crow)
		tc+=1
		if pc>100000:
			savefile('linkedin_person_' + query + '_' + str(fc), nlines)
			fc+=1
			pc=1
			nlines = []
			nlines.append(header)
		if tc> 1000000:
			mrows+=1
			tc=0
			print(str(mrows) + ' million lines processed, nlines: ' + str(len(nlines)))
			if mrows > 94:
				mrows = 0
				if len(nlines) > 1:
					savefile('linkedin_person_' + query + '_' + str(fc), nlines)
					break
def get_leaves(item, key=None):
	if isinstance(item, dict):
		leaves = {}
		for i in item.keys():
			leaves.update(get_leaves(item[i], i))
		return leaves
	elif isinstance(item, list):
		leaves = {}
		for i in item:
			leaves.update(get_leaves(i, key))
		return leaves
	else:
		return {key : item}
def json2csv(filename, data):
	sdata = []
	for item in data:
		sdata.append(getJsonObjectSerialized(item))
	fieldnames = set()
	for entry in sdata:
		fieldnames.update(get_leaves(entry).keys())
	with open(filename + '.csv', 'w', encoding='utf-8', newline='') as f_output:
		csv_output = csv.DictWriter(f_output, fieldnames=sorted(fieldnames))
		csv_output.writeheader()
		csv_output.writerows(get_leaves(entry) for entry in sdata)
def getListSerialized(key,values):
	rdict = {}
	counter = 1
	for value in values:
		rdict.update({key + '/' +str(counter):value})
		counter+=1
	return rdict
def getDictSerialized(mKey, values):
	rdict = {}
	for k, v in values.items():
		rdict.update({mKey + '/' + k:v})
	return rdict
def getJsonObjectSerialized(cobject):
	rdict = {}
	for k,v in cobject.items():
		if 'list' in str(type(v)).split("'")[1]:
			rdict.update(getListSerialized(k,v))
		elif 'dict' in str(type(v)).split("'")[1]:
			rdict.update(getDictSerialized(k, v))
		else:
			rdict.update({k:v})
	return rdict
def tbrowser():
	options = Options()
	prefs = {
		"translate_whitelists": {"fr":"en"},
		"translate":{"enabled":"true"}
		}
	options.add_experimental_option("prefs", prefs)
	return webdriver.Chrome(chrome_options=options)
def bsoup(browser):
	return BeautifulSoup(browser.page_source, 'html.parser')
def csvfromExcel(bookName):
	data_xls = pd.read_excel(bookName, 'Sheet1', index_col=None)
	csvName = bookName.split('.')[0] + '_csv.csv'
	data_xls.to_csv(csvName, encoding='utf-8')
	lines = getList(csvName)
	return lines
def getPC(filename):
	pc=0
	lines = getList(filename + '.csv')
	lines1 = getList('names.csv')
	lname = lines[-1][0]
	fname = lname.split(' ')[1]
	lname = lname.split(' ')[0]
	for i in range(0, len(lines1)):
		if fname in lines1[i]:
			if lname in lines1[i]:
				print ('pc= ' + str(i))
				pc= i
				break
	return pc
def formatString(data):
	data = data.replace("\t", " ")
	data = data.replace("\n", " ")
	data = " ".join(data.split())
	return data
def start(pc, endlimit):
	while 1:
		try:
			r = requests.get(lines[pc][0], timeout=5)
			rsoup = BeautifulSoup(r.content, 'html.parser')
			getDetails(rsoup, lines[pc][0])
			pc+=1
			pnoc=0
		except:
			pnoc+=1
			if pnoc > 10:
				pc+=1
				pnoc=0
			waitLong()
		if pc > endlimit:
			break
#from fake_useragent import UserAgent
#ua = UserAgent()
flist = []
ritems =[]
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
def cs(ce):
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
		sname = str(ce.find('h4').text).split('registered')[0]
	except:
		pass
	try:
		domain = str(ce.find('h4').text).split('"')[1]
	except:
		pass
	cb = ce.findAll('p')
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
	with open(r'cubib_9.csv', 'a', encoding='utf-8') as f:
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(data)
		f.close()
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
def haveIn(link, ol):
	found = True
	for i in range(0, len(ol)):
		if ol[i][-1] == link:
			found = False
	return found
def getRemainings(lines, l):
	rlinks = []
	for i in range(0, len(l)):
		if haveIn(l[i], lines):
			rlinks.append(l[i])
	return rlinks
def Browser2():
	chrome_options = Options()
	prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096 }
	chrome_options.add_experimental_option("prefs", prefs)
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('window-size=1200,1100')
	chrome_options.add_experimental_option("detach", True)
	return webdriver.Chrome(options=chrome_options)
def removeNonAscii(te):
	return ''.join(c for c in te if ord(c) < 128)
def updateRow(csvname, row):
	file = open(csvname + ".csv", "a", encoding='utf-8')
	writer = csv.writer(file, delimiter=",", lineterminator='\n')
	writer.writerow(row)
	file.close()
def getNumbers(te):
	tc = 0
	ld = re.findall(r'\d+', te)[0]
	return int(ld)
def removeUC(text):
	return re.sub(r'[^\x00-\x7f]',r' ',text)
def formatString(data):
	data = data.replace("\t", " ")
	data = data.replace("\n", " ")
	data = " ".join(data.split())
	return data
def getList(filename):
	with open(filename, 'r', errors='ignore') as file:
		reader = csv.reader(file)
		mlinks = list(reader)
		file.close()
	return mlinks
def wait():
    time.sleep(random.uniform(2.1, 2.9))
def waitLong():
    time.sleep(random.uniform(4.1, 5.9))
def waitSmall():
    time.sleep(random.uniform(0.1, 0.5))
def pbrowser():
	options = webdriver.ChromeOptions()
	options.add_argument('--load-extension=C:/Users/Shayan/AppData/Local/Google/Chrome/userda~1/Default/Extensions/bihmplhobchoageeokmgbdihknkjbknd/4.1.0_0')
	options.add_argument('--load-extension=C:/Users/Shayan/AppData/Local/Google/Chrome/User Data/Default/Extensions/kalfeohpimfncbfhjhanngehpbfilokk/2.0.10_0')
	browser = webdriver.Chrome(chrome_options=options)
	return browser
#browser = pbrowser()
def savetextfile(fn, txt):
	file = open(fn + '.txt', 'a', encoding='utf-8')
	file.writelines(txt)
	file.close()
def savelist(filename, flist):
	with open(filename, 'a', encoding='utf-8') as f:
		writer = csv.writer(f, lineterminator='\n')
		for data in flist:
			ndata = [data]
			writer.writerow(ndata)
		f.close()
def CollectLinks():
	global browser
	global new_links
	global mpl
	global more_cat
	links1 = getMlinks()
	new_links.extend(getLinks())
	clinks = getLinks()
	clink = browser.current_url
	if len(clinks) == 300:
		mpl.append(clink)
	print ('1 level links are : ' + str(len(links1)))
	for link1 in links1:
		browser.get(link1)
		waitSmall()
		new_links.extend(getLinks())
		clinks = getLinks()
		if len(clinks) == 300:
			mpl.append(link1)
		links2 = getMlinks()
		if len(links2) > 0:
			print ('2 level links are : ' + str(len(links2)))
			for link2 in links2:
				browser.get(link2)
				waitSmall()
				new_links.extend(getLinks())
				clinks = getLinks()
				if len(clinks) == 300:
					mpl.append(link2)
				links3 = getMlinks()
				if len(links3) > 0:
					print ('3 level links are : ' + str(len(links3)))
					for link3 in links3:
						browser.get(link3)
						waitSmall()
						new_links.extend(getLinks())
						clinks = getLinks()
						if len(clinks) == 300:
							mpl.append(link3)
						links4 = getMlinks()
						if len(links4) > 0:
							print ('4 level links are : ' + str(len(links4)))
							for link4 in links4:
								browser.get(link4)
								waitSmall()
								new_links.extend(getLinks())
								clinks = getLinks()
								if len(clinks) == 300:
									mpl.append(link4)
								links5 = getMlinks()
								if len(links5) > 0:
									print ('5 level links are : ' + str(len(links5)))
									for link5 in links5:
										browser.get(link5)
										waitSmall()
										new_links.extend(getLinks())
										clinks = getLinks()
										if len(clinks) == 300:
											mpl.append(link5)
										links6 = getMlinks()
										if len(links6) > 0:
											print ('6 level links are : ' + str(len(links6)))
											for link6 in links6:
												browser.get(link6)
												waitSmall()
												new_links.extend(getLinks())
												clinks = getLinks()
												if len(clinks) == 300:
													mpl.append(link6)
												links7 = getMlinks()
												if len(links7) > 0:
													print ('7 level links are : ' + str(len(links7)))
													for link7 in links7:
														browser.get(link7)
														waitSmall()
														new_links.extend(getLinks())
														clinks = getLinks()
														if len(clinks) == 300:
															mpl.append(link7)
														links8 = getMlinks()
														if len(links8) > 0:
															more_cat.extend(links8)
def changeSession():
    session = requests.Session()
    session.headers['User-Agent'] = str(ua.random)
    return session
def maketree(url):
    global session
    tree = None
    crawled = True
    while crawled:
        try:
            r = session.get(url, timeout=3, verify=False)
            tree = html.fromstring(r.text)
            crawled = False
        except:
            session = changeSession()
            waitSmall()
    return tree
def makesoup(url):
    global session
    soup = None
    crawled = True
    while crawled:
        try:
            r = session.get(url, timeout=3, verify=False)
            soup = BeautifulSoup(r.text, 'html.parser')
            crawled = False
        except:
            session = changeSession()
            waitSmall()
    return soup
def makeresp(url):
    global session
    r = None
    crawled = True
    while crawled:
        try:
            r = session.get(url, timeout=3, verify=False)
            crawled = False
        except:
            session = changeSession()
            waitSmall()
    return r
ua = UserAgent()
session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
def loadJson(filename):
	with open(filename + '.json') as handle:
		dictdump = json.loads(handle.read())
	return dictdump
def saveJson(filename, prods):
	with open(filename + ".json", "w") as write_file:
		json.dump(prods, write_file)
def savefile(filename, flist):
	with open(filename + '.csv', 'a', encoding='utf-8') as f:
		writer = csv.writer(f, lineterminator='\n')
		for data in flist:
			writer.writerow(data)
		f.close()
print ("getLabel(label, data), formatString(),getList(), wait(), waitLong(), savefile(), pbrowser(), savelist(), functions are loaded")

###============================================== wsemi =========================
pros = []
epros = []
rlinks = []
pc = 10012
lines = getList('wsemi_links.csv')
def burl(url):
	global browser
	soup = ''
	success = False
	global pc
	global links
	global rlines
	rc = 0
	tl = 0
	while 1:
		waitLong()
		try:
			browser.set_page_load_timeout(60)
			browser.get(url)
		except:
			pass
		try:
			soup = bsoup(browser)
			itn = soup.find('h1', {'class':'text_join_big'}).text
			utn = url.split('/')[-1]
			if utn in itn:
				success = True
			else:
				rc+=1
		except:
			pass
		if success == True:
			break
		if rc > 5:
			pc+= 1
			rc = 0
			tc+=5
			if tc > 13:
				break
			rlinks.append(url)
			url = lines[pc][0]
	return soup
def getelinks(soup, totalVendorListings):
	relinks = []
	try:
		elinks = soup.find('table', {'class':'linkage'}).find('tbody').findAll('a', {'class':'view_vendor'})
	except:
		elinks = []
	if len(elinks) == 0:
		for i in range(0, totalVendorListings):
			relinks.append('')
	elif len(elinks) > 0:
		for i in range(0, totalVendorListings):
			try:
				nelink = 'https://www.ebay.com/itm/' + elinks[i]['href'].split('?id=')[1]
				relinks.append(nelink)
			except:
				relinks.append('')
	return relinks
def savedata():
	global pc
	global pros
	global epros
	savefile('wsemi_epros_' + str(pc), epros)
	saveJson('wsemi_pros_' + str(pc), pros)
def getEbayDetails(soup, wsemiVendor, link):
	try:
		seller = soup.find('span', {'class':'mbg-nw'}).text
	except:
		seller = ''
	try:
		image = soup.find('img', {'itemprop':'image'})['src']
	except:
		image = ''
	try:
		status = soup.find('', {'itemprop':'itemCondition'}).text
	except:
		status = ''
	try:
		price = soup.find('span', {'itemprop':'price'})['content']
	except:
		price = ''
	try:
		mpn = soup.find('', {'itemprop':'mpn'}).text
	except:
		try:
		     mpn = soup.find('', {'itemprop':'model'}).text
		except:
		     mpn = ''
	try:
		qty = soup.find('input', {'name':'quantity'})['value']
	except:
		qty = ''
	try:
		stock = soup.find('span', {'id':'qtySubTxt'}).text
	except:
		stock = ''
	try:
		location = soup.find('', {'itemprop':'availableAtOrFrom'}).text
	except:
		location = ''
	data = [formatString(mpn), formatString(wsemiVendor), link, formatString(seller), formatString(status), qty, formatString(price), image, formatString(stock), formatString(location)]
	return data

def getDetails(de, link, ebaylink):
	data = []
	email = ''
	phone = ''
	country = ''
	j = de.findAll('tr')[0].findAll('td')[0].text.split('\n')
	desc = de.findAll('tr')[1].findAll('td')[0].text
	company = j[1]
	if '[view on eBay]' in company:
		company = company.replace('[view on eBay]', '')
	for item in j:
		if 'Email' in item:
			email = item.split(':')[1]
		if 'Phone' in item:
			phone = item.split(':')[1]
		if 'Country' in item:
			country = item.split(':')[1]
	x = de.findAll('tr')[0].findAll('td')[0].text
	if 'Login to view' in x:
		email = 'login required'
	try:
		istatus = de.findAll('tr')[0].findAll('td')[1].text
	except:
		istatus = ''
	try:
		price = de.findAll('tr')[0].findAll('td')[5].text
	except:
		price = ''
	try:
		stock = de.findAll('tr')[0].findAll('td')[4].text
	except:
		stock = ''
	try:
		image = de.findAll('tr')[0].find('a').find('img')['src']
	except:
		image = ''
	part = link.split('/')[-1]
	return {'image':image, 'ebaylink':ebaylink, 'stock':stock, 'desc':desc,'mpn': part, 'company':company, 'email':email, 'phone':phone, 'country':country, 'status':istatus, 'price':formatString(price), 'link':link}
def getWsemiDetails(soup):
	global pros
	try:
		de = soup.find('table', {'class':'linkage'}).find('tbody').findAll('table')
	except:
		de = []
	if len(de) > 0:
		elinks = getelinks(soup, len(de)+1)
		plcounter = 0
		for item in de:
			nitem = getDetails(item, lines[pc][0], elinks[plcounter])
			plcounter+=1
			pros.append(nitem)
	else:
		nitem = {'link':lines[pc][0]}
'''		pros.append(nitem)
def crawl():
	global pc
	global epros
	global pros
	global lines
	global browser
	global pl
	global pi
	while 1:
		waitSmall()
		try:
			pc+=1
			browser.set_page_load_timeout(220)
			browser.get(lines[pc][0])
		except:
			browser = getBrowser(pl[pi])
			pi+=1
			if pi > len(pl)-1:
                            break
		if url.split('/')[-1] in browser.title:
			soup = bsoup(browser)
			try:
				de = soup.find('table', {'class':'linkage'}).find('tbody').findAll('table')
				elinks = getelinks(soup, len(de)+1)
				plcounter = 0
				for item in de:
					nitem = getDetails(item, lines[pc][0], elinks[plcounter])
					plcounter+=1
					if 'ebay' in elinks[plcounter]:
						esoup = makesoup(elinks[plcounter])
						epros.append(getEbayDetails(esoup, nitem['company'], elinks[plcounter]))
					pros.append(nitem)
			except:
				nitem = {'link':lines[pc][0]}
				pros.append(nitem)
		else:
			pc-=1
		if pc > len(lines)-1:
			break
'''
def getpbrowser(browser, url):
	global pl
	#global proxyCounter
	#proxyCounter+=1
	try:
		browser.close()
		browser.quit()
	except:
		pass
	conn = False
	while 1:
		proxy = pl[-1]
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
		chrome_options.add_argument(f'--proxy-server={proxy}')
		browser = webdriver.Chrome(options=chrome_options)
		#print(str(proxyCounter)+' => ' + '--proxy-server=https://{}'.format(proxy))
		try:
			browser.set_page_load_timeout(220)
			browser.get(url)
		except:
			pass
		try:
			if url.split('/')[-1] in browser.title:
				conn = True
			else:
				del pl[-1]
				print('Remaining number of proxies are: ' + str(len(pl)))
		except:
			pass
		if conn == True:
			break
		else:
			browser.close()
			browser.quit()
			waitLong()
		#if proxyCounter > len(pl)-1:
		#	proxyCounter=0
	return browser
def getProxyRotateBrowser(browser, url):
	global pl
	try:
		browser.close()
		browser.quit()
	except:
		pass
	conn = False
	while 1:
		settings = {
        "httpProxy": pl[-1],
        "sslProxy": pl[-1]
    }
		proxy = Proxy(settings)
		cap = DesiredCapabilities.CHROME.copy()
		cap['platform'] = "WINDOWS"
		cap['version'] = "10"
		proxy.add_to_capabilities(cap)
		browser = ChromeDriver(desired_capabilities=cap, executable_path='D:\Python37-32\chromedriver.exe')
		try:
			browser.set_page_load_timeout(220)
			browser.get(url)
		except:
			pass
		if url.split('/')[-1] in browser.title:
			conn = True
		else:
			del pl[-1]
			print('Remaining number of proxies are: ' + str(len(pl)))
		if conn == True:
			break
		else:
			browser.close()
			browser.quit()
			waitLong()
	return browser
###============================================== wsemi end =====================
def getrdetails(res, link):
	tree = html.fromstring(res.text)
	de = tree.xpath('//table[@class="linkage"]')
	for item in de:
		try:
			ebaylink = item.xpath('//tr[3]/td/a[@class="view_vendor"]/@href')[0]
		except:
			ebaylink = ''
		try:
			vendorname = item.xpath('//tr[3]/td/table/tr[1]/td[1]/strong/text()')[0]
		except:
			vendorname = ''
		try:
			loginreq = item.xpath('//tr[3]/td/table/tr[1]/td[1]/font/text()')[0]
		except:
			loginreq = ''
		try:
			image = item.xpath('//tr[3]/td/table/tr[1]/td[7]/a/img/@src')[0]
		except:
			image = ''
		try:
			price = item.xpath('//tr[3]/td/table/tr[1]/td[6]/text()')[0]
			price  = price.replace('\n', '')
		except:
			price = ''
		try:
			stock = item.xpath('//tr[3]/td/table/tr[1]/td[5]/strong/text()')[0]
		except:
			stock = ''
		try:
			condition = item.xpath('//tr[3]/td/table/tr[1]/td[2]/text()')[-1]
			condition = formatString(condition)
		except:
			condition = ''
		try:
			desc = item.xpath('//tr[3]/td/table/tr[2]/td/text()')[-1]
			desc  = formatString(desc)
		except:
			desc = ''
		mpn = link.split('/')[-1]
		data = [vendorname, '', desc,ebaylink,'',image,link,mpn,'',price,condition, stock, loginreq]
		updateRow('wsemi_40k_selpro', data)
def getbdetails(text, link):
	tree = html.fromstring(text)
	de = tree.xpath('//table[@class="linkage"]')
	for item in de:
		try:
			ebaylink = item.xpath('//tbody/tr[3]/td/a[@class="view_vendor"]/@href')[0]
		except:
			ebaylink = ''
		try:
			vendorname = item.xpath('//tbody/tr[3]/td/table/tbody/tr[1]/td[1]/strong/text()')[0]
		except:
			vendorname = ''
		try:
			loginreq = item.xpath('//tbody/tr[3]/td/table/tbody/tr[1]/td[1]/font/text()')[0]
		except:
			loginreq = ''
		try:
			image = item.xpath('//tbody/tr[3]/td/table/tbody/tr[1]/td[7]/a/img/@src')[0]
		except:
			image = ''
		try:
			price = item.xpath('//tbody/tr[3]/td/table/tbody/tr[1]/td[6]/text()')[0]
			price  = price.replace('\n', '')
		except:
			price = ''
		try:
			stock = item.xpath('//tbody/tr[3]/td/table/tbody/tr[1]/td[5]/strong/text()')[0]
		except:
			stock = ''
		try:
			condition = item.xpath('//tbody/tr[3]/td/table/tbody/tr[1]/td[2]/text()')[-1]
			condition = formatString(condition)
		except:
			condition = ''
		try:
			desc = item.xpath('//tbody/tr[3]/td/table/tbody/tr[2]/td/text()')[-1]
			desc  = formatString(desc)
		except:
			desc = ''
		mpn = link.split('/')[-1]
		data = [vendorname, '', desc,ebaylink,'',image,link,mpn,'',price,condition, stock, loginreq]
		updateRow('wsemi_req_40k_', data)
def initBrowser():
	success = False
	global pl
	global pi
	#while 1:
	pi+=1
	if pi > len(pl) -1:
		pi = 0
	settings = {"httpProxy": pl[pi], "sslProxy": pl[pi] }
	proxy = Proxy(settings)
	cap = DesiredCapabilities.CHROME.copy()
	cap['platform'] = "WINDOWS"
	cap['version'] = "10"
	proxy.add_to_capabilities(cap)
	chrome_options = Options()
	chrome_options.add_argument('--headless') 
	browser = ChromeDriver(options=chrome_options, desired_capabilities=cap, executable_path='D:\Python37-32\chromedriver.exe')
	return browser
def validResponse(text, link):
	matched = False
	try:
		mpn = link.split('/')[-1]
		tree = html.fromstring(text)
		fmpn = tree.xpath('//h1/text()')[0]
		#print('found on site: ' + fmpn)
		if mpn.upper() in fmpn.upper():
			matched = True
	except:
		pass
	return matched
def getResponse(link):
	global session
	success = False
	global pl
	global pi
	while 1:
		try:
			session = requests.Session()
			session.headers['User-Agent'] = str(ua.random)
			proxies = {"https": "https://" + pl[pi], "http": "http://" + pl[pi]}
			session.proxies.update(proxies)
			res = session.get(link, timeout=10)
			if validResponse(res, link):
				success = True
				print('proxy worked: ' + pl[pi])
		except:
			print(str(pi) + ' : proxy failed: ' + pl[pi])
			pi+=1
		if success == True:
			break
		#waitSmall()
		if pi > len(pl) -1:
			pi = 0
	return res
def getProxies3():
	global pl
	pl = []
	plt = getList('proxylist3.txt')
	for item in plt:
		pl.append(item[0].split(' ')[0])
def getProxies():
	global pl
	pl = []
	plt = getList('proxylist2.txt')
	for item in plt:
		pl.append(item[0])
def crawlr():
	global lines
	global pc
	global session
	while 1:
		waitSmall()
		try:
			print(str(pc) + ' : ' + lines[pc][0])
			res = session.get(lines[pc][0], timeout=10)
			if validResponse(res, lines[pc][0]):
				#print('validResponse got')
				row = getrdetails(res, lines[pc][0])
				if row != None:
					updateRow('wsemi_req_40k_', row)
				else:
					updateRow('wsemi_req_40k_',[lines[pc][0]])
			else:
				res = getResponse(lines[pc][0])
				row = getrdetails(res, lines[pc][0])
				if row != None:
					updateRow('wsemi_req_40k_', row)
				else:
					updateRow('wsemi_req_40k_',[lines[pc][0]])
			pc+=1
		except:
			res = getResponse(lines[pc][0])
			row = getrdetails(res, lines[pc][0])
			if row != None:
				updateRow('wsemi_req_40k_', row)
			else:
				updateRow('wsemi_req_40k_',[lines[pc][0]])
			pc+=1
		if pc > len(lines)-1:
			break
def getResponse2(link):
	global session
	success = False
	global collector
	while 1:
		proxy = collector.get_proxy({'code': ('ca', 'nz', 'au'), 'anonymous': True})
		try:
			session = requests.Session()
			session.headers['User-Agent'] = str(ua.random)
			proxies = {"https": f"https://{proxy.host}:{proxy.port}", "http": f"http://{proxy.host}:{proxy.port}"}
			session.proxies.update(proxies)
			res = session.get(link, timeout=10)
			if validResponse(res, link):
				success = True
				print(proxy)
		except:
			pass
		if success == True:
			break
	return res
def crawlb():
	global lines
	global pc
	global browser
	while 1:
		crawled = False
		waitSmall()
		try:
			browser.get(lines[pc][0])
			waitLong()
			crawled = True
		except:
			pass
		if crawled == True:
			if validResponse(browser.page_source, lines[pc][0]):
				print(str(pc) + ' : ' + lines[pc][0])
				row = getbdetails(browser.page_source, lines[pc][0])
				if row != None:
					updateRow('wsemi_req_40k_selenium', row)
				else:
					updateRow('wsemi_req_40k_selenium',[lines[pc][0]])
				pc+=1
		else:
			browser.close()
			browser.quit()
			browser = initBrowser()
			waitLong()
		if pc > len(lines)-1:
			break
def crawlr2():
	global lines
	global pc
	global session
	while 1:
		crawled = False
		waitSmall()
		try:
			res = session.get(lines[pc][0], timeout=10)
			crawled = True
		except:
			pass
		if crawled == True:
			if validResponse(res, lines[pc][0]):
				print(str(pc) + ' : ' + lines[pc][0])
				row = getrdetails(res, lines[pc][0])
				if row != None:
					updateRow('wsemi_req_40k_', row)
				else:
					updateRow('wsemi_req_40k_',[lines[pc][0]])
				pc+=1
		else:
			print(str(pc) + ' : ' + lines[pc][0])
			res = getResponse2(lines[pc][0])
			row = getrdetails(res, lines[pc][0])
			if row != None:
				updateRow('wsemi_req_40k_', row)
			else:
				updateRow('wsemi_req_40k_',[lines[pc][0]])
			pc+=1
		if pc > len(lines)-1:
			break
getProxies3()
pl = list(set(pl))
pc=40343
#crawlr()

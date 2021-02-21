import csv, re, time, random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
outputCSV = 'Top_750__keywords'
def createCSV():
	global lines
	header = lines[0]
	with open(outputCSV + '.csv', 'a') as f:
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(header)
		f.close()
def getURL(pc):
	global lines
	keyword = lines[pc][1] + ', ' + lines[pc][2] + ', ' + lines[pc][3]
	keyword = keyword.replace(' ', '+')
	url = 'https://www.google.com/search?q=' + keyword + '&rlz=1C1GCEA_enPK794PK794&oq=' + keyword + '&aqs=chrome.0.0.1548j0j8&sourceid=chrome&ie=UTF-8'
	return url
def getURL1(pc):
	global lines
	keyword = lines[pc][1].replace(' ', '+')
	url = 'https://www.google.com/search?q=' + keyword + '&rlz=1C1GCEA_enPK794PK794&oq=' + keyword + '&aqs=chrome.0.0.1548j0j8&sourceid=chrome&ie=UTF-8'
	return url
def waitSmall():
    time.sleep(random.uniform(1.1, 2.0))
def getOCtimings():
	global browser
	data = []
	days = browser.find_element_by_xpath('//table[@class="WgFkxc"]/tbody')
	dt = BeautifulSoup(days.get_attribute('innerHTML'), 'html.parser')
	dy = dt.findAll('tr')
	for row in dy:
		tresult = {}
		tresult['day'] = row.findAll('td')[0].text
		tresult['open'] = ''
		tresult['close'] = ''
		oc = row.findAll('td')[1].text
		try:
			tresult['open'] = oc.split('–')[0]
		except:
			pass
		try:
			tresult['close'] = oc.split('–')[1]
		except:
			pass
		data.append(tresult)
	return data
def getList(filename):
	with open(filename, 'r', errors='ignore') as file:
		reader = csv.reader(file)
		mlinks = list(reader)
		file.close()
	return mlinks
lines = getList('Top 750.csv')
def getHours(hlist):
	pm12 = '0'
	pm1 = '0'
	pm2 = '0'
	pm3 = '0'
	pm4 = '0'
	pm5 = '0'
	pm6 = '0'
	pm7 = '0'
	pm8 = '0'
	pm9 = '0'
	pm10 = '0'
	pm11 = '0'
	am00 = '0'
	am1 = '0'
	am2 = '0'
	am3 = '0'
	am4 = '0'
	am5 = '0'
	am6 = '0'
	am7 = '0'
	am8 = '0'
	am9 = '0'
	am10 = '0'
	am11 = '0'
	for hour in hlist:
		if hour['hour'] == '12 pm':
			pm12 = hour['value']
		if hour['hour'] == '1 pm':
			pm1 = hour['value']
		if hour['hour'] == '2 pm':
			pm2 = hour['value']
		if hour['hour'] == '3 pm':
			pm3 = hour['value']
		if hour['hour'] == '4 pm':
			pm4 = hour['value']
		if hour['hour'] == '5 pm':
			pm5 = hour['value']
		if hour['hour'] == '6 pm':
			pm6 = hour['value']
		if hour['hour'] == '7 pm':
			pm7 = hour['value']
		if hour['hour'] == '8 pm':
			pm8 = hour['value']
		if hour['hour'] == '9 pm':
			pm9 = hour['value']
		if hour['hour'] == '10 pm':
			pm10 = hour['value']
		if hour['hour'] == '11 pm':
			pm11 = hour['value']
		if hour['hour'] == '12 am':
			am00 = hour['value']
		if hour['hour'] == '1 am':
			am1 = hour['value']
		if hour['hour'] == '2 am':
			am2 = hour['value']
		if hour['hour'] == '3 am':
			am3 = hour['value']
		if hour['hour'] == '4 am':
			am4 = hour['value']
		if hour['hour'] == '5 am':
			am5 = hour['value']
		if hour['hour'] == '6 am':
			am6 = hour['value']
		if hour['hour'] == '7 am':
			am7 = hour['value']
		if hour['hour'] == '8 am':
			am8 = hour['value']
		if hour['hour'] == '9 am':
			am9 = hour['value']
		if hour['hour'] == '10 am':
			am10 = hour['value']
		if hour['hour'] == '11 am':
			am11 = hour['value']
	data = [am00, am1, am2, am3, am4, am5, am6, am7, am8, am9, am10, am11, pm12, pm1, pm2, pm3, pm4, pm5, pm6, pm7, pm8, pm9, pm10, pm11]
	return data
def getWeeklyValues(soup):
	mdata = []
	week = {}
	closedayvalues = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
	try:
		weekly = soup.findAll('div', {'class':'yPHXsc'})
	except:
		pass
	try:
		for day in weekly:
			try:
				data = []
				pr1 = day.find_previous_sibling('div')
				pr2 = pr1.parent
				dayname = pr2['aria-label'].split('times on ')[1]
				hours = day.findAll('div', {'class':'lubh-bar'})
				#print ('Collect values for the day: ' + dayname)
				week[dayname]=getDayValues(hours)
			except:
				pass
	except:
		pass
	try:
		mdata.extend(getHours(week['Mondays']))
	except:
		mdata.extend(closedayvalues)
	try:
		mdata.extend(getHours(week['Tuesdays']))
	except:
		mdata.extend(closedayvalues)
	try:
		mdata.extend(getHours(week['Wednesdays']))
	except:
		mdata.extend(closedayvalues)
	try:
		mdata.extend(getHours(week['Thursdays']))
	except:
		mdata.extend(closedayvalues)
	try:
		mdata.extend(getHours(week['Fridays']))
	except:
		mdata.extend(closedayvalues)
	try:
		mdata.extend(getHours(week['Saturdays']))
	except:
		mdata.extend(closedayvalues)
	try:
		mdata.extend(getHours(week['Sundays']))
	except:
		mdata.extend(closedayvalues)
	return mdata
def getDayValues(daysvalue):
	data = []
	for value in daysvalue:
		tresult = {}
		tresult['value'] = re.findall(r'\d+', value['style'])[0]
		tresult['hour'] = value['aria-label'].split(':')[0]
		data.append(tresult)
	return data
def getweeklytimingSeq(hlist):
	data = []
	mon_op = '0'
	mon_cl = '0'
	tue_op = '0'
	tue_cl = '0'
	wed_op = '0'
	wed_cl = '0'
	thu_op = '0'
	thu_cl = '0'
	fri_op = '0'
	fri_cl = '0'
	sat_op = '0'
	sat_cl = '0'
	sun_op = '0'
	sun_cl = '0'
	for day in hlist:
		if day['open'] == 'Closed':
			day['open'] = '0'
			day['close'] = '0'
		if day['day'] == 'Monday':
			mon_op = day['open']
			mon_cl = day['close']
		if day['day'] == 'Tuesday':
			tue_op = day['open']
			tue_cl = day['close']
		if day['day'] == 'Wednesday':
			wed_op = day['open']
			wed_cl = day['close']
		if day['day'] == 'Thursday':
			thu_op = day['open']
			thu_cl = day['close']
		if day['day'] == 'Friday':
			fri_op = day['open']
			fri_cl = day['close']
		if day['day'] == 'Saturday':
			sat_op = day['open']
			sat_cl = day['close']
		if day['day'] == 'Sunday':
			sun_op = day['open']
			sun_cl = day['close']
	try:
		data.append(mon_op)
		data.append(mon_cl)
	except:
		data.append('0')
		data.append('0')
	try:
		data.append(tue_op)
		data.append(tue_cl)
	except:
		data.append('0')
		data.append('0')
	try:
		data.append(wed_op)
		data.append(wed_cl)
	except:
		data.append('0')
		data.append('0')
	try:
		data.append(thu_op)
		data.append(thu_cl)
	except:
		data.append('0')
		data.append('0')
	try:
		data.append(fri_op)
		data.append(fri_cl)
	except:
		data.append('0')
		data.append('0')
	try:
		data.append(sat_op)
		data.append(sat_cl)
	except:
		data.append('0')
		data.append('0')
	try:
		data.append(sun_op)
		data.append(sun_cl)
	except:
		data.append('0')
		data.append('0')
	return data
def collectDetails(pc):
	global browser
	global lines
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	op_cl_timings = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0']
	waitSmall()
	row = []
	try:
		rating = browser.find_element_by_xpath('//span[@class="rtng"]').text
	except:
		rating = '0'
	try:
		reviews = browser.find_element_by_xpath('//a[@data-async-trigger="reviewDialog"]').text
		reviews = re.findall(r'\d+', reviews)[0]
	except:
		reviews = '0'
	print ('Collecting Open and close timings...')
	try:
		op_cl_timings = getweeklytimingSeq(getOCtimings())
	except:
		pass
	print ('Collecting weekly char values')
	try:
		weeklychartvalues = getWeeklyValues(soup)
	except:
		pass
	row.append(lines[pc][0])
	row.append(lines[pc][1])
	row.append(lines[pc][2])
	row.append(lines[pc][3])
	row.append(rating)
	row.append(reviews)
	row.extend(weeklychartvalues)
	row.extend(op_cl_timings)
	#print (str(len(row)) + ' in row[]')
	with open(outputCSV + '.csv', 'a', encoding='utf-8') as f:
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(row)
		f.close()
def scrape(pc):
	global browser
	while 1:
		browser.get(getURL(pc))
		waitSmall()
		try:
			timings = browser.find_element_by_xpath('//span[@class="BTP3Ac"]')
			actions = ActionChains(browser)
			actions.move_to_element(timings).click().perform()
		except:
			pass
		collectDetails(pc)
		pc+=1
		if pc > len(lines):
			break
pc=1
createCSV()
scrape(pc)

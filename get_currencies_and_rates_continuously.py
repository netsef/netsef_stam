import urllib.request, urllib.parse
import time, datetime, shutil, sys, os

APP_ID = ""
USAGE = "Usage: "+os.path.basename(sys.argv[0])+" <app_id> [output directory]"
RATES_URL = "http://openexchangerates.org/api/latest.json?app_id="
CURRENCIES_URL = "http://openexchangerates.org/api/currencies.json?app_id="

def getExchangeRates(dir):
    rates = urllib.request.urlopen(RATES_URL+APP_ID).read()
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
    filename = dir+"rates-"+timestamp+".txt"
    f_rates = open(filename, 'w')
    f_rates.write(rates.decode('ascii','ignore'))
    f_rates.close()
    shutil.copy(filename, dir+"rates_last.txt")

def getCurrencies(dir):
    currencies = urllib.request.urlopen(CURRENCIES_URL+APP_ID).read()
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
    filename = dir+"currencies-"+timestamp+".txt"
    f_currencies = open(filename, 'w')
    f_currencies.write(currencies.decode('ascii','ignore'))
    f_currencies.close()
    shutil.copy(filename, dir+"currencies-last.txt")

dir = ""
app_id = ""

if len(sys.argv) < 2 or len(sys.argv) > 3:
	print(USAGE)
	sys.exit(0)
APP_ID = sys.argv[1]

if len(sys.argv) > 2:
    dir = sys.argv[2]

while (True):
    for i in range(24):
        if i == 0:
            getCurrencies(dir)
        getExchangeRates(dir)
        time.sleep(3600)
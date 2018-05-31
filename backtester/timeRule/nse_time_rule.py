from backtester.timeRule.custom_time_rule import CustomTimeRule
from datetime import datetime, timedelta
import os
import os.path
import csv
from bs4 import BeautifulSoup
try:
    from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen  # Python 2


class NSETimeRule(TimeRule):
    def __init__(self, startDate, endDate, frequency='H', sample='1'):
        CustomTimeRule.__init__(startDate = startDate, endDate = endDate, holidays = getNSEHolidays(), frequency = frequency, sample = sample)

    def getNSEHolidays():
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.8',
               'Host': 'nseindia.com',
               'Connection': 'keep-alive',
               'Referer': 'https://www.nseindia.com/products/content/equities/equities/mrkt_timing_holidays.htm',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'X-Requested-With': 'XMLHttpRequest'}
        req = Request(url, headers=hdr)
        try:
            page = urlopen(req)
            content = page.read().decode('utf8')
            BeautifulSoup(context, 'lxml')
            holiday_dates = soup.find(id="tab20Content").find_all(style="text-align:right")
            holidays = []
            for date in holiday_dates:
                holidays.append(datetime.strptime(var.get_text(), '%d-%b-%Y')
            return holidays
        except urllib2.HTTPError as e:
            print(e.fp.read())
            return None
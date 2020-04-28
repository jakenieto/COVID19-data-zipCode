import requests
import csv
from contextlib import closing
import argparse
from datetime import date, timedelta
from helper import derivative, plotData

CONFIRMED_COL = 7
DEATHS_COL = 8
COUNTY_COL = 1
STATE_COL= 2

def getDates(days):
    day = date.today().day
    dates = []
    temp = date.today() - timedelta (days=days)
    while date.today() != temp:
        dates.append(temp.strftime("%m-%d-%Y"))
        temp += timedelta(days=1)
              
    return dates


def getData(zip,days):
    url = "https://raw.githubusercontent.com/bgruber/zip2fips/master/zip2fips.json"
    fips = requests.get(url).json()[zip]
    dates = getDates(days)
    data = []
    first = True
    for d in dates :
        url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + d + ".csv"
        with closing(requests.get(url,stream=True)) as r:
            f = (line.decode('utf-8') for line in r.iter_lines())
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in reader:
                if len(row) == 0:
                    break
                if row[0] == '404: Not Found':
                    break
                if first:
                    data.append(row)
                    first = False
                if row[0] == fips:
                    data.append(row)
    return data

def main(zip,days):
    data = getData(zip,days)
    county = ""
    state = ""

    if len(data) > 1:
        county = data[1][COUNTY_COL]
        state = data[1][STATE_COL]
    
    confirm_data = [int(con[CONFIRMED_COL]) for con in data[1:]]
    CONFIRM_dict = {
                "days": len(confirm_data),
                "data": confirm_data,
                "title": 'Confirmed cases in ' + str(county) + " County, " + str(state),
                "xlabel": 'Last ' + str(len(confirm_data)) + " days",
                "ylabel": 'Number of Confirmed cases'
                
        }
    plotData(CONFIRM_dict)
    DERIV_dict = {
                "days": len(confirm_data),
                "data": derivative([i for i in range(0,len(confirm_data))],confirm_data,0,0),
                "title": 'Derivative of Confirmed cases in ' + str(county) + " County, " + str(state),
                "xlabel": 'Last ' + str(len(confirm_data)) + " days",
                "ylabel": 'Number of New Confirmed cases/Day'
                
        }
    plotData(DERIV_dict)

if __name__ == "__main__":

   
    parser = argparse.ArgumentParser(description='COVID-19 Graphs')
    parser.add_argument("-zip","--zip", required=True, help="US Zip code")
    parser.add_argument("-days","--days", default=30, help="How many days in the past")
    args = parser.parse_args()
    main(args.zip,int(args.days))
from datetime import date, timedelta
import pandas as pd
import calendar


# input your starting quarter
FromYearQuarter = '2021-Q1'



def week1_start_ordinal(year):
    jan1 = date(year, 1, 1)
    jan1_ordinal = jan1.toordinal()
    jan1_weekday = jan1.weekday()
    week1_start_ordinal = jan1_ordinal - ((jan1_weekday + 1) % 7)
    return week1_start_ordinal

def week_from_date(date_object):
    date_ordinal = date_object.toordinal()
    year = date_object.year
    week = ((date_ordinal - week1_start_ordinal(year)) // 7) + 1
    return f"{year}-W{week}"

def eomonth(date_object):
    year = date_object.year
    month = date_object.month
    days_in_month = calendar.monthrange(year, month)[1]
    eomonth = date(year, month, days_in_month)
    return eomonth

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)



YearStart = FromYearQuarter[:4]
QuarterStart = FromYearQuarter[-1:]
DateStart = date(int(YearStart), int(QuarterStart)*3-2, 1)
DateEnd = date(date.today().year, date.today().month, eomonth(date.today()).day)
Output = []
OutputWeek = ''
OutputMonth = ''

for dt in daterange(DateStart, DateEnd):

    if OutputWeek != week_from_date(dt) or OutputMonth != f"{dt.year}-{('0' if dt.month < 10 else '')}{dt.month}":
        
        OutputWeek = week_from_date(dt)
        OutputMonth = f"{dt.year}-{('0' if dt.month < 10 else '')}{dt.month}"
        OutputQuarter = f"{dt.year}-Q{dt.month//4+1}"
        Output.append([OutputQuarter, OutputMonth, OutputWeek])
    

OutputDF = pd.DataFrame(Output, columns = ['Quarter', 'Month', 'Week'])

print(OutputDF)

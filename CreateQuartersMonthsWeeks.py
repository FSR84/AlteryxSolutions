from datetime import date, timedelta
import pandas as pd
import math


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
    week = ((date_ordinal - week1_start_ordinal(year)) // 7) # add +1 if you want your list to start with W01 instead of W00 for each year
    return f"{year}-W{('0' if week < 10 else '')}{week}"

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)



YearStart = FromYearQuarter[:4]
QuarterStart = FromYearQuarter[-1:]
DateStart = date(int(YearStart), int(QuarterStart)*3-2, 1)
DateEnd = date.today()
Output = []
OutputWeek = ''
OutputMonth = ''


for dt in daterange(DateStart, DateEnd):

    if OutputWeek != week_from_date(dt) or OutputMonth != f"{dt.year}-{('0' if dt.month < 10 else '')}{dt.month}":
        
        OutputWeek = week_from_date(dt)
        OutputMonth = f"{dt.year}-{('0' if dt.month < 10 else '')}{dt.month}"
        OutputQuarter = f"{dt.year}-Q{math.ceil(dt.month/3)}"
        Output.append([OutputQuarter, OutputMonth, OutputWeek])
    


OutputDF = pd.DataFrame(Output, columns = ['Quarter', 'Month', 'Week'])

print(OutputDF)

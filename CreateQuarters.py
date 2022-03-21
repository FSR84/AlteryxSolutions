from datetime import date
import math
import pandas as pd

# input your starting quarter
FromYearQuarter = '2021-Q1'


YearStart = FromYearQuarter[:4]
QuarterStart = FromYearQuarter[-1:]
YearEnd = date.today().year
QuarterEnd = math.ceil(date.today().month/3)


OutputTable = []

i=0
j=int(QuarterStart)

while int(str(int(YearStart)+i)+str(j)) <= int(str(YearEnd)+str(QuarterEnd)):

    OutputQuarter = str(int(YearStart)+i)+'-Q'+str(j)
    OutputTable.append([OutputQuarter])

    if j == 4:
        j=1
        i+=1
    else:
        j+=1


OutputDF = pd.DataFrame(OutputTable, columns = ['Quarter'])

print(OutputDF)

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os

# <codecell>

os.getcwd()

# <codecell>

files = !ls 201312/Partes/*.csv

# <codecell>

files

# <codecell>

files[0][20:26]

# <codecell>

def getAcronym(filename):
    return filename[20:26]

# <codecell>

getAcronym(files[0])

# <codecell>

import pandas as pd
import string
from datetime import datetime
import tkSimpleDialog

# <codecell>



# <codecell>

def removeDummyProyects(report):
    return report[report.Project.str.contains('^X')==False]

# <codecell>

def getReport(fileName):
    report = pd.read_csv(fileName, sep=';', names=['Date','Hours','Project','Phase','SubPhase','Task','OnCall','CallIn'])
    report['Acronym']=getAcronym(fileName)
    report['Hours'] = report['Hours'].apply(lambda x: float(string.replace(x,',','.')))
    report['Date'] = [datetime.strptime(x, '%d/%m/%Y') for x in report['Date']]
    report['Period'] = [str(_date.month)+'/'+str(_date.year) for _date in report['Date']]
    return removeDummyProyects(report)

# <codecell>

report=getReport(files[0])
tot = report.groupby(['Acronym','Project','Period']).sum()
tot.index[0][0]

# <codecell>

for _file in files:
    totReport = getReport(_file).groupby(['Acronym','Project','Period']).sum()
    factura=float(tkSimpleDialog.askstring('Factura', "Importe factura de "+str(totReport.index[0][0])))
    print totReport.apply(lambda x: factura*x/sum(x))

# <codecell>



#!/usr/bin/env python2 
#
#	mileage.py
#	IdlePhysicist, 2018
#

import sqlite3 as lite
from matplotlib.pyplot import *

# Connecting to the SQLite db
try:
    conn = lite.connect('mileage.db')
    conn.row_factory = lite.Row
    cur   = conn.cursor()
    query = """SELECT * FROM audi"""
    cur.execute(query)
except:
    print "Error connecting to database"

# Creating a data dictionary
data = dict()
for row in cur:
    #data[str(row['id'])] = row['id'],row['date'],row['mileage'],row['fuel'],row['price']
    #data[row['id']] = { 'date': row['date'],row['mileage'],row['fuel'],row['price'] }
    data.update({ row['id']: { 'date': row['date'], 'mileage': row['mileage'], 'fuel': row['fuel'], 'price': row['price'] }})

#print data

dates = [ data[key]['date'] for key in data ]

def avgMileage(data):
    from numpy import mean
    global gallonsUsed, milesDriven
    oddometerReading, gallonsUsed = [], []
    for key in data: oddometerReading.append(data[key]['mileage']), gallonsUsed.append(data[key]['fuel'])
    #for key in data: gallonsUsed.append(data[key]['fuel'])
    if len(oddometerReading) is len(gallonsUsed):
        milesDriven, avg_mileage = [], []
        for i in xrange(len(oddometerReading)-1):
            milesDriven.append(oddometerReading[i+1]-oddometerReading[i])
        for j in xrange(len(milesDriven)):
            avg_mileage.append(milesDriven[j]/gallonsUsed[j])
    
    return avg_mileage, mean(avg_mileage)

averageMilagePerTank, averageMileage = avgMileage(data)

print 'Total average fuel consumption: {0}\n'.format(averageMileage)
#print len(milesDriven), len(gallonsUsed)

for x in milesDriven:
    print ''


# Line fitting-ish
from numpy import linspace
x = linspace(0,1.2*max(milesDriven))
def linear(x, m): return x*(m)

# Plotting
rc('font', family='sans')
rc('xtick', labelsize='small')
rc('ytick', labelsize='small')

plot(x, linear(x,averageMileage), linestyle=':', color='Grey', label='MPG')
#scatter(milesDriven, gallonsUsed[0:len(milesDriven)], marker='^', color='red', label='MPG/tank')
for x,y,z in zip( gallonsUsed[0:len(milesDriven)], milesDriven, dates[0:len(milesDriven)] ):
    scatter(x, y, marker='.', color='red')
    annotate( xy=[ x+0.15 ,y ], s=z )

title('Miles Per Gallon')
ylim(0,1.1*max(milesDriven))
xlim(0,16) # It's a 15.8 gallon tank so a fill up will not be anymore than 15.
xlabel("Distance Driven (Miles)")
ylabel("Fuel Consumed (US Gallons)")
#xscale('log')
legend(loc='upper left')
savefig("output.png")
show()

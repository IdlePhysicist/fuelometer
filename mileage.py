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
for row in cur: data.update({ row['id']: { 'date': row['date'], 'mileage': row['mileage'], 'fuel': row['fuel'], 'price': row['price'] }})

dates = [ data[key]['date'] for key in data ]

def avgMileage(data):
    from numpy import mean
    global gallonsUsed, milesDriven
    milesDriven, avg_mileage, gallonsUsed = [], [], []
    for key in data: milesDriven.append(data[key]['mileage']), gallonsUsed.append(data[key]['fuel'])
    for j in xrange(len(milesDriven)):
        avg_mileage.append(milesDriven[j]/gallonsUsed[j])
    return avg_mileage, mean(avg_mileage)

averageMilagePerTank, averageMileage = avgMileage(data)

print 'Total average fuel consumption: {0}\n'.format(averageMileage)

# Line fitting-ish
#   This generates a line of the average gallons per mile.
from numpy import linspace
x = linspace(0,1.2*max(milesDriven))
def linear(x, m): return x*(1/m)

# Plotting
#
figure('Fuelometer')
rc('font', family='sans')
rc('xtick', labelsize='small')
rc('ytick', labelsize='small')

plot(x, linear(x, averageMileage), linestyle=':', color='Grey', label='GPM')

for x,y,z in zip( milesDriven, gallonsUsed[0:len(milesDriven)], dates[0:len(milesDriven)] ):
    # NB: This plots gallons per mile!
    scatter(x, y, marker='.', color='red')
    annotate( xy=[ x+0.15 ,y ], s=z )

title('Miles Per Gallon: {:4.2f}'.format(averageMileage))
xlim(150,1.1*max(milesDriven))
ylim(0,16) # It's a 15.8 gallon tank so a fill up will not be anymore than 15.
xlabel("Distance Driven (Miles)")
ylabel("Fuel Consumed (US Gallons)")
#xscale('log')
legend(loc='upper left')
savefig("output.png")#,bbox_inches='tight')
show()

#!/usr/bin/env python2
#
#	mileage.py
#	IdlePhysicist, 2018
#

import sqlite3 as lite
from matplotlib.pyplot import *
from numpy import linspace, mean


class App:
    def db_connection(self):
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
        return data

    def avgMileage(self):
        global gallonsUsed, milesDriven
        self.milesDriven, avg_mileage, gallonsUsed = [], [], []
        for key in self.data: self.milesDriven.append(data[key]['mileage']), self.gallonsUsed.append(data[key]['fuel'])
        for j in xrange(len(self.milesDriven)):
            avg_mileage.append(self.milesDriven[j]/gallonsUsed[j])
        print 'Total average fuel consumption: {0}\n'.format( mean(avg_mileage) )
        return avg_mileage, mean(avg_mileage)

    def __init__(self):
        self.data = db_connection()
        self.dates = [ data[key]['date'] for key in data ]
        self.averageMilagePerTank, self.averageMileage = avgMileage(data)
        x = linspace(0,1.2*max(self.milesDriven))
        return plotting

    # Line fitting-ish
    #   This generates a line of the average gallons per mile.
    def linear(self, m): return x*(1/m)

    def plotting(self):
        # Plotting
        #
        figure('Fuelometer')
        rc('font', family='sans')
        rc('xtick', labelsize='small')
        rc('ytick', labelsize='small')

        plot(self.x, linear(self.x, self.averageMileage), linestyle=':', color='Grey', label='GPM')

        for x,y,z in zip( self.milesDriven, self.gallonsUsed[0:len(milesDriven)], self.dates[0:len(milesDriven)] ):
            # NB: This plots gallons per mile!
            scatter(x, y, marker='.', color='red')
            annotate( xy=[ x+0.15 ,y ], s=z )

        title('Miles Per Gallon: {:4.2f}'.format(self.averageMileage))
        xlim(150,1.1*max(self.milesDriven))
        ylim(0,16) # It's a 15.8 gallon tank so a fill up will not be anymore than 15.
        xlabel("Distance Driven (Miles)")
        ylabel("Fuel Consumed (US Gallons)")
        #xscale('log')
        legend(loc='upper left')
        savefig("output.png")#,bbox_inches='tight')
        show()

App.__init__()

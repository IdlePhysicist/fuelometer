#!/usr/bin/env python2
#
#   mileage.py
#   IdlePhysicist, 2018
#

import sqlite3 as lite
from matplotlib.pyplot import *
from numpy import linspace, mean

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from mainWindow import Ui_Fuelometer

#class Communicate(QObject):
#    mpgEmit = pyqtSignal(float)

class MileageWorker(QRunnable):
#    signals = Communicate()

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
        for row in cur: data.update({ row['id']: { 'date': row['date'], 'mileage': row['mileage'], 'fuel': row['fuel'],'price': row['price'] }})
        return data

    #@pyqtSlot()
    def avgMileage(self):
        global gallonsUsed, milesDriven
        self.milesDriven, avg_mileage, self.gallonsUsed = [], [], []
        for key in self.data: self.milesDriven.append( self.data[key]['mileage'] ), self.gallonsUsed.append( self.data[key]['fuel'] )
        for j in xrange(len(self.milesDriven)):
            avg_mileage.append(self.milesDriven[j]/self.gallonsUsed[j])
        #print 'Total average fuel consumption: {0}\n'.format( mean(avg_mileage) )
        return avg_mileage, mean(avg_mileage)

    def __init__(self):
        super(MileageWorker, self).__init__()
        self.data = self.db_connection()
        self.dates = [ self.data[key]['date'] for key in self.data ]
        self.averageMilagePerTank, self.averageMileage = self.avgMileage()
        self.x = linspace(0, 1.2*max(self.milesDriven))
        #self.signals.mpgEmit.emit(self.averageMileage)
        #self.plotting()

    def avgMileageReturner(self): return float(self.averageMileage)

    # Line fitting-ish
    #   This generates a line of the average gallons per mile.
    def linear(self): return self.x * (1/self.averageMileage)

    def plotting(self):
        # Plotting
        #
        figure('Fuelometer')
        rc('font', family='sans')
        rc('xtick', labelsize='small')
        rc('ytick', labelsize='small')

        plot(self.x, self.linear(), linestyle=':', color='Grey', label='GPM')

        for x,y,z in zip( self.milesDriven, self.gallonsUsed[0:len(self.milesDriven)], self.dates[0:len(self.milesDriven)] ):
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

class mainWindow(QMainWindow, Ui_Fuelometer):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        #MileageWorker().__init__()
        self.worker = MileageWorker()
        self.mpgLabel( self.worker.avgMileageReturner() )
        self.plotButton.clicked.connect( self.plot )

    def plot(self):
        #self.plotButton.setText( ':4.2f' )
        self.worker.plotting()

    def mpgLabel(self, mpg):
        self.label_AM_Value.setText( '{:4.2f}'.format( mpg ) )


if __name__ == '__main__':
    app = QApplication([])
    Fuelometer = mainWindow()
    ui = Ui_Fuelometer()
    #ui.setupUi(Fuelometer) # This line is the root of all evil
    Fuelometer.show()
    app.exec_()

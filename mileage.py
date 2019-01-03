#!/usr/bin/env python2
#
#   mileage.py
#   IdlePhysicist, 2018
#

import sqlite3 as lite
from matplotlib.pyplot import *
from numpy import linspace, mean
from yaml import load

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

from mainWindow import Ui_Fuelometer
from viewDBWindow import Ui_databaseViewer

class dbViewWindow(QMainWindow, Ui_databaseViewer):
    def __init__(self):
        super(dbViewWindow, self).__init__()
        self.setupUi(self)

    def loadData(self):
        # where c is the cursor
        self.c.execute('''SELECT * FROM {0} '''.format(config['TableName'].lower()))
        rows = self.c.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.tableWidget_2.insertRow(inx)
            # add more if there is more columns in the database.
            self.tableWidget_2.setItem(inx, 0, QTableWidgetItem(row[1]))
            self.tableWidget_2.setItem(inx, 1, QTableWidgetItem(row[2]))
            self.tableWidget_2.setItem(inx, 2, QTableWidgetItem(row[3]))

class MileageWorker(QRunnable):
    def db_connection(self):
        # Connecting to the SQLite db
        #
        try:
            self.conn = lite.connect('mileage.db')
            self.conn.row_factory = lite.Row
            cur   = self.conn.cursor()
        except:
            print "Error connecting to database"

        return cur

    def db_fetchrows(self):
        # Fetch data from the table
        #
        try:
            query = "SELECT * FROM {0}".format(config['TableName'].lower())
            self.cur.execute(query)
        except:
            print "Error fetching database rows"

        # Creating a data dictionary
        data = dict()
        for row in self.cur: data.update({ row['id']: { 'date': row['date'], 'mileage': row['mileage'], 'fuel': row['fuel'], 'price': row['price'] }})
        return data

    def db_insertrows(self, query_arg):
        # Insert data into the table
        #
        try:
            query = 'INSERT INTO {0} (date, mileage, fuel, price) VALUES ({1})'.format(config['TableName'].lower(), query_arg)
            self.cur.execute(query)
            self.conn.commit()
        except:
            print "Error inserting into database"

    def avgMileage(self):
        global gallonsUsed, milesDriven
        self.milesDriven, avg_mileage, self.gallonsUsed, oddometerReading = [], [], [], []
        #for key in self.data: self.milesDriven.append( self.data[key]['mileage'] ), self.gallonsUsed.append( self.data[key]['fuel'] )
        #for j in xrange(len(self.milesDriven)):
        #    avg_mileage.append(self.milesDriven[j]/self.gallonsUsed[j])
        for key in self.data: oddometerReading.append( self.data[key]['mileage'] ), self.gallonsUsed.append( self.data[key]['fuel'] )
        if len(oddometerReading) is len(self.gallonsUsed):
            for i in xrange(len(oddometerReading)-1):
                self.milesDriven.append(oddometerReading[i+1]-oddometerReading[i])
            for j in xrange(len(self.milesDriven)):
                avg_mileage.append(self.milesDriven[j]/self.gallonsUsed[j])
        return avg_mileage, mean(avg_mileage)

    def __init__(self):
        super(MileageWorker, self).__init__()
        self.cur = self.db_connection()
        self.data = self.db_fetchrows() # TODO
        self.dates = [ self.data[key]['date'] for key in self.data ]
        self.averageMilagePerTank, self.averageMileage = self.avgMileage()
        self.x = linspace(0, 1.2*max(self.milesDriven))

    def avgMileageReturner(self): return float(self.averageMileage)

    def linear(self):
        # Line fitting-ish
        #   This generates a line of the average gallons per mile.
        return self.x * (1/self.averageMileage)

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
        xlim(0.9*min(self.milesDriven),1.1*max(self.milesDriven))
        ylim(round(0.8*min(self.gallonsUsed)),round(1.15*max(self.gallonsUsed))) # It's a 15.8 gallon tank so a fill up will not be anymore than 15.
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
        global config
        config = load(open('config.yml'))
        self.setWindowTitle( " - ".join(['Fuelometer', config['TableName'] ]))
        self.worker = MileageWorker()
        self.mpgLabel( self.worker.avgMileageReturner() )
        self.plotButton.clicked.connect( self.plot )
        self.insertButton.clicked.connect( self.insertIntoDB )
        self.vDBButton.clicked.connect( self.callViewDB )

    def plot(self):
        if len(self.worker.gallonsUsed) < 3:
            QMessageBox.about(self, "Warning", "The plot function cannot be run until\nthere are at least 3 database enteries.\nSorry.")
        else:
            self.worker.plotting()

    def mpgLabel(self, mpg): self.label_AM_Value.setText( '{:4.2f} MPG'.format( mpg ) )

    def insertIntoDB(self):
        query_arg = ",".join([
            str( self.dateEdit.date().toPyDate() ),
            str( self.mileageEdit.text()         ),
            str( self.fuelEdit.text()            ),
            str( self.priceEdit.text()           )
            ])
        #print query_arg
        self.worker.db_insertrows( query_arg )
        self.mileageEdit.clear()
        self.fuelEdit.clear()
        self.priceEdit.clear()

    def callViewDB(self):
        self.dbWindow = dbViewWindow()
        self.dbWindow.show()

if __name__ == '__main__':
    app = QApplication([])
    Fuelometer = mainWindow()
    ui = Ui_Fuelometer()
    #ui.setupUi(Fuelometer) # This line is the root of all evil
    Fuelometer.show()
    app.exec_()

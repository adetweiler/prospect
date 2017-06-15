import csv
import matplotlib.pyplot as plt

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []
x6 = []
y6 = []
x7 = []
y7 = []

with open('spreadsheetThree - MURE-10^7s.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x1.append((row[0]))
		y1.append((row[1]))

with open('spreadsheetThree - MURE-36hrs.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x2.append((row[0]))
                y2.append((row[1]))

with open('spreadsheetThree - MURE-12hrs.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x3.append((row[0]))
                y3.append((row[1]))

with open('spreadsheetThree - MURE-10^4s.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x4.append((row[0]))
                y4.append((row[1]))

with open('spreadsheetThree - [53]-10^4s.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x5.append((row[0]))
                y5.append((row[1]))

with open('spreadsheetThree - [53]-36hrs.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x6.append((row[0]))
                y6.append((row[1]))

with open('spreadsheetThree - [53]-10^7s.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x7.append((row[0]))
                y7.append((row[1]))

fig = plt.figure()
abc = fig.add_subplot(111)

abc.plot(x1,y1,color='black',label='MURE - 10^4 s')
abc.plot(x2,y2,'k--',label='MURE - 12 h')
abc.plot(x3,y3,'k-.',label='MURE - 36 h')
abc.plot(x4,y4,'k:',label='MURE - 10^7 s')
abc.plot(x5,y5,'k',marker='*',linestyle='None',label='[53] - 10^4 s')
abc.plot(x6,y6,'k',marker='+',linestyle='None',label='[53] - 36 h')
abc.plot(x7,y7,color='black',marker='x',linestyle='None',label='[53] - 10^7 s')

plt.legend(loc = 4)

plt.xlabel('neutrino kinetic energy (MeV)')
plt.ylabel('correlation to infinite irradiation time (%)')
plt.title('235 U spectrum for diff. irradiation times')
plt.show()

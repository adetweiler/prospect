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

with open('oneMin.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x1.append((row[0]))
		y1.append((row[1]))

with open('oneHour.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x2.append((row[0]))
                y2.append((row[1]))

with open('oneDay.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x3.append((row[0]))
                y3.append((row[1]))

with open('thirtyDays.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x4.append((row[0]))
                y4.append((row[1]))

with open('oneYear.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x5.append((row[0]))
                y5.append((row[1]))

with open('tenYears.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x6.append((row[0]))
                y6.append((row[1]))

with open('oneHundredYears.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x7.append((row[0]))
                y7.append((row[1]))

plt.plot(x1,y1,'r',label='1 min')
plt.plot(x2,y2,color='orange',linestyle='dashed',label='1 hr')
plt.plot(x3,y3,color='yellow',linestyle='dashed',label='1 day')
plt.plot(x4,y4,color='green',linestyle='dashed',label='30 days')
plt.plot(x5,y5,color='green',label='1 yr')
plt.plot(x6,y6,color='blue',linestyle='dashed',label='10 yrs')
plt.plot(x7,y7,color='purple',linestyle='dashed',label='100 yrs')
plt.yscale('log')
plt.xlabel('Neutrino Energy [MeV]')
plt.ylabel('Neutrino Flux [s^-1 MeV^-1 ton^-1]')
plt.title('SNF antineutrinos vs time after discharge from reactor')
plt.legend()
plt.show()

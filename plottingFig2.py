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
x8 = []
y8 = []
x9 = []
y9 = []
x10 = []
y10 = []
x11 = []
y11 = []
x12 = []
y12 = []

with open('spreadsheetTwo - Day 0.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x1.append((row[0]))
		y1.append((row[1]))

with open('spreadsheetTwo - Day 1.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x2.append((row[0]))
                y2.append((row[1]))

with open('spreadsheetTwo - Day 2.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x3.append((row[0]))
                y3.append((row[1]))

with open('spreadsheetTwo - Day 3.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x4.append((row[0]))
                y4.append((row[1]))

with open('spreadsheetTwo - Day 4.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x5.append((row[0]))
                y5.append((row[1]))

with open('spreadsheetTwo - Day 5.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x6.append((row[0]))
                y6.append((row[1]))

with open('spreadsheetTwo - Day 10.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x7.append((row[0]))
                y7.append((row[1]))

with open('spreadsheetTwo - Day 15.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x8.append((row[0]))
                y8.append((row[1]))

with open('spreadsheetTwo - Day 20.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x9.append((row[0]))
                y9.append((row[1]))

with open('spreadsheetTwo - Day 25.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x10.append((row[0]))
                y10.append((row[1]))

with open('spreadsheetTwo - Day 30.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x11.append((row[0]))
                y11.append((row[1]))

with open('spreadsheetTwo - Day 365.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
                x12.append((row[0]))
                y12.append((row[1]))


plt.plot(x1,y1,color='black',marker='o',label='0th day')
plt.plot(x2,y2,color='orange',marker='o',label='1st day')
plt.plot(x3,y3,color='purple',marker='v',label='2nd day')
plt.plot(x4,y4,color='blue',marker='v',label='3rd day')
plt.plot(x5,y5,color='black',marker='D',label='4th day')
plt.plot(x6,y6,color='orange',marker='D',label='5th day')
plt.plot(x7,y7,color='purple',marker='^',label='10th day')
plt.plot(x8,y8,color='blue',marker='^',label='15th day')
plt.plot(x9,y9,color='black',marker='<',label='20th day')
plt.plot(x10,y10,color='orange',marker='<',label='25th day')
plt.plot(x11,y11,color='purple',marker='>',label='30th day')
plt.plot(x12,y12,color='blue',marker='>',label='365th day')
plt.xlabel('E/MeV')
plt.ylabel('ratio (SNF/total)')
plt.title('ratio (SNF/total) vs total spectrum at end of cycle')
plt.legend()
plt.show()

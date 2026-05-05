import Main
import pandas as ps
import numpy as np
from word2number import w2n
from matplotlib import pyplot as plt

filepath = r".\DataRepository\imports-85.data"

parser = Main.parser

allData = parser.parse(filepath)

##TODO
#Possible engine properties:
#   bore(19), stroke(20), compression ratio (21), horsepower (22), 
#   peak rpm (23), city mpg (24), highway mpg (25)
#   num of cylinders (16), engine size (17), fuel system (18)


citympg = allData["city-mpg"]
highwaympg = allData["highway-mpg"]


bore = parser.refineData(allData,"bore",float)
stroke = parser.refineData(allData,"stroke",float)
compRatio = parser.refineData(allData,"compression-ratio",float)
numCylinders = parser.refineData(allData,"num-of-cylinders",str)
horsepower = parser.refineData(allData,"horsepower",float)
engineSize = parser.refineData(allData,"engine-size",float)
fuelSystem = parser.refineData(allData,"fuel-system",str)
peakRPM = parser.refineData(allData,"peak-rpm",float)
engineLoc = parser.refineData(allData,"engine-location",str)
fuelType = parser.refineData(allData,"fuel-type",str)

# sortCylinders = sorted(allData,key=w2n.word_to_num(allData["num-of-cylinders"]))


plt.scatter(horsepower,highwaympg,color='red',label="Highway MPG")
plt.scatter(horsepower,citympg,color='blue',label="City MPG")
plt.xlabel("Horsepower")
plt.ylabel("Miles Per Gallon")
plt.title("Horsepower vs MPG")
plt.legend()
plt.show()

plt.scatter(numCylinders[55],highwaympg[55],color='red')
plt.scatter(numCylinders[18],highwaympg[18],color='red')
plt.scatter(numCylinders[0],highwaympg[0],color='red')
plt.scatter(numCylinders[4],highwaympg[4],color='red')
plt.scatter(numCylinders[2],highwaympg[2],color='red')
plt.scatter(numCylinders[71],highwaympg[71],color='red')
plt.scatter(numCylinders[49],highwaympg[49],color='red')

plt.scatter(numCylinders,highwaympg,color='red',label="Highway MPG")
plt.scatter(numCylinders,citympg,color='blue',label="City MPG")
plt.xlabel("number of cylinders")
plt.ylabel("Miles Per Gallon")
plt.title("Number of Cylinders vs MPG")
plt.legend()
plt.show()

plt.scatter(engineSize,highwaympg,color='red',label="Highway MPG")
plt.scatter(engineSize,citympg,color='blue',label="City MPG")
plt.xlabel("Engine size (cubic inches)")
plt.ylabel("Miles Per Gallon")
plt.title("Engine Size vs MPG")
plt.legend()
plt.show()

plt.scatter(stroke,highwaympg,color='red',label="Highway MPG")
plt.scatter(stroke,citympg,color='blue',label="City MPG")
plt.xlabel("stroke (in)")
plt.ylabel("Miles Per Gallon")
plt.title("Stroke vs MPG")
plt.legend()
plt.show()

plt.scatter(fuelType,highwaympg,color='red',label="Highway MPG")
plt.scatter(fuelType,citympg,color='blue',label="City MPG")
plt.xlabel("Fuel Type")
plt.ylabel("Miles Per Gallon")
plt.title("Fuel Type vs MPG")
plt.legend()
plt.show()

plt.scatter(peakRPM,highwaympg,color='red',label="Highway MPG")
plt.scatter(peakRPM,citympg,color='blue',label="City MPG")
plt.xlabel("peak RPM")
plt.ylabel("Miles Per Gallon")
plt.title("peak RPM vs MPG")
plt.legend()
plt.show()

# plt.scatter(stroke,highwaympg,color='blue',label="stroke")
# plt.scatter(compRatio,highwaympg,color='green',label="compression ratio")

# Useless: Engine Loc


# Higher Horsepower, engine size, and number of cylinders correlate to lower mpg



# plt.legend()





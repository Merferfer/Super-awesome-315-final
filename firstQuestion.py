from cProfile import label

import Main
import pandas as ps
import numpy as np
from matplotlib import pyplot as plt

filepath = ".\DataRepository\imports-85.data"

parser = Main.parser

allData = parser.parse(filepath)

##TODO
#Possible engine properties:
#   bore(19), stroke(20), compression ratio (21), horsepower (22), 
#   peak rpm (23), city mpg (24), highway mpg (25)
#   num of cylinders (16), engine size (17), fuel system (18)


citympg = allData["city-mpg"]
highwaympg = allData["highway-mpg"]

print((allData["num-of-cylinders"][3]))

bore = parser.refineData(allData,"bore",float)
stroke = parser.refineData(allData,"stroke",float)
compRatio = parser.refineData(allData,"compression-ratio",float)
numCylinders = parser.refineData(allData,"num-of-cylinders",str)
horsepower = parser.refineData(allData,"horsepower",float)
engineSize = parser.refineData(allData,"engine-size",float)
fuelSystem = parser.refineData(allData,"fuel-system",str)
peakRPM = parser.refineData(allData,"peak-rpm",float)
engineLoc = parser.refineData(allData,"engine-location",str)


# plt.scatter(bore,highwaympg,color='red',label="bore")
# plt.scatter(stroke,highwaympg,color='blue',label="stroke")
# plt.scatter(compRatio,highwaympg,color='green',label="compression ratio")

plt.scatter(engineLoc,highwaympg)

# Higher Horsepower, engine size, and number of cylinders correlate to lower mpg

plt.legend()
plt.show()


# plt.legend()





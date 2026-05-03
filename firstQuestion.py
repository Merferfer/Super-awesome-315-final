import Main
import pandas as ps
from matplotlib import pyplot as plt

filepath = ".\DataRepository\imports-85.data"

parser = Main.parser

allData = parser.parse(filepath)

##TODO
#Possible engine properties:
#   bore(19), stroke(20), compression ratio (21), horsepower (22), 
#   peak rmp (23), city mpg (24), highway mpg (25)
#   num of cylinders (16), engine size (17), fuel system (18)

#Create a plot of 
plt.hist(allData['21'],label="City MPG?")
plt.hist(allData['27'],label="Highway MPG?")
plt.legend()
plt.show()



print(allData.columns)


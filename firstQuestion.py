import Main
import pandas as ps

filepath = ".\DataRepository\imports-85.data"

parser = Main.parser

allData = parser.parse(filepath)

print(allData)
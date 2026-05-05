import pandas as ps
from pandas import StringDtype
import numpy as np
from numpy import dtype


filepath = ".\DataRepository\imports-85.data"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration",'num-of-doors',
"body-style",
"drive-wheels",
"engine-location",
"wheel-base",
"length",
"width",
"height",
"curb-weight",
"engine-type",
"num-of-cylinders",
"engine-size",
"fuel-system",
"bore",
"stroke",
"compression-ratio",
"horsepower",
"peak-rpm",
"city-mpg",
"highway-mpg",
"price"]

class parser:

  def parse(filepath):

    file = open(filepath)


    dataFrame = ps.read_csv(file,names=headers)

    

    return dataFrame
  
# Takes the column of the dataframe, casts each element to type, 
# and turns the missing data to None 
  def refineData(dataFrame,header: str,typeCast: dtype):

    if(typeCast == str):
      refinedData = np.empty(len(dataFrame[header]),dtype=np.dtypes.StringDType)
    else:
      refinedData = np.empty(len(dataFrame[header]),dtype=typeCast)     


    for a in range(0,len(dataFrame[header])):
      if dataFrame[header][a] == "?":
        refinedData[a] = None
      else:
        refinedData[a] = typeCast(dataFrame[header][a])

    return refinedData
  


if __name__ == "__main__":

  frame = parser.parse(filepath)
  print(frame)



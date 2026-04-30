import pandas as ps


filepath = ".\DataRepository\imports-85.data"

class parser:

  def parse(filepath):
    file = open(filepath)

    dataFrame = ps.read_csv(file)

    return dataFrame


  


if __name__ == "__main__":

  parser.parse(filepath)






import pandas as pd

class usefulFunctions:
    def loadCSV(csv):
        df = pd.read_csv(csv)
        return df
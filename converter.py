import pandas as pd
readfile = pd.read_csv("C:\\Users\\PRADEEP\\PycharmProjects\\pythonProject5\\Attendence.csv")
readfile.to_excel("C:\\Users\\PRADEEP\\PycharmProjects\\pythonProject5\\Attendence.xlsx",index=None,header=True)

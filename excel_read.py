import pandas as pd

excel_file='C:\\Users\EPCQT\PycharmProjects\\testfile\Book1.xlsx'

ef=pd.read_excel(excel_file)
print(ef.head(10))

import requests
import time
import pandas as pd

xls_file = pd.read_excel('C:\\Users\\xfang\\Desktop\\2022\\LIMS\\API-production1.xlsx', sheet_name="production")
xls_file2 = xls_file[:1000]
xls_file3 = xls_file[1000:]
print(xls_file2)
print(xls_file3)
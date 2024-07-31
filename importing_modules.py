import pandas as pd
import python.pandas.change_excel_sheet_name as d
# python\pandas\pandas_applying.py

path = r'c:\Users\PASGTPK\Downloads\Currency File Feb24FC.xlsb'

x = d.ChangeSheetName(path='./')
print(x.__path__)

ah = pd.read_excel(path, sheet_name='FX Impact by Market')
print(ah)

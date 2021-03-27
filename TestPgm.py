from openpyxl import load_workbook

wb = load_workbook(filename='CatalogEntries-Vita.xlsx') #load workbook from the location
wb.active=2
ws = wb.active
# List sheets available
sheets = wb.get_sheet_names()
print(sheets)

# Load active sheet or named sheet
sheet = wb.active
# sheet = wb['User Information']
# Read a specific cell
print(sheet['J4'].value)

import openpyxl

workbook = openpyxl.Workbook()

sheet = workbook.active

header = ["Name", "Age", "City"]
data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "San Francisco"],
    ["Charlie", 35, "Los Angeles"]
]

sheet.append(header)

for row in data:
    sheet.append(row)

file_name = "sample_excel_file.xlsx"
workbook.save(file_name)

print(f"Excel file '{file_name}' has been created with the header and data.")
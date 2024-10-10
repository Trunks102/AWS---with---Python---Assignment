import csv
header = ["Name", "Age", "City"]
data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "San Francisco"],
    ["Charlie", 35, "Los Angeles"]
]

file_name = "sample_csv_file.csv"

with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header) 
    writer.writerows(data) 

print(f"CSV file '{file_name}' has been created with the header and data.")
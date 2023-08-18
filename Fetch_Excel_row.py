import openpyxl

def excel_row_generator(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    
    for row in sheet.iter_rows(min_row=2, values_only=True):
        # Assuming the first row is headers
        yield row

# Usage
file_path = 'path_to_your_excel_file.xlsx'
sheet_name = 'Sheet1'  # Change to the actual sheet name
for row in excel_row_generator(file_path, sheet_name):
    print(row)

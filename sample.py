from openpyxl import Workbook  
from openpyxl.styles import Font
wb = Workbook()  
sheet = wb.active


sheet['A1'] = "EMP_ID"
sheet['B1'] = "Emp_Name"
sheet['C1'] = "Branch_Name"
sheet['D1'] = "Shift"
sheet['E1'] = "Location"
sheet['F1'] = "Attendance"
sheet['G1'] = "Delay"


sheet['A1'].font = Font(bold=True)
sheet['B1'].font = Font(bold=True)
sheet['C1'].font = Font(bold=True)
sheet['D1'].font = Font(bold=True)
sheet['E1'].font = Font(bold=True)
sheet['F1'].font = Font(bold=True)
sheet['G1'].font = Font(bold=True)

rows = [
    [90, 46, 48, 44],  
    [81, 30, 32, 16],  
    ]  

for i in range(len(rows)):
    sheet.append(rows[i])

   
wb.save(filename='iter_rows.xlsx')  

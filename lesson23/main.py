# from openpyxl import Workbook, load_workbook
# # import datetime

# wb = load_workbook("hello_world.xlsx")

# # ws1['A1'] = 'Hello'
# # ws1['B1'] = 'World'
# # ws1['A2'] = datetime.datetime.now()
# # ws1.append([1, 2, 3])

# ws2 = wb.active
# ws2 = wb.create_sheet('Mysheet')
# ws2['A1'] = 'Hello'
# ws2['B1'] = 'World'
# ws2.title = "New. title"

# print(wb.sheetnames)


# wb.save('hello_world.xlsx')

# wb = load_workbook(filename="hello_world.xlsx")
# sheet = wb["Mysheet"]
# print(sheet['A1'].value)


# sheet = wb["Mysheet"]
# sheet.append([1, 2, 3])

# wb.save('hello_world.xlsx')


# try:
#     a = 4 + 9
#     print(a)
    
# except TypeError:
#     print(f"TypeError occurred")
    
# except ValueError:
#     print("Value error occurred")
    
    
# else:
#     print("No error")

# import openpyxl

# wb = openpyxl.load_workbook("hello_world.xlsx")
# wb  = openpyxl.Workbook()
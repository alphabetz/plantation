import xlsxwriter
import random

# Create workbook
workbook = xlsxwriter.Workbook('tree_data.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column(1, 1, 25)
# data to write header
worksheet.write('A1', 'Tree_Id')
worksheet.write('B1', 'Staff_Email')
worksheet.write('C1', 'GBH')
worksheet.write('D1', 'Height')
worksheet.write('E1', 'Soil_PH')
worksheet.write('F1', 'Note')

# Data to write on TH01-002A-001
'''
data = (
    ['TH01-002A-001', 'wutt@wooooot.com', 45, 250, 6.1, ''],
    ['TH01-002A-002', 'wutt@wooooot.com', 45, 250, 6.1, ''],
)
'''

# To display 000 use f-string
#  for i in range(1,21):
#    print(f"{i:03}")

quad = 'A'
data = []
tree_no = 0
email = 'wutt@wooooot.com'
height = 280
gbh = 45
soil_ph = 6.1


for lot in range(1, 74):
    while (quad < 'E'):
        height = random.randint(150, 220)
        gbh = round(random.uniform(1, 3), 1)
        tree_id = 'TH01-' + f"{lot:03}" + quad + "-" + f"{tree_no+1:03}"
        new_data = [tree_id, email, gbh, height, soil_ph, '']
        data.append(new_data)
        tree_no += 1
        if tree_no == 25:
            quad = chr(ord(quad) + 1)
            tree_no = 0


data = tuple(data)

# Start from the first cell below the headers
row = 1
col = 0

for tree_id, staff_email, gbh, height, soil_ph, note in (data):
    worksheet.write_string(row, col, tree_id)
    worksheet.write_string(row, col + 1, staff_email)
    worksheet.write_number(row, col + 2, gbh)
    worksheet.write_number(row, col + 3, height)
    worksheet.write_number(row, col + 4, soil_ph)
    worksheet.write_string(row, col + 5, note)
    row += 1

workbook.close()
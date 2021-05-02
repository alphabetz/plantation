import xlsxwriter
import random

# Create workbook
workbook = xlsxwriter.Workbook('height_gbh.xlsx')
worksheet = workbook.add_worksheet()

#worksheet.set_column(0, 0, 15)
# data to write header
'''
worksheet.write('A1', 'Tree_Id')
worksheet.write('B1', 'GBH')
worksheet.write('C1', 'Height')
worksheet.write('D1', 'Tree_Id')
worksheet.write('E1', 'GBH')
worksheet.write('F1', 'Height')
worksheet.write('G1', 'Tree_Id')
worksheet.write('H1', 'GBH')
worksheet.write('I1', 'Height')
worksheet.write('J1', 'Tree_Id')
worksheet.write('K1', 'GBH')
worksheet.write('L1', 'Height')
'''

# Data to write on TH01-002A-001
'''
data = (
    ['TH01-002A-001', 45, 250],
    ['TH01-002A-002', 45, 250],
)
'''

# To display 000 use f-string
#  for i in range(1,21):
#    print(f"{i:03}")

def generate_tree(lot):
    #lot = 1
    quad = 'A'
    data = []
    tree_no = 0
    height = ''
    gbh = ''
    while quad < 'E':
        tree_id = f"{lot:03}" + quad + "-" + f"{tree_no+1:03}"
        new_data = [tree_id, height, gbh]
        data.append(new_data)
        tree_no += 1
        if tree_no == 25:
            quad = chr(ord(quad) + 1)
            tree_no = 0
        
    return tuple(data)




# Start from the first cell below the headers
row = 0
col = 0
lot = 1

while lot < 75:
    trees = generate_tree(lot)
    for tree_id,height, gbh in (trees):
        worksheet.write_string(row, col, tree_id)
        worksheet.write_string(row, col+1, height)
        worksheet.write_string(row, col+2, gbh)
        row += 1
        
        if row == 46:
            col += 3
            row = 0
        
    lot += 1

workbook.close()
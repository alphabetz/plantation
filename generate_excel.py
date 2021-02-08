from datetime import datetime
import xlsxwriter

# Create workbook
workbook = xlsxwriter.Workbook('Trees.xlsx')
worksheet = workbook.add_worksheet()

'''
formatdict = {'num_format':'d/m/yyyy'}
fmt = workbook.add_format(formatdict)
'''

date_format = workbook.add_format({'num_format': 'd/m/yyyy'})


worksheet.set_column(1, 1, 25)
# data to write header
worksheet.write('A1', 'country')
worksheet.write('B1', 'phase')
worksheet.write('C1', 'lot')
worksheet.write('D1', 'quad')
worksheet.write('E1', 'tree_no')
worksheet.write('F1', 'product_type')
worksheet.write('G1', 'planted_at')
worksheet.write('H1', 'note')
#worksheet.set_column('G:G', None, fmt)

# Date to write down in worksheet
'''
trees = (
    ['TH', 5, 1, 'A', 1, 14, '10/2/2019', ''],
    ['TH', 5, 1, 'A', 2, 14, '10/2/2019', ''],
)
'''

# TODO: Generate tuple of trees - done.
# TODO: Use function instead
def generate_tree():
    first_1000 = []
    quad = 'A'
    tree_no = 0

    for lot in range(1, 11): 
        while(quad < 'E'):
            new_tree = ['TH', 1, lot, quad, tree_no + 1 , 14, '10/2/2019', '']
            first_1000.append(new_tree)
            tree_no += 1
            if tree_no == 25:
                quad = chr(ord(quad) + 1)
                tree_no = 0

        lot += 1
        quad = 'A'

    return tuple(first_1000)

trees = generate_tree()

# Start from the first cell below the headers
row = 1
col = 0

for country, phase, lot, quad, tree_no, product_type, planted_at, note in (trees):
    # Convert the date string into a datetime object.
    date = datetime.strptime(planted_at, "%d/%m/%Y")

    worksheet.write_string(row, col, country)
    worksheet.write_number(row, col + 1, phase)
    worksheet.write_number(row, col + 2, lot)
    worksheet.write_string(row, col + 3, quad)
    worksheet.write_number(row, col + 4, tree_no)
    worksheet.write_number(row, col + 5, product_type)
    worksheet.write_datetime(row, col + 6, date, date_format)
    worksheet.write_string(row, col + 7, note)
    row += 1

workbook.close()
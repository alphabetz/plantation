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

lot = 1
quad = 'A'
data = []
tree_no = 0
email = 'wutt@wooooot.com'
height = 280
gbh = 45
soil_ph = 6.1

while quad < 'E':
    tree_id = 'TH01-' + f"{lot:03}" + quad + "-" + f"{tree_no+1:03}"
    new_data = [tree_id, email, gbh, height, soil_ph, '']
    data.append(new_data)
    tree_no += 1
    if tree_no == 25:
        quad = chr(ord(quad) + 1)
        tree_no = 0

data = tuple(data)
print(data)
# Generate trees

first_100 = []
quad = 'A'
tree_no = 0

while(quad < 'E'):
    new_tree = ['TH', 5, 1, quad, tree_no + 1 , 14, '10/2/2019', '']
    first_100.append(new_tree)
    tree_no += 1
    if tree_no == 25:
        quad = chr(ord(quad) + 1)
        tree_no = 0

print(tuple(first_100))

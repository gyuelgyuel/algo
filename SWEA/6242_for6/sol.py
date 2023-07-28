blood_types_list = ['A','A','A','O','B','B','O','AB','AB','O']
blood_types = {}
for blood_type in blood_types_list:
    if blood_type in blood_types.keys():
        blood_types[blood_type] += 1
    else:
        blood_types[blood_type] = 1
print(blood_types)
str_list = []
for i in range(200):
    if i % 7 == 0:
        if i % 5 != 0:
            str_list.append(str(i))

string = ','.join(str_list)
print(string)
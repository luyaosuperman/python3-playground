a = [1,2,3,4,5,6,7,8,9]
b = [2,3,5,7,10,11]

hash_dict = {}

for item in a+b:
    if item not in hash_dict:
        hash_dict[item] = 1
    else:
        hash_dict[item] += 1
        if hash_dict[item] == 2:
           print(item)

#for key in hash_dict:
#    if hash_dict[key] > 1:
#        print(key)

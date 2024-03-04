#use such libs for our needs
import random
import string

#range of key values
a = 0
b = 100
#keys = random.sample(string.ascii_lowercase, 5)
#keys2 = random.sample(string.ascii_lowercase, 5)

#creation keys
keys = [random.choice('abcdefg') for _ in range(5)]
keys2 = [random.choice('abcdefg') for _ in range(5)]

#sorted keys
keys = sorted(keys)
keys2 = sorted(keys2)

print(keys)
print(keys2)

#creation dicts
my_dict = {key: random.randint(a, b) for key in keys}
my_dict2 = {key: random.randint(a, b) for key in keys2}

print('My first dictionary ',my_dict)
print('My second dictionary ',my_dict2)

# create newly blank dict
merged_dict = {}

#here we use cycle for to compare all unique keys in both dicts using "|" union of sets.
for key in my_dict | my_dict2:
    #if key present in both dicts we check their values and difine them to newly dict
    if key in my_dict and key in my_dict2:
        if my_dict2[key] > my_dict[key]:
            #merged_dict[key] = my_dict[key]
            #here we insert value from my_dict2 if need as *_2
            merged_dict[key+'_2'] = my_dict2[key]
        else:
            #merged_dict[key] = my_dict2[key]
            # here we insert value from my_dict if need as *_1
            merged_dict[key+'_1'] = my_dict[key]
    elif key in my_dict:
        merged_dict[key] = my_dict[key]
    elif key in my_dict2:
        merged_dict[key] = my_dict2[key]

print('merged dict = ',merged_dict)


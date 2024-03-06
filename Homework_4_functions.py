def main_function(*arg): # here we use *arg
    for i in arg:
        if isinstance(i, int):
            print('\n ===============================')
            print("Wow it's int")


        elif isinstance(i, str):
            print('\n ===============================')
            print("Wow it's str")
            import re

            # here we are normalizing string from case point of view using capitalize
            l_string = i.capitalize()

            #print(l_string)

            # here we are spliting our string on separated sencences using regular expresions.
            sentences = re.split(r'(?<=[.!?])\s*', l_string)

            #print('all parts = ', sentences)

            # variable show when we have to break
            cnt_sentences = len(sentences)
            #print(cnt_sentences)

            b = 1
            new_sentence = ''

            # let's find all last words from all sentences
            for i in sentences:
                a = re.findall(r'\b\w+\b', i)[-1]
                #print('the last word is = ', a)
                b = b + 1
                # print(b)

                # here we are going to generate new sentence
                new_sentence = new_sentence + ' ' + a
                # print(new_sentence)
                if b == cnt_sentences:
                    new_sentence = new_sentence + '.'
                    break

            # print new sentence
            #print(new_sentence)

            l_string = l_string + new_sentence
            #print(l_string)

            # fix "iz" to is where it needed
            l_string = l_string.replace(' iz ', ' is ')
            #print(l_string)

            # prepared variables for loop
            cnt_space = 0
            str_len = len(l_string)
            #print(str_len)

            # here we use "for" loop to check each character in l_string
            for i in range(0, len(l_string)):
                if l_string[i] == " ":
                    cnt_space += 1
            # not sure why but I've calculated just only 85
            print(cnt_space)

            # here we remove enter characted from all string
            l_string = l_string.replace('\n', '')
            print(l_string)


        elif isinstance(i, list):
            print('\n ===============================')
            print("Wow it's list")

            import random
            import string
            print("Imported all libs")

            keys = [random.choice(i[0]) for _ in range(i[1])]
            keys2 = [random.choice(i[0]) for _ in range(i[1])]

            my_dict = {key: random.randint(i[2], i[3]) for key in keys}
            my_dict2 = {key: random.randint(i[2], i[3]) for key in keys2}

            merged_dict = {}

            # here we use cycle for to compare all unique keys in both dicts using "|" union of sets.
            for key in my_dict | my_dict2:
                # if key present in both dicts we check their values and difine them to newly dict
                if key in my_dict and key in my_dict2:
                    if my_dict2[key] > my_dict[key]:
                        # merged_dict[key] = my_dict[key]
                        # here we insert value from my_dict2 if need as *_2
                        merged_dict[key + '_2'] = my_dict2[key]
                    else:
                        # merged_dict[key] = my_dict2[key]
                        # here we insert value from my_dict if need as *_1
                        merged_dict[key + '_1'] = my_dict[key]
                elif key in my_dict:
                    merged_dict[key] = my_dict[key]
                elif key in my_dict2:
                    merged_dict[key] = my_dict2[key]

            print('My first dictionary ', my_dict)
            print('My second dictionary ', my_dict2)
            print('merged dict = ', merged_dict)

#this for collection homework. List should include first value as possible letters for future keys of dict.
#Second value as keys count and min and max values for random values for these keys
#example : main_function(['abcdefsg', 7,1,100])

#===================================================================
# please use main_function and string sentence  to check if it's work
# """"  tHis iz your homeWork, copy these Text to variable.
# 
# 
# 
#   You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
# 
# 
# 
#   it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
# 
# 
# 
#   last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
# """
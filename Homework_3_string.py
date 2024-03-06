import re

# defined string variable and set up text value for futher transformation
l_string = """"  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

print(l_string)

#here we are normalizing string from case point of view using capitalize
l_string = l_string.capitalize()

print(l_string)

#here we are spliting our string on separated sencences using regular expresions.
sentences = re.split(r'(?<=[.!?])\s*', l_string)

print('all parts = ',sentences)

# variable show when we have to break
cnt_sentences = len(sentences)
print(cnt_sentences)

b = 1
new_sentence =''

#let's find all last words from all sentences
for i in sentences:
    a = re.findall(r'\b\w+\b', i)[-1]
    print('the last word is = ', a)
    b = b + 1
    #print(b)

    # here we are going to generate new sentence
    new_sentence = new_sentence + ' ' + a
    #print(new_sentence)
    if b == cnt_sentences:
        new_sentence = new_sentence +'.'
        break

#print new sentence
print(new_sentence)

l_string = l_string + new_sentence
print(l_string)

#fix "iz" to is where it needed
l_string = l_string.replace(' iz ',' is ')
print(l_string)

#prepared variables for loop
cnt_space = 0
str_len = len(l_string)
print(str_len)

#here we use "for" loop to check each character in l_string
for i in range(0, len(l_string)):
    if l_string[i] == " " :
        cnt_space += 1
# not sure why but I've calculated just only 85
print(cnt_space)

#here we remove enter characted from all string
l_string = l_string.replace('\n','')
print(l_string)

import Homework_Modules as hm
import csv
from collections import Counter
import re

Main = hm.main()
Main.run()

# let's prepare file and add some news. Please, use such code and use your file_path path for that.
# Also, your file path we will use in file_path varieble in the next step. Thank you

import csv
import re
from collections import Counter

def count_words(file_path):
    word_counter = Counter()

    # here we open file for reading
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # reading each row in file
            for cell in row:
                # find all words without digitals
                words = re.findall(r'\b[a-zA-Z][a-zA-Z\']*+\b', cell.lower())
                word_counter.update(words)
                #for word, count in word_counter.items():
                #    print(f'{word}: {count}')
    return word_counter
    # word, count

# file_path where from we are supposed to read data. USE here your file_path please !!!!!!!!!!!!!
file_path = "C:\\Users\\Artur_Khomenko\\Desktop\\input_directory\\publish_news.csv"

unique_word_count = count_words(file_path)
print(unique_word_count)


#here we are supposed to use file path where we will insert words and their count
file_path = "C:\\Users\\Artur_Khomenko\\Desktop\\input_directory\\word_count_file.csv"

def write_into_word_count_file(file_path,word_cnt):
    word_counter = word_cnt

    with open(file_path, 'w', newline='') as csv_file:
        for word, count in word_counter.items():
            print(f'Word : {word} - {count}')
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow( [word.lower(),count] )

write_into_word_count_file(file_path,unique_word_count)


def calculate_percentage(count, total):
    return (count / total) * 100 if total != 0 else 0


# file path where to we want load data
file_path = "C:\\Users\\Artur_Khomenko\\Desktop\\input_directory\\total_word_file.csv"

def write_into_total_file(file_path):

    # here we are calculating total count of letters and letter count
    total_letters = sum(len(word) for word in unique_word_count.keys())
    letter_counts = Counter(char.lower() for word in unique_word_count.keys() for char in word)

    upper_letter_counts = Counter(char for word in unique_word_count.keys() for char in word if char.isupper())

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['letter', 'count_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for letter, count in letter_counts.items():
            uppercase_count = upper_letter_counts.get(letter, 0)
            percentage = calculate_percentage(count, total_letters)
            writer.writerow({'letter': letter, 'count_all': count, 'count_uppercase': uppercase_count, 'percentage': percentage})

    print("Data have loaded succesfully!")

write_into_total_file(file_path)
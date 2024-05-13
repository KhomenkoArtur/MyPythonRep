import xml.etree.ElementTree as ET
import os
import random
import datetime
import csv
import sys
import Homework_function as hf
import json

class NewsFeed:
    def __init__(self):
        self.feed = []
        self.file_path = []

    def add_record(self, record_type, data):
        self.feed.append({'type': record_type, 'data': data})

    def publish_feed(self, filename):
        with open(filename, "a") as file:
            for record in self.feed:
                file.write(f"{record['type']}: {record['data']}\n")

    def get_randon_motivation_phrase(self):
        motivation_phrases =["The only way to do great work is to love what you do.","Believe you can and you're halfway there.","Dream it. Wish it. Do it.",
                             "Success is not final, failure is not fatal: It is the courage to continue that counts.","Don't stop when you're tired. Stop when you're done.",
                             "Push yourself, because no one else is going to do it for you.","Dream bigger. Do bigger.",
                             "The harder you work for something, the greater you'll feel when you achieve it.","Dream it. Believe it. Build it.",
                             "Strive for progress, not perfection.","Do what you love, love what you do.","Don't wait for opportunity. Create it.",
                             "Wake up with determination. Go to bed with satisfaction.","Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
                             "Don't count the days, make the days count.","Success doesn't just find you. You have to go out and get it.",
                             "The only limit to our realization of tomorrow will be our doubts of today.","Dream big and dare to fail.",
                             "Make each day your masterpiece.","You are the only one who can limit your greatness."]

        return random.choice(motivation_phrases)


class TextRecord:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

############################ Newly created logic to parse File ####################################
class FileParser:
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        try:
            with open(self.filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("File not found.")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []

#################### Newly created logic to write data into the file ############################
class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, lines):
        try:
            with open(self.filename, 'w') as file:
                for line in lines:
                    file.write(line)
        except Exception as e:
            print(f"Error writing to file: {e}")


################### 20240418 create logic to parse json file and add news and privat ad and public it to the file
class JsonFileParser:

    def __init__(self,filename):
        self.filename = filename

    def ParseJsonFile(filename):
        total_news = ""
        with open(filename, 'r') as file:
            for json_line in file:
                json_object = json.loads(json_line)
                # print(json_object)
                # print(type(json_object))

                # if type is news then let's write it's context as news
                if "type" in json_object and json_object["type"] == "news":
                    # print("it is fucken news")
                    # generate news message
                    news = "\n\nNews feed\n---------------------------------\n" + json_object["text"] + "\n" + \
                           json_object["city"] + ", " + str(
                        datetime.datetime.now()) + "\n================================="
                    # print(news)

                    total_news = total_news + news
                    # return news
                # if type is add then let's write it's context as privat add
                elif "type" in json_object and json_object["type"] == "privat_ad":
                    # print("it is fucken ad")
                    # generate Privat ad message
                    news = "\n\nPrivat ad\n---------------------------------\n" + json_object[
                        "text"] + "\n Actual until: left " + str(datetime.datetime.strptime(json_object["expiration"],
                                                                                            "%Y-%m-%d").date() - datetime.date.today()) + "\n================================="

                    # print(news)

                    total_news = total_news + news
                    # return news
                else:
                    print("not sure what is it pease of shit")

        return total_news

    ################### 20240418 create logic to parse json from user and add news and privat ad and public it to the file
    def ParseJsonString(json_string):
        total_news =""
        #print(type(json.loads(json_string)))
       #json_str = json.loads(json_string)
        json_str = json_string
        if "type" in json_str and json_str["type"] == "news":
                # print("it is fucken news")
                # generate news message
            news = "\n\nNews feed\n---------------------------------\n" + json_str["text"] + "\n" + json_str["city"] + ", " + str(datetime.datetime.now()) + "\n================================="
                # print(news)
            total_news = total_news + news
                # return news
            # if type is add then let's write it's context as privat add
        elif "type" in json_str and json_str["type"] == "privat_ad":
                # print("it is fucken ad")
                # generate Privat ad message
            news = "\n\nPrivat ad\n---------------------------------\n" + json_str["text"] + "\n Actual until: left " + str(datetime.datetime.strptime(json_str["expiration"],"%Y-%m-%d").date() - datetime.date.today()) + "\n================================="
            total_news = total_news + news
            # return news
        else:
                print("something went wrong")
        return total_news


################### 20240513 create logic to parse XML file and add news and privat ad and publish it into the file
class XmlFileParser():

    def ParseXmlFile(file_path):
        # xml file parsing
        tree = ET.parse(file_path)
        root = tree.getroot()
        total_return_value = ""

        for type_element in root.findall('type'):
            name = type_element.get('name')
            text = type_element.find('text').text
            city = type_element.find('city').text
            expiration = type_element.find('expiration')

            # print( name)
            return_value = '\n' + name
            # print("-" * 30)
            return_value = return_value + '\n' + "-" * 30
            # print( text)
            return_value = return_value + '\n' + text
            # print( city)
            return_value = return_value + '\n' + city
            if expiration is not None:
                # print("Actual until: left " + str(datetime.datetime.strptime(expiration.text,"%Y-%m-%d").date() - datetime.date.today()))
                return_value = return_value + '\n' + "Actual until: left " + str(
                    datetime.datetime.strptime(expiration.text,
                                            "%Y-%m-%d").date() - datetime.date.today()) + '\n' + "=" * 30 + '\n'
                print("=" * 30 + '\n')

            total_return_value = total_return_value + '\n' + return_value

        return total_return_value


    def check_for_xml_files(file_path):
        #xml_files = [file for file in os.scandir(file_path) if file.endswith('.xml')]
        xml_files = [entry.name for entry in os.scandir(file_path) if entry.name.endswith('.xml') and entry.is_file()]
        return xml_files

    def check_xml_format(file_path):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            if root.tag != 'news_feed':
                # raise ValueError("Invalid XML format: Root tag must be 'news_feed'")
                return 0
            for child in root:
                if child.tag != 'type' or 'name' not in child.attrib:
                    # raise ValueError("Invalid XML format: Each 'type' tag must have a 'name' attribute")
                    return 0
            # ("XML format is correct")
            return 1
        except ET.ParseError as e:
            # print("Invalid XML format:", e)
            return 0

class main():
    def __init__(self):
        self.file_parser = None
        self.file_writer = None

    def run(self):
        news_feed = NewsFeed()
        while True:
            print("1. Publish news feed")
            print("2. Publish privat ad")
            print("3. Return your good prediction")
            print("4. Exit")
            print("5. Parse file and insert data to another file ==== new option from homework 6")
            print("6. JSON option ==== new option from homework 8")
            print("7. XML option ==== new option from homework 9")
            choice = input("Enter your choice: ")

            if  choice == "1":
                filename = input("Enter the filepath to publish the news feed: ")
                news = "News feed\n---------------------------------\n" + input("Please write your news: ")
                city = input("Please write a city where it happened: ")
                current_datetime = datetime.datetime.now()
                news = news + "\n" + city + ", " + str(current_datetime) +"\n================================="
                news_feed.add_record(choice, news)
                news_feed.publish_feed(filename)
                print("News feed published successfully!\n=====================\n ")
            elif choice == "2":
                filename = input("Enter the filepath to publish the privat ad: ")

                news = "Privat ad\n---------------------------------\n" + input("Please write your privat ad: ")

                publish_expiration = input("Enter publish expiration in date format as YYYY-MM-DD : ")

                try:
                    publish_expiration = datetime.datetime.strptime(publish_expiration, "%Y-%m-%d").date() - datetime.date.today()
                    print("Inputed date:", publish_expiration)
                except ValueError:
                    print("Invalide date. Please use such date format  YYYY-MM-DD.")

                #days_left = datetime.date.today()
                publish_expiration = publish_expiration.days
                news = news + "\n Actual until: left" + str(publish_expiration) +"\n================================="

                news_feed.add_record(choice, news)
                news_feed.publish_feed(filename)

                print("Your privat ad added to the file\n=====================")
            elif choice == "3":
                filename = input("Enter the filepath to publish the news feed: ")
                prediction = "motivation_phrase for all day\n---------------------------------\n" + news_feed.get_randon_motivation_phrase() +"\n================================="
                news_feed.add_record(choice, prediction)
                news_feed.publish_feed(filename)
            elif choice == "4":
                break

########################### Newly created logic ###########################
            elif choice == "5":
                file_path = input("Enter the file path to parse: ")
                if file_path:
                    self.file_parser = FileParser(file_path)
                    lines = self.file_parser.parse()

                    if lines: ####If we parsed all file then we will remove it using os.remove
                        os.remove(file_path)
                        print("File successfully parsed and removed.")
                    else:
                        print("No data parsed. File not removed.")

                    file_path = input("Enter the file path to insert: ")
                    self.file_writer = FileWriter(file_path)
                    self.file_writer.write(hf.normalized_string(str(lines) ) )

                else:
                    file_path = sys.path[1]
                    print("You didn't insert filepath. Using default path " + str(file_path))
                    # here can be next logic

            elif choice == "6":
                file_path = input("Enter the JSON file path for parsing. If you haven't a file press enter for next tips. ======= ")

                if file_path:
                    result = JsonFileParser.ParseJsonFile(file_path)
                    # C:\Users\Artur_Khomenko\Desktop\input_directory\test.json
                    filename = input("Enter the filepath to publish the news feed: ")
                    # C:\Users\Artur_Khomenko\Desktop\input_directory\publish_news.csv
                    news_feed.add_record(choice, result)
                    news_feed.publish_feed(filename)

                else:
                    print("You didn't insert filepath. Perhaps you want insert your JSON without file ========")
                    json_value = input("Please input here your JSON to publish in neews feed : ")
                    try:
                        json_value = json.loads(json_value)
                        if isinstance(json_value, dict):
                            filename = input("Enter the filepath to publish the news feed: ")
                            result = JsonFileParser.ParseJsonString(json_value)
                            news_feed.add_record(choice, result)
                            news_feed.publish_feed(filename)
                    except ValueError:
                        print("ERROR --->>> Invalide JSON format. Please use format like this : {""""type"""": """"news"""", """"text"""": """"your text"""", """"city"""": """"your city""""} ")
                        break
#######################################################
##### NEWly created part of code related to XML parsing. Also another part present at 142 - 192 lines above
#######################################################
            elif choice == "7":
                file_path = input("Enter the XML file path for parsing. If you haven't a file press enter for next tips. ======= ")

                if file_path:
                    xml_check_format = XmlFileParser.check_xml_format(file_path)
                    if xml_check_format != 1:
                        print('XML format is wrong. Please use <news_feed> as a root tag. Root tag should save child tag as name. Name have to save <text>,<city>,<expiration> tags')
                        break
                    else:
                        result = XmlFileParser.ParseXmlFile(file_path)
                        filename = input("Enter the filepath to publish the news feed: ")
                        # C:\Users\Artur_Khomenko\Desktop\input_directory\publish_news.csv
                        news_feed.add_record(choice, result)
                        news_feed.publish_feed(filename)

                else:

                    file_path = sys.path[0]
                    print(file_path)
                    xml_files = XmlFileParser.check_for_xml_files(file_path)
                    #print(xml_files[0])
                    #print(xml_files)
                    if xml_files:
                        print("XML file found: " + str(file_path ) + "\\"+ str(xml_files[0] ) )
                        file_path = file_path + "\\"+ str(xml_files[0] )
                        print(file_path)

                        xml_check_format = XmlFileParser.check_xml_format(file_path)
                        if xml_check_format != 1:
                            print(
                                'XML format is wrong. Please use <news_feed> as a root tag. Root tag should save child tag as name. Name have to save <text>,<city>,<expiration> tags')
                        else:
                            for file in xml_files:
                                result = XmlFileParser.ParseXmlFile(file_path)
                                filename = input("Enter the filepath to publish the news feed: ")
                                # C:\Users\Artur_Khomenko\Desktop\input_directory\publish_news.csv
                                news_feed.add_record(choice, result)
                                news_feed.publish_feed(filename)
                    else:
                        print("No XML files found in the directory:", file_path)

            else:
                print("=====================\nInvalid choice\n=====================")


if __name__ == "__main__":
    Main = main()
    Main.run()

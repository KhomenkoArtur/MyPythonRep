import random
import datetime

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


def main():
    news_feed = NewsFeed()
    while True:
        print("1. Publish news feed")
        print("2. Publish privat ad")
        print("3. Return your good prediction")
        print("4. Exit")
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
        else:
            print("=====================\nInvalid choice\n=====================")


if __name__ == "__main__":
    main()

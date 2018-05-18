import webbrowser
import time


name = "JuJu Smith-Schuster"

subjects = ["Mandarin","Science","History","English","Math"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)
    
games = ["Call of Duty","Fortnite","Pubg","CS:GO"]

for i in games:
    if i == "Fortnite":
        print(i + " never loads...")
    elif i == "Pubg":
        print(i + " is a better Fornite.")
    elif i == "CS:GO":
        print(i + " is currently irrelevant.")
    elif i == "Call of Duty":
        print(i + " has had some really bad games but pulled through with WW2.")
    else:
        print("My favorite video game is " + i)

movies = []

while True:
    print("What movie do you like? Type 'end' to quit.")
    answer = input()
    
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorite movies is " + i)
    webbrowser.open(i + " movie poster")
    time.sleep(1)

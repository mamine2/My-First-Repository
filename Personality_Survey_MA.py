print("What is your favorite color?")
color = input().lower()

if color == "red":
    print("Red is a great color.")
elif color == "blue":
    print("Good Choice!")
else:
    print("Mhm, nice!")
    


print("What's your favorite sport")
sport = input().title()

if sport == "Football" or "Lacrosse":
    print("Wow, me too!")
elif sport == "Tennis":
    print("Great sport, but I'm not a fan")
elif sport == "Soccer":
    print("Nice!")
else:
    print("Great.")



print("What is your favorite tv show?")
tvshow = input().title()

if tvshow == "The Office":
    print("Who is your favorite character from the office?")
    character = input()

    if character == "Dwight":
        print("Fact. Me too.")
    elif character == "Michael":
        print("JAN!")


print("What is your favorite book")
book = input().title()

if "Martian" in book:
    print("Im a botanist!")
    


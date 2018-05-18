import pyautogui as pg
import time
import webbrowser

points = 0

#Question goes here
answer = pg.prompt(
"""
Which would you rather do?

a) Get injured when your team needs you most
b) Be good, on the worst team in the NFL
c) Be on the dirtiest playing team in the league but do well

""")

pg.alert("You chose" + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""
Which would you rather do?

a) Break your collar bone
b) Have your best cornerback tear their achilles
c) Illegally hit Antonio Brown in the playoffs

""")

pg.alert("You chose" + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""
Which would you rather do?

a) Have Bret Hunley as your backup quarterback
b) Have your starting running back weight more than an O-Lineman
c) Have a losing season this year

""")

pg.alert("You chose" + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""
Which would you rather do?

a) Lose to the Detroit Lions and not make the playoffs
b) Lose to Tom Brady in the Superbowl when you could have won
c) Lose to the Steelers twice this season

""")

pg.alert("You chose" + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

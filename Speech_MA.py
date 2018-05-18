import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")


"""
speak.Speak("What's suh dud?")
suh = pg.prompt("Enter what's suh dude")
if suh == "not much":
    speak.Speak("Oh! Same brother.")
elif suh == "I have school classes right now":
    speak.Speak("Oh no!")
else:
    speak.Speak("Rest in peace Avicci")

speak.Speak("What video do you want to watch?")
video = pg.prompt("Enter your video below.")
speak.Speak("Ok, let's look for " + video + " on Youtube.")
wb.open("https://www.youtube.com/results?search_query=" + video)
"""

speak.Speak("What do you want to search for?")
search = pg.prompt("Enter your search below.")
speak.Speak("Ok, let's look for " + search + " on Google.")
wb.open("https://www.google.com/search?q=" + search)

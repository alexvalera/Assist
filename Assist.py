import webbrowser
import random
from os import *

#COMMANDS
#Open (Websites, documents, files, applications)

#Create Suffix and Prefix checkers for user_input
WEBSITE_SUFFIX = ".com"
WEBSITE_PREFIX = "www."
WEBSITE_PREFIX_2 = "http://"

APP_SUFFIX = ".app"

WEBSITE_URL_CHECKERS = (WEBSITE_SUFFIX, WEBSITE_PREFIX, WEBSITE_PREFIX_2)

#Create phrases
GREETING_1 = "Hello, how may eye help you"
GREETING_2 = "Hello, what shall we do"
GREETING_3 = "Hello, let's get started."

GREETING_LIST = (GREETING_1,GREETING_2,GREETING_3)




def checkWeb(phrase):
    check = 0
    for checker in WEBSITE_URL_CHECKERS:
        if checker in phrase:
            check+=1
    if check == 3:
        return phrase
    else:
        for checker in WEBSITE_URL_CHECKERS:
            if checker in phrase:
                phrase = phrase.replace(checker,"")
        return phrase

def checkApp(phrase):
    check = 0
    if APP_SUFFIX in phrase:
        check+=1
    if check == 1:
        return phrase
    else:
        if APP_SUFFIX in phrase:
            phrase = phrase.replace(APP_SUFFIX, "")
        return phrase

def inAppList(phrase):
    phrase = checkWeb(phrase)
    phrase = checkApp(phrase)
    phrase = (phrase + ".app")
    if phrase in listdir("/Applications"):
        #system("open /Applications/" + phrase)
        return True
    else:
        return False
        

def main():
    greetInt = random.randint(1,3)
    greeting = GREETING_LIST[greetInt-1]
    system('say ' +str(greeting))
    user_input = raw_input("What can I help you with?  ")
    #print (user_input)
    while user_input:
        user_input = str(user_input)
        input_checked = checkWeb(user_input)
        input_checked_app = checkApp(input_checked)
        #print (input_checked_app)
        if inAppList(user_input):
            system('say Opening' + str(input_checked_app))
            system('open /Applications/' +input_checked_app + '.app')
            user_input = raw_input("Anything else? ")
        else:
            system('say here is ' + input_checked_app)
            webbrowser.open('http://'+input_checked+'.com')
            user_input = raw_input("Anything else? ")


main()
    
    

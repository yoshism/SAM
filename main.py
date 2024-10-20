# youtube - Play
# jokes - Tell me a joke
# wikipedia - who
# google search - Search

"""
This a mini program that I call *SAM* for Special Action Model.
SAM is capable of task like:
    * searching on google
    * playing youtube video
    * searching name on wikipedia
    * tell you jokes.


How to use? 
Before anything on your terminal you need to download the following python library:
*run "pip install pyjokes"
*run "pip install pywhatkit"
*run "pip install wikipedia"
*run "pip install selenium"


    * Hi my name is SAM. SAM means Special Action Model
    *Run the program
    * On the terminal it will return you welcome
    * Where it is written "Type here* " type your request(see guide)
 
"""

#the guide of the program
guide = """
Input guide:
    This program only accept the input below:

    *G
        Access the guide
    *K
        Kill the terminal
    *Search 
        Make a search on Google
    *Who
        Search for someone using Wikipedia
    *Play
        Search on YouTube
    *Tell me a joke
        To tell you a joke
        
        *n
            Neutral joke
        *c
            Chuck Norris joke
        *a
            Any type of joke 
        *m
            Joke from my library
"""

import pyjokes
import pywhatkit
from selenium import webdriver
import time
import random

#Because of limited jokes from pyjokes I had to create my own library
def my_jokes():

    #my joke list
    jokes_list = [
    #disclaimer: Those jokes where copied from "www.cosmopolitan.com/uk/lifestyle/funny-jokes/"
    f"How do you know if a vampire is unwell? \n🤣 Because he'll be coffin", 
    f"Where do pirates get their hooks?\n🤣 Second hand shops", 
    f"Why did the bicycle collapse?\n🤣 It was too tyred", 
    f"What kind of music do bubbles hate?\n🤣 Pop",
    f"Why did the hairdresser win the race?\n🤣 He knew a shortcut",
    f"How did the picture end up in prison? \n🤣 It was framed",
    f"What do solicitors wear to work? \n🤣 Lawsuits",
    f"Why did the bullet lose its job? \n🤣 It got fired",
    f"Why can’t a toe be 12 inches long? \n🤣 Then it’d be a foot",
    f"Want to hear a joke about a roof? \n🤣 The first one’s on the house",
    f"What does a house wear? \n🤣 Address",
    f"What did one wall say to the other? \n🤣 I'll meet you at the corner",
    f"Why is grass so dangerous? \n🤣 It’s full of blades",
    f"What’s orange and sounds like a carrot? \n🤣 A parrot",
    f"Why do French people eat snails? \n🤣 They don’t like fast food",
    f"Where do hamburgers and hot dogs go dancing? \n🤣 A meatball",
    f"How do trees get online? \n🤣 They just log on!",
    f"How do billboards talk? \n🤣 Sign language"
    f"What do PHD students eat when they're hungry?\n🤣 Academia nuts",
    f"Why should you always knock before opening the fridge door?\n🤣 In case there's a salad dressing",
    f"Why couldn't the sesame seed stop talking?\n🤣 He was on a roll",
    f"Why do prawns never share?\n🤣 Because they're shellfish",
    f"What did the cheese say to himself in the mirror?\n🤣 Halloumi!",
    f"What do you call a drunk parsnip?\n🤣 A steaming vegetable",
    f"Why did the mushroom go to the party?\n🤣 Because he was a fungi",
    f"Why did the Oreo go to the dentist?\n🤣 Because he lost his filling",
    f"What did one pickle say to the other?\n🤣 Dill with it",
    f"What food is never on time?\n🤣 Choco-late!",
    f"What do you call a fake noodle?\n🤣 An impasta",
    f"What’s the most famous fish?\n🤣 A starfish!",
    f"What are spiders really good at?\n🤣 Surfing the web",
    f"What do you call a magic dog?\n🤣 A labracadabrador",
    f"How does a farmer keep track of his cattle?\n🤣 With a cow-culator",
    f"What do you call an alligator detective?\n🤣 An investi-gator",
    f"Where would you find a giraffe?\n🤣 The same place you lost it!",
    f"Why don't they play cards in the jungle?\n🤣 Too many cheetahs",
    f"How do you measure a slug?\n🤣 In inches, because they don't have feet",
    f"What social events do spiders love to attend?\n🤣 Webbings",
    f"What do you get from a pampered cow?\n🤣 Spoiled milk",
    f"Why aren’t koalas considered bears?\n🤣 They don’t have the right koala-fications",
    f"What do you call a well-balanced horse?\n🤣 Stable",
    f"What do you call a bear with no teeth?\n🤣 A gummy bear",
    f"What’s the smartest insect?\n🤣 A spelling bee!",
    f"What do you call a singer with a laptop on her head?\n🤣 A-Dell",
    f"When is a door not a door?\n🤣 When it's ajar",
    f"What do toilets do when they're embarrassed?\n🤣 They always get a bit flush",
    f"How do you organise a space-themed party?\n🤣 You planet",
    f"Why do pancakes always win at cricket?\n🤣 They have the best batter",
    f"Why did the robot arrive at the event so tired?\n🤣 He had a hard-drive",
    f"What do runners eat before a race?\n🤣 Nothing - they fast",
    f"How do you stop an astronaut’s toddler from crying?\n🤣 You rocket",
    f"What do you call an unpredictable camera?\n🤣 A loose Canon",
    f"Why shouldn't you use a broken pencil?\n🤣 Because it's point-less",
    f"What did the policeman say to his nipple?\n🤣 You're under a vest",
    f"Why couldn’t the sailor learn the alphabet?\n🤣 He kept getting lost at C",
    f"Why was Cinderella so bad at rugby?\n🤣 She kept running away from the ball",
    f"What did the dentist win at the competition?\n🤣 A little plaque",
    f"What do you call a skeleton with only a head?\n🤣 A nobody",
    f"What’s the difference between a hippo and a zippo?\n🤣 One's very heavy and the other’s a little lighter.",
    f"Why do ghosts like to take the lift?\n🤣 It lifts their spirits",
    f"What do you call a patronising bear?\n🤣 A pan-duh",
    f"Why did the scarecrow win an award?\n🤣 He was outstanding in his field",
    f"Why didn't the skeleton never go on dates?\n🤣 He didn't have the guts to ask anyone",
    f"Do you want to hear a construction joke?\n🤣 Sorry, I’m still working on it",
    f"Why doesn't Dracula have any friends?\n🤣 He's a bit of a pain in the neck",
    f"What do you call a guy who’s really loud?\n🤣 Mike",
    f"What do you call a retired vegetable?\n🤣 A has-bean",
    f"Can February March?\n🤣 No, but April May!",
    f"Why shouldn't you marry a calendar?\n🤣 Its days are numbered",
    f"Why do barbers make good drivers?\n🤣 They know a lot of short cuts"
k
    ]

    #take a random joke of my list
    l = len(jokes_list) - 1
    x = random.randint(0, l)
    joke = jokes_list[x]
    print("")
    print(joke)

# Will return you a joke
def jokes():
    type = input("What type of joke do you want? ")
    type = type.lower()

    #Those are for the jokes from pyjokes
    if type == "n" or type == "c" or type == "a":
        if type == "n":
            type = "neutral"
        elif type == "c":
            type = "chuck"
        elif type == "a":
            type = "all"
        

        your_joke = pyjokes.get_joke(category= type)
        print("")
        print(f"💥 {your_joke} 💥")

    #To access the jokes in my own jokes library
    elif type == "m":
        my_jokes()    

    #For error handling
    else:
        print("Invalid type")
    return True


# Open youtube and play a video
def youtube():
    video = input("The title of your video here *")

    print(f"SEARCHING... {video}")
    pywhatkit.playonyt(video)

    return True


# use selenium webdriver API to search name 
def wiki():

    search = input("Who do you want me to search?\n(Press enter to go to the main page) ")
    search = search.replace(" ", "_")

    sleep = input("How much time do you want this window open for (seconds) Default:30s *")
       
    if sleep.isnumeric == True:
        sleep = int(sleep)
    else:
        sleep = 30

    url = f"https://en.wikipedia.org/wiki/{search}"

    driver = webdriver.Chrome()
    
    if search == "" or search == " ":

        search = search.replace("_", "")
        print("Invalid Input")
    
        print(f"SEARCHING... {search}")
        driver.get(f"{url}")

        time.sleep(sleep)

        return True


    else:
        return True
        


#Open google then do search on it
def google():
    #No easy library to open google so I have to be creative do this my own way
    search = input("What do you want me to search\nPress enter to go to the main page ")
    search = search.replace(" ", "+")
    
    sleep = input("How much time do you want this window open for (seconds) Default:30s *")
    
    if sleep.isnumeric == True:
        sleep = int(sleep)
    else:
        sleep = 30

    url = f"https://www.google.com/search?q={search}"

    driver = webdriver.Chrome()

    if search != " ":
        print(f"SEARCHING... {search}")
        driver.get(f"{url}")
        time.sleep(sleep)

    else:
        return True    

    return True


# Main module where all comes together
def main():
    print("👋 Hey I am SAM 🤖 \n🤖 SAM stands for Special Action Model \nI was created 💻 as Final project by Loens")
     
    while True:
        print("")
        print("⌨️ Tell me what you want me to do. \nType 'G' to see the guide.🧭 ")
        
        prompt = input("Type here *")
        prompt = prompt.lower()

        #Logic for the program
        if prompt == "tell me a joke":
            jokes()

        elif prompt ==  "k":
            break

        elif prompt == "g":
            print(guide)

        elif prompt == "play":
            youtube()

        elif prompt == "search":
            google()

        elif prompt == "who":
            wiki()
        #error handling
        else:
            print("😖 Invalid input, I was not programmed for that")    

        

main()

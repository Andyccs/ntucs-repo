#Andy Chong Chin Shin

def welcome():
    """hangman welcome graphic"""
    print("""
OO   OO    OOOOO    OO      OO     OOOOO     OO        OO    OOOOO    OO      OO
OO   OO   OOO OOO   OOOO    OO   OOO   OOO   OOO      OOO  OOOOOOOOO  OOOO    OO
OO   OO  OO     OO  OO OO   OO  OO           OOOO    OOOO  OO     OO  OO OO   OO
OOOOOOO  OO     OO  OO  OO  OO  OO           OO OO  OO OO  OO     OO  OO  OO  OO
OO   OO  OOOOOOOOO  OO   OO OO  OO    OOOOO  OO  OOOO  OO  OOOOOOOOO  OO   OO OO
OO   OO  OO     OO  OO    OOOO  OO       OO  OO   OO   OO  OO     OO  OO    OOOO
OO   OO  OO     OO  OO     OOO   OOO   OOO   OO        OO  OO     OO  OO     OOO
OO   OO  OO     OO  OO      OO     OOOOO     OO        OO  OO     OO  OO      OO

    """)

def dictionary():
    """define a dictionary with 4 scope and five words for each scope"""
    MakeDictionary = {  "computer science"   :   ["python","prolog","computer","program","internet"],
                        "colour"             :   ["violet","blue","green","yellow","purple"],
                        "mathematics"        :   ["probability","differentiation","addition","subtraction","division"],
                        "science"            :   ["biology","chemistry","physics","zoology","quantum"]}
    return MakeDictionary

def select_word(FromDictionary):
    """ select a word randomly from the dictionary
    print the scope and return WordChosen """
    #make all keys in dictionary to be a list
    #select a key in the list randomly, make all values of the key to be a list
    #select a value randomly from the list
    ScopeAvailable = list(FromDictionary.keys())
    import random
    ScopeChosen = random.choice (ScopeAvailable)
    ListOfWordChosen = FromDictionary[ScopeChosen]
    WordChosen = random.choice(ListOfWordChosen)
    print("{:^40s}".format("Scope: "+ScopeChosen))
    return WordChosen

def ShowGraphic(chance):
    """graphic of hangman"""
    if chance == 9:
        print("{:^40s}".format("          "))
        print("{:^40s}".format("          "))
        print("{:^40s}".format("          "))
        print("{:^40s}".format("          "))
        print("{:^40s}".format("          "))
    elif chance == 8:
        print("{:^40s}".format("          "))
        print("{:^40s}".format("          "))
        print("{:^40s}".format("          "))
        print("{:^40s}".format("          "))
        print("{:^40s}".format("__________"))
    elif chance == 7:
        print("{:^40s}".format("          "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("__|_______"))
    elif chance == 6:
        print("{:^40s}".format("   ____   "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("__|_______"))
    elif chance == 5:
        print("{:^40s}".format("   ____   "))
        print("{:^40s}".format("  |    O  "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("__|_______"))
    elif chance == 4:
        print("{:^40s}".format("   ____   "))
        print("{:^40s}".format("  |    O  "))
        print("{:^40s}".format("  |    |  "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("__|_______"))
    elif chance == 3:
        print("{:^40s}".format("   ____   "))
        print("{:^40s}".format("  |    O  "))
        print("{:^40s}".format("  |   /|  "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("__|_______"))
    elif chance == 2:
        print("{:^40s}".format("   ____   "))
        print("{:^40s}".format("  |    O  "))
        print("{:^40s}".format("  |   /|\\ "))
        print("{:^40s}".format("  |       "))
        print("{:^40s}".format("__|_______"))
    elif chance == 1:
        print("{:^40s}".format("   ____   "))
        print("{:^40s}".format("  |    O  "))
        print("{:^40s}".format("  |   /|\\ "))
        print("{:^40s}".format("  |   /   "))
        print("{:^40s}".format("__|_______"))

    elif chance == 0:
        print("{:^40s}".format("   ____   "))
        print("{:^40s}".format("  |    O  "))
        print("{:^40s}".format("  |   /|\\ "))
        print("{:^40s}".format("  |   / \\ "))
        print("{:^40s}".format("__|_______"))

def ShowCurrentStatus(CurrentStatus):
    """input a list of word in 'list', output a list of word in 'string'"""
    print("{:^40s}".format(" ".join(CurrentStatus)))

def ShowGuessedWord(alphabet_guess_already):
    """show all word in the list of alphabet_guess_already"""
    print("{:^40s}".format("you have guess: "+" ".join(alphabet_guess_already)))

def ShowChance(chance):
    """show how many chances are left"""
    print("{:^40s}".format("you have {} more chance".format(chance)))

def AskForInput():
    print("{:^40s}".format("You may enter 'hint' for a hint"))
    print("{:^40s}".format("Please enter an alphabet: "))

def GetInput():
    """Get player inputs and lower-case the input"""
    Input = str(input("{:>20s}".format("")))
    print("\n \n \n \n \n")
    return Input.lower()

def CheckInput(Input):
    """check for player input.
    If it is 'hint' or a alphabet,
    return True"""
    if Input.lower() == "hint":
        return True
    elif len(Input) == 1 and Input.islower():
        return True
    else:
        return False

def MultipleSameInput(Input,alphabet_guess_already):
    """if Input is in alphabet_guess_already, return True"""
    if Input in alphabet_guess_already:
        return True
    else:
        return False

def GiveHint(CurrentStatus,word):
    """ if player ask for a hint
    select an alphabet that is correct and has not been guessed by player
    print out the hint"""
    ListOfHint =[]
    #iterate through CurrentStatus to check for alphabets that haven't been guessed by player
    #make all the alphabets to be a list
    for n in range (0, len(CurrentStatus)):
        if CurrentStatus[n] == "_":
            ListOfHint.append(n)
    import random
    #choose an alphabets randomly from the list
    ChosenHint = random.choice(ListOfHint)
    ChosenHint = word[ChosenHint]
    print("you hint is: ",ChosenHint)

def CorrectOrWrong(Input,word):
    """Check if Input is inside word"""
    if Input in word:
        return True
    else:
        return False

def UpdateVariable(Input,word,CurrentStatus,chance):
    """if Input is correct, update CurrentStatus.
    If input is wrong, update chance
    return CurrentStatus,chance """
    if CorrectOrWrong(Input,word):
        for n in range (0,(len(word))):
            if Input == word[n]:
                CurrentStatus[n] = Input
    else:
        chance -= 1
    return CurrentStatus,chance

def UpdateGuessWord(Input, alphabet_guess_already):
    """update new Input to alphabet_guess_already"""
    alphabet_guess_already.append(Input)
    return alphabet_guess_already

def Win(CurrentStatus,word):
    """check if player win"""
    if CurrentStatus == word:
        return True
    else:
        return False

def Lose(chance):
    """check if player lose"""
    if chance == 0:
        return True
    else:
        return False

def game():
    """whole game process"""
    welcome()

    MyDict = dictionary()
    word = list(select_word(MyDict))
    CurrentStatus = list("_"*len(word))
    chance = 9
    alphabet_guess_already=[]

    while True:
        ShowGraphic(chance)
        ShowCurrentStatus(CurrentStatus)
        ShowGuessedWord(alphabet_guess_already)
        ShowChance(chance)
        AskForInput()
        Input = GetInput()
        if CheckInput(Input):
            if MultipleSameInput(Input,alphabet_guess_already):
                print("{:^40s}".format("You have guess this alphabet already, please guess another alphabet"))
                continue
            elif Input =="hint":
                GiveHint(CurrentStatus,word)
                continue
            elif CorrectOrWrong(Input,word):
                print("{:^40s}".format("you guess the correct alphabet"))
                CurrentStatus,chance = UpdateVariable(Input,word,CurrentStatus,chance)
            else:
                print("{:^40s}".format("you guess the wrong alphabet"))
                CurrentStatus,chance = UpdateVariable(Input,word,CurrentStatus,chance)
            alphabet_guess_already = UpdateGuessWord(Input, alphabet_guess_already)
        else:
            print("{:^40s}".format("Please enter a alphabet only"))

        if Win(CurrentStatus,word):
            print("{:^40s}".format("you win!"))
            print("{:^40s}".format("the correct word is: "+"".join(word)))
            break
        elif Lose(chance):
            ShowGraphic(chance)
            print("{:^40s}".format("you lose"))
            print("{:^40s}".format("the correct word is: "+ "".join(word)))
            break

def PlayAgain():
    """ask if player wants to play again"""
    print("{:^40s}".format("Do you want to play again? y or n ?"))
    again = str(input("{:>20s}".format("")))
    again = again.lower()

    # when it is not the case that "y" XOR "n"
    while not ((again != "y" and again == "n") or (again == "y" and again != "n")):
        print("{:^40s}".format("Please enter y or n"))
        print("{:^40s}".format("Do you want to play again? y or n ?"))
        again = str(input("{:>20s}".format("")))
        again = again.lower()

    if again == "y":
        return True
    elif again == "n":
        return False

while True:
    game()
    if PlayAgain():
        continue
    else:
        print("{:^40s}".format("Thank For Playing!"))
        break
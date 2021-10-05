import random

Words_file = "words.txt"

def loadWords():
    print("Loading words...")
    inFile = open(Words_file, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(Secretword, guessedletter): 

    c=0
    for i in guessedletter:
        if i in Secretword:
            c+=1
    if c==len(Secretword):
        return True
    else:
        return False


def getGuessedWord(Secretword, guessedletter):
    s=[]
    for i in Secretword:
        if i in guessedletter:
            s.append(i)
    ans=''
    for i in Secretword:
        if i in s:
            ans+=i
        else:
            ans+='_ '
    return ans



def getAvailableLetters(guessedletter):
    import string
    ans=list(string.ascii_lowercase)
    for i in guessedletter:
        ans.remove(i)
    return ''.join(ans)

def hangman(Secretword):
    print("Welcome")
    print("Thinking of a word that is",len(Secretword),"letters long.")
    
    global guessedletter
    mistake=0
    guessedletter=[]
    
    while 6 - mistake > 0:
        
        if isWordGuessed(Secretword, guessedletter):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        else:
            print("-------------")
            print("You have",6-mistake,"guesses left.")
            print("Available letters:",getAvailableLetters(guessedletter))
            guess=str(input("Please guess a letter: ")).lower()
            
            if guess in guessedletter:
                print("Oops! You've already guessed that letter:",getGuessedWord(Secretword,guessedletter))
                
            elif guess in Secretword and guess not in guessedletter:
                guessedletter.append(guess)
                print("Good guess:",getGuessedWord(Secretword,guessedletter))
                
            else:
                guessedletter.append(guess)
                mistake += 1
                print("Oops! That letter is not in my word:",getGuessedWord(Secretword,guessedletter))
                
        if 6 - mistake == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.",Secretword)
            break
        
        else:
            continue


Secretword = chooseWord(wordlist).lower()
hangman(Secretword)
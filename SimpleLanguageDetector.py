import sys
import nltk, re, pprint
from nltk.corpus import udhr
from nltk import word_tokenize

# Helper Functions:
# Returns the name the language with the highest score
def findLang(Languages, langScores, langNames): # 
    maxVal = 0
    winner = "Couldn't Decide"
    for i in range(len(Languages)):
        if(langScores[i] > maxVal):
            maxVal = langScores[i] 
            winner = langNames[i]
    return winner

def scoreLangs(Languages, tokens, langScores):
    for token in tokens:
        for i in range(len(Languages)):
            if(token in Languages[i]):
                langScores[i] = langScores[i] + 1

def main():
################################### DATA #########################################    
    # Vocabularies
    Afrikaans = nltk.corpus.udhr.words('Afrikaans-Latin1')      
    Danish = nltk.corpus.udhr.words('Danish_Dansk-Latin1')      
    Dutch = nltk.corpus.udhr.words('Dutch_Nederlands-Latin1')   
    English = nltk.corpus.udhr.words('English-Latin1')
    French = nltk.corpus.udhr.words('French_Francais-Latin1')
    German = nltk.corpus.udhr.words('German_Deutsch-Latin1')
    Indonesian = nltk.corpus.udhr.words('Indonesian-Latin1')
    Italian = nltk.corpus.udhr.words('Italian-Latin1')
    Spanish = nltk.corpus.udhr.words('Spanish-Latin1')
    Swedish = nltk.corpus.udhr.words('Swedish_Svenska-Latin1')  

    # Should have made a language class but was lazy and had already wrote 
    #   them out as lists.
    Languages = [Afrikaans, Danish, Dutch, English, French, German, 
                    Indonesian, Italian, Spanish, Swedish]
    langNames = ["Afrikaans", "Danish", "Dutch", "English", "French", "German", 
                    "Indonesian", "Italian", "Spanish", "Swedish"]
    langScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

###################################################################################
############################### FUNCTION CALLS #################################### 
    # Takes input file (with no error handling), reads the file and puts in 'raw'.
    with open(sys.argv[1], 'r') as my_file:
        raw = my_file.read()

    # Tokenizes raw input file
    tokens = word_tokenize(raw)

    # Score each language
    scoreLangs(Languages, tokens, langScores)
    # Choose language based on score
    langChoice = findLang(Languages, langScores, langNames)
    print(langChoice)
###################################################################################
if __name__ == "__main__":
    main()


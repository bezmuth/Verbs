import time

def make_3gs_form(verb):
    verblength = int(len(verb) - 1) ##finds length of inputed word, min 1 because indexes
    if verb[verblength] == "y": ##if last leter is y
        newverb = verb[:verblength] ##newverb is now input except last letter
        newverb = newverb + "ies"
    elif verb[(verblength-1):(verblength+1)] == "ch" or verb[(verblength-1):(verblength+1)] == "sh" or verb[verblength] == "o" or verb[verblength] == "s" or verb[verblength] == "x" or verb[verblength] == "z": ##If the verb ends in o,ch,s,sh,x or z, add es
        newverb = verb + "es"
    else:
        newverb = verb + "s"
    return(newverb) ##output

def make_ing_form(verb):
    verblength = int(len(verb) - 1) ##finds length of inputed word, min 1 because indexes
    if verb[verblength] == "e":
        newverb = verb[:verblength]
        newverb = newverb + "ing"
    elif verb[verblength] == "ie":
        newverb = verb[:(verblength - 1)]
        newverb = verb + "ying"
    return(newverb)

mode = input("enter mode 1 or 2")
if mode == 1:
    verb = input("Enter verb to make plural ")
    verb = make_3gs_form(verb) ##sets verb equal to function
else:
    verb = input("Enter verb to make plural ")
    verb = make_ing_form(verb) ##sets verb equal to function
print(verb) ##prints output
time.sleep(4)

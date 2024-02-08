""" this code provides random sentences everytime"""


# for calling anything random
import random

# this code is for the main part as it determines whether the output is past or future or present
def main():
    sentence = make_sentence(1, "past")
    prepositional_phrase = get_prepositional_phrase()
    print(sentence +''+ prepositional_phrase)


def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    #picks a random word from the list 
    return word

def get_noun(quantity):

    # If quantity == 1 then it is a singular noun
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # If quantity  == 2 then it is a plural    
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):

    # Returns a randomly chosen verb if quantity is 1:

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

#Returns a randomly chosen word if quantity is 2:

    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]


    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond","by","despite","except","for","from","in","into","near","of","off","on","onto", "out","over","past","to","under","with","without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    noun = get_noun(quantity)
    prepositional_phrase = preposition + '' + noun
    return prepositional_phrase

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase()
    sentence = determiner + ' ' + noun + ' ' + verb + '' + prepositional_phrase + '.'
    return sentence.capitalize()


main()
#imports
import random
import time
f = open("/home/patrick/Documents/GitHub/Random-Python-Test-Game/words_alpha.txt", "r")
word_list2 = f.readlines()
word_list=[]




#setup
for a in word_list2:
	word_list.append(a.rstrip(a[-1]))
print(word_list)
print("Countdown")
listletters = []
print("Enter v or c")






#letter loop
for i in range (1, 10):
    vc = input()
    if vc == "v":
        vowel = random.randint(1, 5)
        if vowel == 1:
            nextletter = "a"
        elif vowel == 2:
            nextletter = "e"
        elif vowel == 3:
            nextletter = "i"
        elif vowel == 4:
            nextletter = "o"
        elif vowel == 5:
            nextletter = "u"
    elif vc == "c":
        vowel = random.randint(1, 21)
        if vowel == 1:
            nextletter = "b"
        elif vowel == 2:
            nextletter = "c"
        elif vowel == 3:
            nextletter = "d"
        elif vowel == 4:
            nextletter = "f"
        elif vowel == 5:
            nextletter = "g"
        elif vowel == 6:
            nextletter = "h"
        elif vowel == 7:
            nextletter = "j"
        elif vowel == 8:
            nextletter = "k"
        elif vowel == 9:
            nextletter = "l"
        elif vowel == 10:
            nextletter = "m"
        elif vowel == 11:
            nextletter = "n"
        elif vowel == 12:
            nextletter = "p"
        elif vowel == 13:
            nextletter = "q"
        elif vowel == 14:
            nextletter = "r"
        elif vowel == 15:
            nextletter = "s"
        elif vowel == 16:
            nextletter = "t"
        elif vowel == 17:
            nextletter = "v"
        elif vowel == 18:
            nextletter = "w"
        elif vowel == 19:
            nextletter = "x"
        elif vowel == 20:
            nextletter = "y"
        elif vowel == 21:
            nextletter = "z"
    listletters.append(nextletter)
    print(listletters)
    i = i + 1
print(listletters)


#functions
def check(word):
    if word in word_list:
    	print("OK")
    else:
    	print(word+" is an invalid word")
                                   
def word_input():
    wordtbchecked = input()
    check(wordtbchecked)
def countdown(t):
    while t > 0:
        print(listletters)
        print(t)
        t = t - 1
        time.sleep(1)
    print("Time is up")

#timer
print("Start")
countdown(2)
for i in range (1, 9):
    listletters.append("")
    i = i + 1

while True:
    wordtbchecked = input("Word: ")
    if wordtbchecked == ".":
        break
    check(wordtbchecked.lower())

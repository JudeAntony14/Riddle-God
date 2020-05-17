print('''
This riddle game is brought to you by Jude Antony Liju. In this game you have to answer 10 riddles one by one.
Good luck!
''')

riddle_1 = 'What can you catch but not throw?'
riddle_2 = 'What should be broken before using?'
riddle_3 = "What has 88 keys but can't open a single door"
riddle_4 = "What is so delicate that speaking a word can break it?"
riddle_5 = '''
There are two fathers and two sons in a car, but there are only three people in the car. 
Who are these three people?'''
riddle_6 = "Take my first letter, then my second, then the third, then all of my letters. I remain the same. Who am i?"
riddle_7 = "Which word's pronounciation remains the same even after you remove 4 or 5 letters?"
riddle_8 = "I am tall when i am young and i am short when i am old. What am i?"
riddle_9 = "What is full of holes but still holds water?"
riddle_10 = "What question can you never answer 'yes' to"

answer1 = 'cold'
answera = 'fire'

answer2 = 'egg'
answer3 = 'piano'
answer4 = 'silence'

answer5 = 'grandfather, father, son'
answere = 'grandfather father son'
answere1 = 'son, father, grandfather'
answere2 = 'son father grandfather'
answere3 = 'father son grandfather'
answere4 = 'father, son, grandfather'
answere5 = 'son, grandfather, father'
answere6 = 'son grandfather father'
answere7 = 'grandfather,father,son'

answer6 = 'postman'
answer7 = 'queue'
answer8 = 'candle'
answer9 = 'sponge'

answer10 = 'are you asleep?'
answer10a = 'are you asleep'
answer10b = 'are you sleeping?'
answer10c = 'are you sleeping'
answer10d = 'are you dead?'
answer10e = "are you dead"

tryagain = 'Try again'
chances = 0
limit = 200
score = 0

print(riddle_1)
while chances < limit:
    a = input("Answer: ")
    chances += 1
    if a == answer1 or answera:
        print("You got it! Let's see the next question.")
        score += 1
        break
    elif a != answer1:
        print(tryagain)
else:
    print("Sorry, the right answer is 'cold'.")


print(riddle_2)
while chances < limit:
    b = input("Answer: ")
    chances += 1
    if b == answer2:
        print("You got it! Let's see the next question.")
        score += 1
        break
    elif b != answer2:
        print(tryagain)
else:
    print("Sorry, the right answer is 'egg'.")


print(riddle_3)
while chances < limit:
    c = input("Answer: ")
    chances += 1
    if c == answer3:
        print("You got it! Let's see the next question.")
        score += 1
        break
    elif c != answer3:
        print(tryagain)
else:
    print("Sorry, the right answer is 'piano'.")


print(riddle_4)
while chances < limit:
    d = input("Answer: ")
    chances += 1
    if d == answer4:
        print("You got it! Let's see the next question.")
        score += 1
        break
    elif d != answer4:
        print(tryagain)
else:
    print("Sorry, the right answer is 'silence'.")


print(riddle_5)
while chances < limit:
    e = input('Answer: ')
    chances += 1
    if e == answer5 or answere or answere1 or answere2 or answere3 or answere4 or answere5 or answere6 or answere7:
        print("You got it! Let's see the next question.")
        score += 1
        break
    elif e != answer5:
        print(tryagain)
else:
    print("Sorry, the right answer is 'grandfather, father, son'.")


print(riddle_6)
while chances < limit:
    f = input("Answer: ")
    chances += 1
    if f == answer6:
        print("You got it! Let's see the next question.")
        score += 1
        break
    elif f != answer6:
        print(tryagain)
        break
else:
    print("Sorry, the right answer is 'postman'.")


print(riddle_7)
while chances < limit:
    g = input("Answer: ")
    chances += 1
    if g == answer7:
        print("You got it! Let's see the next question.")
        score += 1
        break
    elif g != answer7:
        print(tryagain)
else:
    print("Sorry, the right answer is 'queue'.")


print(riddle_8)
while chances < limit:
    h = input("Answer: ")
    chances += 1
    if h == answer8:
        print("You got it! Let's see the next question.")
        score += 1
        break
else:
    print("Sorry, the right answer is 'candle'.")


print(riddle_9)
while chances < limit:
    i = input("Answer: ")
    if i == answer9:
        print("You got it! Let's see the next question.")
        score += 1
        break
    elif i != answer9:
        print(tryagain)
else:
    print("Sorry, the right answer is 'sponge'.")


print(riddle_10)
while chances < limit:
    j = input("Answer: ")
    if j == answer10 or answer10a or answer10b or answer10c or answer10d or answer10e:
        print('''
You got it!.
You have completed the quiz!
Congragulations!
''')
        score += 1
        break
    elif j != answer10 or answer10a or answer10b or answer10c or answer10d or answer10e:
        print(tryagain)

else:
    print("Sorry, the right answer is 'are you asleep?'.")
    print('Congragulations you have completed the quiz!')

print("Your score is:")
print(score)

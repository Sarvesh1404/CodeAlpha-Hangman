import random
words=['apple','potato','banana']
lives=6
chosen_word=random.choice(words)


display=[]
for i in range(len(chosen_word)):
    display +="_"
print(display)
game_over=False

while not game_over:
    Guessed=input("Guess a letter:")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==Guessed:
            display[position]=Guessed
    print(display)

    if Guessed not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose!!!")
    if '_' not in display:
        game_over=True
        print("You won!!!")

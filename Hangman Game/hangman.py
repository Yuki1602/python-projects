import random

word=['python', 'java', 'kotlin', 'javascript']

correct_choice = random.choice(word)
Temp = 0
joined_list = ""
count = 0
print("H A N G M A N")
word_so_far = ("-" * len(correct_choice))
list_word_so_far = list(word_so_far)
list_correct_choice = list(correct_choice)
same = set()

while True:
    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu == "play":
        while count < 8:
            print()
            print(joined_list.join(list_word_so_far))
            if list_correct_choice != list_word_so_far:
                letter = input("Input a letter: ")

            if letter in correct_choice and letter not in list_word_so_far:
                for i in range(len(correct_choice)):
                    if correct_choice[i] == letter:
                        list_word_so_far[i] = letter

            elif len(letter) != 1:
                print("You should print a single letter")

            elif list_correct_choice == list_word_so_far:
                print("""You guessed the word!
        You survived!""")
                Temp = 3
                break

            elif not letter.islower():
                print("It is not an ASCII lowercase letter .")

            elif letter in same:
                print("You already typed this letter ")

            elif letter not in correct_choice:
                print("No such letter in the word")
                Temp = 1
                count += 1
            same.add(letter)

        if Temp==1 or Temp==2:
            print("You are hanged!")
            print()
    elif menu == "exit":
        quit()
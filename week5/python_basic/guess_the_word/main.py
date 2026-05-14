import random

def get_a_number():
    while True:
        num = input("How many rounds do you want to play: ")
        if chacks_number(num):
            return int(num)


def chacks_number(num):
    try:
        return int(num)
    except:
        print("Please enter a valid number...")


def hide_word(len):
    return "#" * len


def get_a_letter():
    while True:
        char = input("Please guess one letter (or quit to exit): ").lower()
        if char == "quit":
            exit()
        if checks_alpha(char):
            return char
        else:
            print("You must enter ONE valid letter...")


def checks_alpha(letter):
    return letter.isalpha() and letter.isascii() and (len(letter) == 1)


def show_status(inputed_letters, hidden_word, guess_times, points):
    print(f"""\n
       ---- HERE IS YOUR STATUS FOR NOW ----
          You already have {points} points
    You already used this letters {inputed_letters}
          The hidden eord is: {hidden_word}
         Left you {guess_times} times to try
      --------------- GOOD LUCK ---------------\n""")


def print_categories(words_dict):
    for category in words_dict.keys():
        print(category, end=" | ")

def main():
    print("""
================================================
                GUESS THE WORD
================================================
""")
    points = 0

    WORDS_DICT = {
                    "animals": [
                        "monkey", "rabbit", "tiger", "turtle", "spider", 
                        "dolphin", "penguin", "lizard", "giraffe", "hamster"
                    ],
                    "foods": [
                        "burger", "cheese", "pizza", "noodle", "yogurt", 
                        "chicken", "pancake", "banana", "garlic", "cookie"
                    ],
                    "countries": [
                        "israel", "brazil", "france", "canada", "mexico", 
                        "norway", "germany", "vietnam", "poland", "greece"
                    ],
                    "names": [
                        "oliver", "sophia", "thomas", "daniel", "arthur", 
                        "joseph", "samuel", "hannah", "claire", "nathan"
                    ],
                    "furniture": [
                        "cabinet", "shelves", "dresser", "mirror", "drawer", 
                        "table", "armchair", "bench", "closet", "counter"
                    ]
                }
    
    print_categories(WORDS_DICT)
    while True:
        category = input("\nChoose a category: ")
        if category in WORDS_DICT:
            break
        print(f"Category {category} not found...")
    
    rounds = get_a_number()


    current_word = random.choice(WORDS_DICT[category])
    print(current_word)

    hidden_word = hide_word(len(current_word))

    ATTEMPTS = round(len(hidden_word) * 1.5)

    inputed_letters = []

    while True:
        show_status(inputed_letters, hidden_word, ATTEMPTS, points)

        users_guess = get_a_letter()

        if users_guess in current_word:
            for i, v in enumerate(current_word):
                if v == users_guess:
                    points += 1
                    tmp_word = list(hidden_word)
                    tmp_word[i] = v
                    hidden_word = "".join(tmp_word)
        else:
            inputed_letters.append(users_guess)
            ATTEMPTS -= 1
            print("\nDon't give up!")

        
        if hidden_word == current_word or ATTEMPTS == 0:
            if ATTEMPTS > 0:
                print("Yayyyy!!!\nYou are a winner!!!")
            else:
                print("Don't give up, maybe next time...")
            print(f"The hidden word was: {current_word}")
            rounds -= 1
            if not rounds:
                break
            current_word = random.choice(WORDS_DICT[category])
            print(current_word)

            hidden_word = hide_word(len(current_word))

            ATTEMPTS = round(len(hidden_word) * 1.5)

            inputed_letters = []


if __name__ == "__main__":
    main()
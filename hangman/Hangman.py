import random

with open("words.txt", "r") as file:
    words = file.read()
words = words.split()
word = random.choice(words)

def hangman(counter):
    if counter == 1:
        return r"""
        _______
        |       |
        |       O  
        |       
        |       
        |___
        """
    elif counter == 2:
        return r"""
        _______
        |       |
        |       O   
        |       |   
        |       
        |___
        """
    elif counter == 3:
        return r"""
        _______
        |       |
        |       O  
        |      /|  
        |       
        |___
        """
    elif counter == 4:
        return r"""
        _______
        |       |
        |       O   
        |      /|\  
        |       
        |___
        """
    elif counter == 5:
        return r"""
        _______
        |       |
        |       O 
        |      /|\
        |      / 
        |___
        """
    elif counter == 6:
        return r"""
        _______
        |       |
        |       O
        |      /|\
        |      / \
        |___
        """
    else:
        return "This can't be executed"

def main(word):
    counter = 0
    print(f"Your word is: {'_ ' * len(word)}")
    wordi = list("_" * len(word))
    while counter != 6:
        guessed_word = input("Enter your choice: ")
        if len(guessed_word) > 1:
            print("Only a single letter")
            continue

        found = False
        for i in range(len(word)):
            if guessed_word.lower() == word[i].lower():
                wordi[i] = guessed_word
                found = True

        if found:
            g = ''.join(wordi)
            print(" ".join(wordi))
            if g == word:
                print("YAY you got it")
                break
        else:
            print(f"Oops, {guessed_word} not in word")
            counter += 1
            print(hangman(counter))

    if counter == 6:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    main(word)
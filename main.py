import random
import string


def main():
    print('H A N G M A N')
    won = 0
    lost = 0
    while True:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        user_input = input()
        if user_input == 'play':
            won, lost = game(won, lost)
        elif user_input == 'results':
            print(f'You won: {won} times.\nYou lost: {lost} times.')
        elif user_input == 'exit':
            break


def game(won=0, lost=0):
    words_list = ['python', 'java', 'swift', 'javascript']
    computer_input = random.choice(words_list)
    number_of_tries = 8
    # computer_input = 'java'
    state_word = '-' * len(computer_input)
    alphabet = string.ascii_lowercase
    guess_letters = set()

    while number_of_tries > 0:
        hat_print = f"\n{state_word}\nInput a letter:"
        print(hat_print)
        user_input = input()
        if len(user_input) != 1:
            print('Please, input a single letter.')
            continue
        elif user_input not in alphabet:
            print('Please, enter a lowercase letter from the English alphabet.')
            continue
        elif user_input in guess_letters:
            print("You've already guessed this letter.")
            continue
        else:
            guess_letters.add(user_input)

        if user_input in computer_input:
            state_word = ''.join(
                [computer_input[i] if computer_input.startswith(user_input, i) else state_word[i] for i in
                 range(len(computer_input))]
                )
            if state_word == computer_input:
                print(f'You guessed the word {computer_input}!\nYou survived!')
                won += 1
                break
        else:
            if number_of_tries > 1:
                print(hat_print + "\nThat letter doesn't appear in the word.")
            number_of_tries -= 1
    else:
        print('\nYou lost!')
        lost += 1
    return won, lost


if __name__ == '__main__':
    main()

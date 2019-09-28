import random

def hangman():
    """
    Elementary form of Hangman. Two options: A) Another user (Player 1) enters a word
    B) Uses four preselected words
    String -> String
    Convert the string into a list than alter the values accordingly
    And end up printing a string 'You win' or 'You loose'
    """
    guess = ""
#     answer = input('Player 1 enter a word: ') Adjustable to the input of another user
    words = ["dog","cat","bird","owl"]
    answer = words[random.randrange(0,3)]
    location_of_guess = 0
    real_answer = list(answer)
#   num_guesses = 2 * len(answe)
    num_guesses = 10
    while num_guesses > 0:
        guess = input("Please guess a letter: ")
        #list(answer)
        #num_guesses = len(answer)
        if guess in real_answer:
            location_of_guess = real_answer.index(guess)
            del(real_answer[location_of_guess])
            print('Correct')
            num_guesses -=1
            if len(real_answer) == 0:
                print("You Won!")
                break
        else:
            num_guesses -= 1
            print("Please try again. Guesses Remaining: ", num_guesses)
            if num_guesses == 0:
                print('You lost!')

hangman()
import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    x = random.randint(0,len(word)-1)#random word generator?
    new_word = ""
    for r in range(0,len(word)):
        if r != x:
            new_word += "_"
        else:
            new_word += word[r]
    return new_word	

# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    origin_char_count = 0
    for index in range(0, len(original_word)):
        if char == original_word[index]:
            origin_char_count = origin_char_count + 1

    answer_char_count = 0
    for index in range(0, len(original_word)):
        if char == answer_word[index]:
            answer_char_count  = answer_char_count  + 1

        result = answer_char_count < origin_char_count
    return result
# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    missing_char = "" 
    char_count = 0
    #x = random.randint(0,len(word)-1)#random word generator?
    for r in range(0,len(original_word)):
        if char == original_word[r] or original_word[r] == answer_word[r]:
            missing_char += original_word[r]
        else:
            missing_char += "_"
    return missing_char

  
def do_correct_answer(original_word, answer, guess):
    result = fill_in_char(original_word, answer, guess)
    print(result)
    return result

# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))# number of guesses decreasing by one
    draw_figure(number_guesses )


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("/----\n|\n|\n|\n|\n_______")

    elif number_guesses == 3:
        print("/----\n|   0\n|\n|\n|\n_______")

    elif  number_guesses == 2:
        print("/----\n|   0\n|  /|\\\n|\n|\n_______")

        
    elif  number_guesses == 1:
        print("/----\n|   0\n|  /|\\\n|   |\n|\n|\n_______")
        
    else:
        print("/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______")
               
# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    number_guesses = 5
    while word != answer:
        guess = get_user_input()
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)

        elif guess == 'exit' or guess == 'quit':
            print("Bye!")
            break

        
        elif not is_missing_char(word, answer, guess):
            number_guesses -= 1
            do_wrong_answer(answer, number_guesses)

        if  number_guesses == 0:
            print(f"Sorry, you are out of guesses. The word was: {word}")
            break

           

        
    
   

# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)


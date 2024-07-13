# << Challenge >>
# Catch the KeyError when a user enters a character that is not in the dictionary.
# Provide feedback to the user when an illegal word was entered.
# Continue prompting the user to enter another word until they enter a valid word.

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic() # 프로그램이 예외발생 시 그대로 끝나지 않고 다시 함수 실행.
    else:
        print(output_list)

generate_phonetic()

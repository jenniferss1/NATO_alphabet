import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

result = {row.letter: row.code for index, row in data.iterrows()}

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_code_words = [result[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letter are allowed.")
        generate_phonetic()
    else:
        print(phonetic_code_words)

generate_phonetic()
import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

result = {row.letter: row.code for index, row in data.iterrows()}

user_input = input("Enter a word: ").upper()

phonetic_code_words = [result[letter] for letter in user_input if letter in result]

print(phonetic_code_words)

import pandas
NATO_FILE = 'Day26/nato_project/nato_phonetic_alphabet.csv'


nato_data = pandas.read_csv(NATO_FILE)
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()} 

input_word = input("Please enter a word to translate: ")
print([nato_dict[letter.upper()] for letter in input_word])
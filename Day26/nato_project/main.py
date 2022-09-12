import pandas
NATO_FILE = 'Day26/nato_project/nato_phonetic_alphabet.csv'


nato_data = pandas.read_csv(NATO_FILE)
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()} 
while True:
    input_word = input("Please enter a word to translate: ")
    try:
        print([nato_dict[letter.upper()] for letter in input_word])
    except TypeError as error_message:
        print("Sorry, only letters in the alphabet please.")

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open('Day24/Input/Letters/starting_letter.txt') as starting:
    template_letter = starting.read()
with open('Day24/Input/Names/invited_names.txt') as names:
    for name in names.readlines():
        name=name.strip()
        letter = template_letter.replace('[name]', name)
        letter_name = f'letter_for_{name}'
        with open(f'Day24/Output/ReadyToSend/{letter_name}', mode="w") as letter_to_send:
            letter_to_send.write(letter)

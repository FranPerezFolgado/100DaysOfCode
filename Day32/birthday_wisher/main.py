##################### Extra Hard Starting Project ######################
import smtplib
import pandas, os, random
import datetime as dt
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
MY_EMAIL = 'franperezfolgado@outlook.com'
PASSWORD = 'placeholder'
SMTP = 'outlook.office365.com'
TEMPLATE_PATH = 'Day32/birthday_wisher/letter_templates'
TEMPLATE_MAIL = 'Subject:Happy Birthday!\n\n'

now = dt.datetime.now()
day = now.day
month = now.month

import os, random
letter_file = random.choice(os.listdir(TEMPLATE_PATH))


try:
    birthdays = pandas.read_csv('Day32/birthday_wisher/birthdays.csv')
except FileNotFoundError:
    print("The csv file doesn't exists")

birthdays_dict = {(): data_row for (index, data_row) in birthdays.iterrows()}

for index, data in birthdays.iterrows():
    if month == data['month'] and day == data['day']:
        print(f"Today is {data['name']}'s birthday!")
        letter_content = ''
        try:
            with open(f'{TEMPLATE_PATH}/{letter_file}') as letter:
                letter_content = letter.read()
        except FileNotFoundError:
            print(f"The letter file doesn't exists. {letter_file}")
        else:
            letter_content = letter_content.replace('[NAME]', data['name'])
        
        try:
            with smtplib.SMTP(SMTP) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=data['email'], msg=f'{TEMPLATE_MAIL}{letter_content}')
        except smtplib.SMTPException:
            print('Error sending email')

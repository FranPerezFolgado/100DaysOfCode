import smtplib
import datetime as dt
from random import choice

'''
my_email = 'franperezfolgado@outlook.com'
email_to = 'pandacabezabuque@gmail.com'
password= '773oLbyXQCVD^R'
msg = f'From: {my_email}\r\nTo: {email_to}\r\n\r\nHello'
msg_subject = f'Subject:Hello\n\nBody'
connection = smtplib.SMTP('outlook.office365.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=email_to, msg=msg_subject)
connection.close()


now = dt.datetime.now()
print(now.year)
'''


date_now = dt.datetime.now()
weekday = date_now.weekday()
if 3 == weekday:
    quotes_list = []
    try:
        with open('Day32/quotes.txt', 'r') as quotes:
            quotes_list = quotes.readlines()
    except FileNotFoundError:
        print('The file does not exist')
    else:
        print(quotes_list)
    try:
        my_email = 'franperezfolgado@outlook.com'
        email_to = 'pandacabezabuque@gmail.com'
        password= '773oLbyXQCVD^R'
        msg_subject = f'Subject:Motivational Quote\n\n{choice(quotes_list)}'
        connection = smtplib.SMTP('outlook.office365.com')
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email_to, msg=msg_subject)
    except Exception:
        print('Error sending email')
    finally:
        connection.close()
import requests
import smtplib
from bs4 import BeautifulSoup
import time

# set the URL of the page to monitor
url = 'https://www.looperman.com/loops'

# set the email addresses
sender_email = 'baitofclick@gmail.com'
sender_password = 'fuckoff6'
receiver_email = 'prodbyjod@gmail.com'

# initialize the previous state to None
previous_state = None

# function to check the loops page
def check_loops():
    global previous_state
    # get the page HTML
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # get the number of loops
    num_loops = int(soup.find('span', {'id': 'navLoopsCount'}).text.replace(',', ''))
    # get the loop table
    loop_table = soup.find('table', {'class': 'table'})
    # get the current state
    current_state = (num_loops, hash(str(loop_table)))
    # compare the current state to the previous state
    if previous_state is not None and current_state != previous_state:
        # send an email
        send_email()
    # update the previous state
    previous_state = current_state

# function to send an email notification
def send_email():
    # set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # log in to the account
    server.login(sender_email, sender_password)
    # compose the email
    subject = 'Looperman Loops Page Updated!'
    body = 'The Looperman loops page has been updated.'
    message = f'Subject: {subject}\n\n{body}'
    # send the email
    server.sendmail(sender_email, receiver_email, message)
    # log out of the account
    server.quit()

# run the loop checker every 5 minutes
while True:
    check_loops()
    time.sleep(300)

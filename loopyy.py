import requests
import smtplib
import time
from datetime import datetime

# email information
email = 'tempname1@email.com'
password = 'Finten33!'
to_email = 'prodbyjod@gmail.com'

# function to send email notification
def send_email():
    subject = 'Looperman.com Loops Review Started'
    body = 'The admins have started uploading loops for review on Looperman.com/loops'
    message = f'Subject: {subject}\n\n{body}'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, to_email, message)
    server.quit()

# loop to check site every 5 minutes between 8am-4pm BST
while True:
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    if current_time >= '08:00:00' and current_time <= '16:00:00':
        try:
            url = 'https://www.looperman.com/loops'
            response = requests.get(url)
            if response.status_code == 200 and 'Upload your loops' in response.text:
                send_email()
                break
        except:
            pass
    time.sleep(300)

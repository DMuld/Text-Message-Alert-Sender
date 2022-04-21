phrase = "Spam Bot"

print(phrase)

import random
import smtplib
from email.message import EmailMessage

randnum = random.randint(1,100)

with open ("100BibleQuotes.txt", 'r', encoding="utf8", errors="ignore") as file:         #might need to put it in the same directory as this file.
    output2 = file.readlines()
    output = output2[randnum]
    file.close()
    pass
print(output)


def email_Alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "*Enter Email Address*"                #the name of the email address
    msg['from'] = user
    password = "*Enter Machine Passowrd*"                               #password of the email address // has to have 2 step verification and the app password entered.

    server = smtplib.SMTP("smtp.gmail.com", 587)                #this is gmails name and port
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

email_Alert("Quote Of The Day", output, "*Enter Phone Number*@vtext.com")
email_Alert("", "Reply Stop, to opt out of automated messages.", "*Enter Phone Number*@vtext.com")
#email_Alert("Quote Of The Day", output, "*Enter Phone Number*@messaging.sprintpcs.com")
#email_Alert("Quote Of The Day", output, "*Enter Phone Number*@tmomail.net")               #change this to the email that it is wished to be sent. Can also be numbers this is specifically for Verizon
print(phrase.replace("Bot", "Completed"))                                             #@messaging.sprintpcs.com  @vtext.com  @tmomail.net
input("Enter anything to exit:")

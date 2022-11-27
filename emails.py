import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Johnny Sin'
email['to'] = 'sinner.johnny@gmail.com'
email['subject'] = 'Congratulations you won a billion won!'

email.set_content(  # we can add more than just text!
    'I am a Python Master'
)
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # says hello to the smtp server
    smtp.starttls()  # tls is an encryption mechanism to connect securely
    # to the server
    smtp.login('johnnysinspam@gmail.com', 'JohnnySpam')
    smtp.send_message(email)
    print('all good boss!')

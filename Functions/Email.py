import yagmail

# Sending Email
body = 'hello world'
subject = 'test'
email = 'alex27dz@gmail.com'


def send_email(email, subject, body):
    ya_email = yagmail.SMTP('alex27dz@gmail.com', 'yeqnnbfgkfetetcr')
    ya_email.send(email, subject, body)
    print('email sent')


send_email(email, subject, body)

'''
Adding image in the body of the email, you need to use yagmail.inline:
import yagmail
yag = yagmail.SMTP(‘YOUR_EMAIL@gmail.com’, ‘YOUR_PASSWORD’)
contents = [“Some Text”, yagmail.inline( full_path_to_image )]
yag.send(send_to, subject, contents)
yag = yagmail.SMTP(‘YOUR_EMAIL@gmail.com’, ‘YOUR_PASSWORD’)
contents = [“Some Text”, yagmail.inline( full_path_to_image )]
yag.send(send_to, subject, contents)
'''


from email.mime.text import MIMEText
import smtplib
def send_email(X,Y,X1,Y1,holder_name,location,email):
    from_email="antitrafficking23@gmail.com"
    from_password="abcd1234!@#$"
    to_email=email

    subject="DNA Record"
    message="Your Data Has Been Recorded successfully. X is <strong>%s</strong>.<br> Y is <strong>%s</strong>.<br> X1 is <strong>%s</strong>.<br> Y1 is <strong>%s</strong>." % (X,Y,X1,Y1)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)

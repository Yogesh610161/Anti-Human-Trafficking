from email.mime.text import MIMEText
import smtplib
def send_email1(vari,email1,vari1,vari2,vari3,vari4):
    from_email="antitrafficking23@gmail.com"
    from_password="abcd1234!@#$"
    to_email=email1

    subject="DNA Result"
    message="DATA FOUND"
    message=" Y is <strong> %s</strong>.<br>X1 is <strong>%s</strong>.<br>Y1 is <strong>%s</strong>.<br>Location is <strong>%s</strong>.<br> Holder Name is <strong>%s</strong>." %(vari,vari2,vari3,vari1,vari4)


    msg1=MIMEText(message,'html')
    msg1['Subject']=subject
    msg1['To']=to_email
    msg1['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg1)

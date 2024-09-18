import smtplib, ssl
def send_email():
    host = "smtp.gmail.com"
    port = 465

    username = "sindumindu8@gmail.com"
    password ="Password@123"

    receiver = "sindumindu8@gmail.com"

    context = ssl.create_default_context()

    message ="""
    Hii
    How are you?
    """
    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

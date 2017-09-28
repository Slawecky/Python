import smtplib
from Day_8 import secrets

adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

mailer = smtplib.SMTP("smtp.gmail.com", 587)

mailer.ehlo()
mailer.starttls()

mailer.login(nadawca, haslo)

temat = "Temat : Hi co tam ?\n"
wiadomosc = "Hello hi"
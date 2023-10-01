import os
from decouple import config
import smtplib
import ssl
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def mailSender():
    email_sender = config('EMAIL_SENDER')
    email_password = config('EMAIL_PASSWORD')
    email_receiver = config('EMAIL_RECEIVER')

    subject = f'Job Alert from Indeed and LinkedIn - {datetime.datetime.now().strftime("%Y-%m-%d")}'
    body = 'Please find the attached files for the job alert from Indeed and LinkedIn.'

    email = MIMEMultipart()
    email['From'] = email_sender
    email['To'] = email_receiver
    email['Subject'] = subject
    email.attach(MIMEText(body, 'plain'))

    # Attach the CSV file
    csv_filename = f'jobs_{datetime.datetime.now().strftime("%Y-%m-%d")}.csv'
    csv_attachment = open(csv_filename, 'rb')
    csv_part = MIMEBase('application', 'octet-stream')
    csv_part.set_payload((csv_attachment).read())
    encoders.encode_base64(csv_part)
    csv_part.add_header('Content-Disposition', f'attachment; filename={csv_filename}')
    email.attach(csv_part)

    # Attach the Excel file
    excel_filename = f'jobs_{datetime.datetime.now().strftime("%Y-%m-%d")}.xlsx'
    excel_attachment = open(excel_filename, 'rb')
    excel_part = MIMEBase('application', 'octet-stream')
    excel_part.set_payload((excel_attachment).read())
    encoders.encode_base64(excel_part)
    excel_part.add_header('Content-Disposition', f'attachment; filename={excel_filename}')
    email.attach(excel_part)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, email.as_string())
        smtp.quit()
    try:
        os.remove(f'jobs_{datetime.datetime.now().strftime("%Y-%m-%d")}.csv')
        os.remove(f'jobs_{datetime.datetime.now().strftime("%Y-%m-%d")}.xlsx')
        print(f"csv and xlsx file successfully deleted.")
    except FileNotFoundError:
        print(f"Not found. Unable to delete.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
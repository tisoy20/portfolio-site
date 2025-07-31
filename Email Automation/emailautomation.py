import smtplib  # Import the library to send emails using SMTP
from email.message import EmailMessage  # Import the class to create email messages
import pandas as pd  # Import pandas to read spreadsheet data
import schedule  # Import schedule to run tasks at specific times
import time  # Import time to pause between checks

def send_email(subject, body, to, attachment_path=None):
    msg = EmailMessage()  # Create a new email message object
    msg['Subject'] = subject  # Set the subject of the email
    msg['From'] = 'your_email@gmail.com'  # Set the sender's email address (replace with your email)
    msg['To'] = to  # Set the recipient's email address
    msg.set_content(body)  # Set the main text content of the email

    if attachment_path:  # If there is an attachment file path provided
        with open(attachment_path, 'rb') as f:  # Open the file in binary mode
            file_data = f.read()  # Read the file data
            file_name = f.name  # Get the file name
        # Attach the file to the email
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Connect to Gmail's SMTP server securely
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your_email@gmail.com', 'your_app_password')  # Log in with your email and app password
        smtp.send_message(msg)  # Send the email message

def send_emails_from_spreadsheet(spreadsheet_path):
    # Read the spreadsheet file (Excel) into a pandas DataFrame
    df = pd.read_excel(spreadsheet_path)
    # Loop through each row in the spreadsheet
    for _, row in df.iterrows():
        name = row['Name']  # Get the recipient's name from the row
        email = row['Email']  # Get the recipient's email address
        message = row['Message']  # Get the message content
        attachment = row.get('Attachment', None)  # Get the attachment file path (if any)
        # Create a personalized message body
        personalized_body = f"Hi {name},\n\n{message}\n\nBest regards,\nYour Name"
        # Send the email with the personalized body and optional attachment
        send_email(
            subject="Personalized Message",  # Set the email subject
            body=personalized_body,  # Set the email body
            to=email,  # Set the recipient's email
            attachment_path=attachment if pd.notna(attachment) else None  # Attach file if provided
        )

def job():
    # This function will be scheduled to run at a specific time
    send_emails_from_spreadsheet('recipients.xlsx')  # Send emails using data from the spreadsheet

schedule.every().day.at("08:00").do(job)  # Schedule the job to run every day at 8:00 AM

while True:  # Infinite loop to keep the script running
    schedule.run_pending()  # Run any scheduled jobs that are ready
    time.sleep(60)  # Wait for 60 seconds before checking again
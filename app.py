import smtplib
import csv
import time
from email.message import EmailMessage
from config import EMAIL, APP_PASS
from utilis import unique_emails


EMAIL = EMAIL
APP_PASSWORD = APP_PASS
FILE_NAME="Email.csv"
SUBJECT = "Singing Bowl Product Presentation"

unique_emails(FILE_NAME)
BODY = """
Hello,
We would like to introduce our Singing Bowl products.
Please find the attached presentation for more details regarding designs, pricing, and export opportunities.
Thank you for your time and consideration.
Best regards
"""

ATTACHMENT_PATH = "presentation.pptx"

emails = []

with open(FILE_NAME, "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        emails.append(row[0])

success_count = 0
failed_count = 0

successful_emails = []
failed_emails = []

smtp = smtplib.SMTP_SSL(
    "smtp.gmail.com",
    465
)

smtp.login(EMAIL, APP_PASSWORD)

for receiver in emails:

    try:
        msg = EmailMessage()

        msg["Subject"] = SUBJECT
        msg["From"] = EMAIL
        msg["To"] = receiver

        msg.set_content(BODY)

        with open(ATTACHMENT_PATH, "rb") as f:
            file_data = f.read()

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.presentationml.presentation",
            filename="presentation.pptx"
        )

        smtp.send_message(msg)

        print(f"Sent to: {receiver}")

        success_count += 1
        successful_emails.append(receiver)

        time.sleep(5)

    except Exception as e:

        print(f"Failed: {receiver}")
        print(e)

        failed_count += 1
        failed_emails.append(receiver)

smtp.quit()

print("\n========== REPORT ==========")

print(f"Total Emails: {len(emails)}")
print(f"Successful: {success_count}")
print(f"Failed: {failed_count}")

print("\nSuccessful Emails:")
for email in successful_emails:
    print(email)

print("\nFailed Emails:")
for email in failed_emails:
    print(email)

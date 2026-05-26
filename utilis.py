import csv
emails = set()
def unique_emails(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row: 
                email = row[0].strip()
                if email:
                    emails.add(email.lower())

    with open(
        FILE_NAME,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        for email in sorted(emails):
            writer.writerow([email])

    print("Unique emails saved!")
    print(f"Total Unique Emails: {len(emails)}")

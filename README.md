# Singing-Bowl-Email-Automation-System
A lightweight Python script for sending bulk personalized emails with a PowerPoint attachment via Gmail's SMTP server. Originally built to distribute a Singing Bowl product presentation to a list of business contacts, but easily adaptable for any bulk email campaign.
Features:
-> CSV-based recipient list — reads email addresses from a .csv file for easy management
-> Duplicate filtering — calls a unique_emails() utility before sending to eliminate duplicate recipients
-> PPTX attachment support — attaches any .pptx file using the correct MIME type
-> Rate limiting — a configurable time.sleep() delay between sends reduces the risk of Gmail flagging your account for spam
-> Session reuse — opens a single SMTP_SSL session for all emails rather than reconnecting per recipient, improving speed and reliability
-> Detailed reporting — prints a final summary showing total, successful, and failed email counts along with per-category recipient lists

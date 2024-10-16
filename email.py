import imaplib

def check_email():
    # Connect to the email server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")  # Change this if using a different provider
    mail.login("your_email@gmail.com", "your_email_password")  # Modify your credentials accordingly

    # This is the route for the email folder that you intend to check
    mail.select("Completed")  # Folder name should match eaxctly

    # Searching operation in provided folder
    status, messages = mail.search(None, 'SUBJECT "PROJECT-Completed"')

    # If no messages, return False
    if messages[0] == b'':
        return False
    return True

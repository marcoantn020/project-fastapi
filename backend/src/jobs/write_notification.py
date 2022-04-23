
def write_notification(email: str, message: str = ''):
    with open('log.txt', mode='a') as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)

def validate_email(email):
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(email_pattern, email):
        return True
    else:
        return False

def validate_sdt (sdt):
    if not sdt.isdigit 
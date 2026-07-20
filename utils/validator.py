def validate_marks(mark):
    if not (isinstance(mark, (int, float)) and not isinstance(mark, bool)):
        raise ValueError("Mark must be a valid number.")
    if not 0 <= mark <= 100:
        raise ValueError("Mark should be between 0 to 100 only\n")
    
    smark = str(mark)
    if not smark.strip() or " " in smark:
        raise ValueError("Mark cannot be empty or contain spaces.")

    return mark


def validate_year(year):
    if not (isinstance(year, int) and not isinstance(year, bool)):
        raise ValueError("Year must be an integer.")
    if not 1 <= year <= 4:
        raise ValueError("Year should be in between 1 to 4 only ")
    
    syear = str(year)
    if not syear.isnumeric() or " " in syear:
        raise ValueError("Year must contain only digits and no spaces.")

    return year


def validate_phone(num): 
    snum = str(num)
    if len(snum) != 10 or not snum.isnumeric():
        raise ValueError("Phone number should have 10 digits without +91")
    return num


def validate_email(email):
    check_mail = ("@gmail.com", "@outlook.com", "@yahoo.com")
    if not email.endswith(check_mail):
        raise ValueError(f"Email should contain any of these {check_mail}")
    return email


def validate_roll_no(rollnum):
    temp = str(rollnum).upper()

    if not temp.strip() or " " in temp:
        raise ValueError("Roll Num cannot be empty or contain spaces.")

    for char in temp:
        if not (char.isalnum() or char in ("-", "/")):
            raise ValueError("Roll Num can only contain numbers, letters, '-', and '/'")

    return temp


def validate_name(name):
    sname = str(name).strip()
    if not sname:
        raise ValueError("Name cannot be empty.")

    for char in sname:
        if not (char.isalpha() or char in (" ", ".")):
            raise ValueError("Name cannot contain numbers or special characters.")

    return name


def validate_department(dept):
    sdept = str(dept).strip()
    if not sdept:
        raise ValueError("Department cannot be empty.")

    for char in sdept:
        if not (char.isalpha() or char in (" ", "-", "/", "&")):
            raise ValueError("Department cannot contain numbers or special haracters.")

    return dept


def validate_section(sec):
    ssec = str(sec).strip()
    if not ssec:
        raise ValueError("Section cannot be empty.")

    for char in ssec:
        if not (char.isalnum() or char in ("-", "/")):
            raise ValueError("Section cannot contain special characters.")

    return sec
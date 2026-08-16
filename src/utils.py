def ask_to_continue():
    """Ask the user to continue and return True or False based on their input."""

    LoopExit = False
    while True:
        ch = input("Enter(Y/N): ")
        if len(ch) == 1 and ch in "YyNn":
            if ch.upper() == "N":
                return not (LoopExit)
            else:
                break
        else:
            print("Please Enter only(Y/N).")


def validate_email(email):
    """To validate an email address."""

    if "@" in email and "." in email:
        if len(email.split("@")[0]) < 4 or len(email.split("@")[1]) < 3:
            return False
        else:
            return True
    else:
        return False


def validate_password(passwd):
    """For passsword validation"""
    
    l = u = d = s = 0  # lowercase, uppercase, digit, specialchr respectively.
    if len(passwd) <= 8 and len(passwd) >= 20:
        return False
    else:
        for i in passwd:
            if i.isalpha():
                if i.islower():
                    l += 1
                else:
                    u += 1
            elif i.isdigit():
                d += 1
            else:
                s += 1

        if l >= 1 and u >= 1 and d >= 1 and s >= 1:
            return True
        else:
            return False

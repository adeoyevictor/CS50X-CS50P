from datetime import date, timedelta
import re
import sys
import inflect

p = inflect.engine()


def main():
    dob = input("Date of birth: ")
    if check_format(dob):
        dob= date.fromisoformat(dob)
        today = date.today()
        days = (today - dob).days
        mins = days * 24 * 60
        mins = p.number_to_words(mins, andword="").capitalize()
        print(f"{mins} minutes")
    else:
        sys.exit("Invalid Date")


def check_format(d):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", d, re.IGNORECASE):
        return True
    return False

if __name__ == "__main__":
    main()
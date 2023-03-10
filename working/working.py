import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9]{1,2}:?(?:[0-9]{2})? (?:AM|PM)) to ([0-9]{1,2}:?(?:[0-9]{2})? (?:AM|PM))$", s):
        start, stop = matches.groups()
        if check_valid_time(start) and check_valid_time(stop):
            start = convert_valid_time(start)
            stop = convert_valid_time(stop)
            return f"{start} to {stop}"
        else:
            raise ValueError("Invalid Time")

    else:
        raise ValueError("Invalid Time")

def check_valid_time(t):
    time = t.split(" ")[0]
    if ":" in time:
        hr, min = time.split(":")
        if int(hr) > 12 or int(hr) < 1 or int(min) > 59 or int(min) < 0:
            return False
    else:
        if int(time) > 12 or int(time) < 1:
            return False
    return True

def convert_valid_time(t):
    am_or_pm = t[-2:]
    time = t.split(" ")[0]
    if ":" in time:
        hr, min = time.split(":")
        hr = int(hr)
    else:
        hr = int(time)
        min = 0
    if am_or_pm == 'AM':
        if hr == 12:
            hr = 0
    elif am_or_pm == 'PM':
        if hr != 12:
            hr += + 12
    return f"{hr:02}:{min:02}"


if __name__ == "__main__":
    main()
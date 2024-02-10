import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #9:00 AM to 5:00 PM
    #9 AM to 5 PM
    #12:30 AM to 8:50 PM
    #12 AM to 12 PM
    if time := re.search(r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$', s, re.IGNORECASE):
        if int(time.group(1)) > 12 or int(time.group(4)) > 12:
            raise ValueError
        elif time.group(2) != None and time.group(5) != None:
            if int(time.group(2)) > 59 or int(time.group(5)) > 59:
                raise ValueError

        hour1= int(time.group(1))
        if time.group(3) == "PM" and int(time.group(1)) != 12:
            hour1 += 12
        elif time.group(3) == "AM" and int(time.group(1)) == 12:
            hour1 -= 12
        if time.group(2) == None:
            time1 = f"{hour1:02}:00"
        else:
            time1 = f"{hour1:02}:{time.group(2)}"

        hour2= int(time.group(4))
        if time.group(6) == "PM" and int(time.group(4)) != 12:
            hour2 += 12
        elif time.group(6) == "AM" and int(time.group(4)) == 12:
            hour2 -= 12
        if time.group(5) == None:
            time2 = f"{hour2:02}:00"
        else:
            time2 = f"{hour2:02}:{time.group(5)}"

        return f"{time1} to {time2}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
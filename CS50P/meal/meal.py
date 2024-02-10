def main():
    time = convert(input("What time is it? "))

    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")
    else:
        pass

def convert(time):

    if "am" in time or "a.m." in time or "pm" in time or "p.m." in time:
        hrs_mins, am_pm = time.split(" ")
        hours, minutes = hrs_mins.split(":")

        if am_pm == "p.m." or am_pm == "pm" and int(hours) != 12:
            hours = float(hours) + 12

    else:
        hours, minutes = time.split(":")
        result = float(minutes) / 60 + float(hours)

    return result

if __name__ == "__main__":
    main()
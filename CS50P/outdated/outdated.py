list = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        if 12 >= int(month) >= 1 and 31 >= int(day) >= 1:
            break

    except:
        if "," in date:
            try:
                month, day, year = date.split(" ")
                for i in range(len(list)):
                    if month == list[i]:
                        month = i + 1
                day = day.replace(",","")

                if 12 >= int(month) >= 1 and 31 >= int(day) >= 1:
                    break
            except:
                print()
                pass
        else:
            continue

print(f"{year}-{int(month):02}-{int(day):02}")
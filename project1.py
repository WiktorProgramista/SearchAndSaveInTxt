
attempt = 0

with open("Poland.txt", "r", encoding='utf-8') as file1:
    lines = file1.readlines()

    location = input("Wpisz lokalizacje:")

    what = input("Wpisz co ma wyszukac w pliku")

    with open(location, "w") as file2:
        for line in lines:
            if what in line:
                file2.writelines(line)
                print(line + "\n")




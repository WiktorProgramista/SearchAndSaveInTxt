
attempt = 0

location1 = input("plik z ktorego chcesz wyszukac fraze: ")

location2 = input("plik do ktorego chcesz wkleic: ")

with open(location1, "r", encoding='UTF-8') as file1:
    lines = file1.readlines()

    what = input("Wpisz co ma wyszukac w pliku: ")

    with open(location2, "w") as file2:
        for line in lines:
            if what in line:
                file2.writelines(line)
                print(line + "\n")
                attempt += 1
                
    if what in lines != lines:
        print("Nie znaleziono ", what, "w pliku: ", location1)

print("Znalezione wyniki: ", attempt)





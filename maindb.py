from crud import*

db = next(get_db())

inputSP = ""
inputKW = ""
inputA = ""

while inputSP != "done":
    inputSP = input("Please enter a sport or 'done' to exit. If you'd like to remove a sport type 'remove': ").lower()
    if inputSP != "done" and inputSP != "remove":
        existing_sport = get_sport_by_content(db, inputSP)
        if existing_sport:
            print(f"Sport '{existing_sport.content}' already exists.")
            new_sport = existing_sport
        else:
            new_sport = add_sport(db, inputSP)
            print(f"Added sport: {new_sport.content}")

        inputKW = ""
        while inputKW != "done":
            inputKW = input("Please enter a keyword or 'done' to finish. If you'd like to remove a keyword type 'remove': ").lower()
            if inputKW != "done" and inputKW != "remove":
                existing_keyword = get_keyword_by_content(db, inputKW)
                if existing_keyword:
                    print(f"Keyword '{existing_keyword.content}' already exists.")
                    new_keyword = existing_keyword
                else:
                    new_keyword = add_keyword(db, new_sport.id, inputKW)
                    print(f"Added keyword: {new_keyword.content}")

                inputA = ""
                while inputA != "done":
                    inputA = input(f"Please enter information about {inputKW.lower()} or type 'done' to finish. If you would like to delete a value, type 'remove': ").lower()
                    if inputA != "done" and inputA != "remove":
                        new_answer = add_answer(db, new_keyword.id, inputA)
                        print(f"Added Information: {new_answer.content}")
                    elif inputA == "remove":
                        inputRMA = input("Which value would you like to delete? ")
                        remove_answer(db, inputRMA)
                        print("Value " + inputRMA + " was removed")
                        inputRMA = ""
            elif inputKW == "remove":
                inputRMKW = input("Which keyword would you like to remove? ")
                remove_keyword(db, inputRMKW)
                print("Keyword " + inputRMKW + " was removed")   
                inputRMKW = "" 
    elif inputSP == "remove":
        inputRMS = input("Which sport would you like to remove? ")
        remove_sport(db, inputRMS)
        print("Sport " + inputRMS + " was removed")
        inputRMS = ""

db.close()


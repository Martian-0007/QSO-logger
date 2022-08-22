import logfunctions as fx
import json


phoneticalpha = {
    "A" : "Alpha",
    "B" : "Bravo",
    "C" : "Charlie",
    "D" : "Delta",
    "E" : "Echo",
    "F" : "Foxtrot",
    "G" : "Golf",
    "H" : "Hotel",
    "I" : "India",
    "J" : "Juliett",
    "K" : "Kilo",
    "L" : "Lima",
    "M" : "Mike",
    "N" : "November",
    "O" : "Oscar",
    "P" : "Papa",
    "Q" : "Quebec",
    "R" : "Romeo",
    "S" : "Sierra",
    "T" : "Tango",
    "U" : "Uniform",
    "V" : "Victor",
    "W" : "Whiskey",
    "X" : "X-ray",
    "Y" : "Yankee",
    "Z" : "Zulu",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Niner",
    "0" : "Zero"
}


try:
   
   
    while True:
       
       
        try:
            CALL = input("\n\nCallsing:\n")
            CALL = CALL.upper()


            print("\n")
            for i in CALL:
                print(phoneticalpha[i])

            

            with open("db/"+CALL+".json", "r", encoding='utf-8') as fl:
                content = fl.read()
                data = json.loads(content)
                print("\n\n"+CALL+":")
                data["QSO count"] = data["QSO count"] + 1
                print("QSO count: "+str(data["QSO count"])+"\nLast seen: "+data["Last seen"])
            
            with open("db/"+CALL+".json", "w", encoding='utf-8') as fl:
                data["Last seen"] = fx.CurTime()
                datawr = json.dumps(data)
                print(datawr, file = fl)
                

        except FileNotFoundError:
            with open("db/"+CALL+".json", "a", encoding='utf-8') as fl:
                content = {
                    "QSO count" : 1,
                    "Last seen" : fx.CurTime()
                }
                print("\n\n"+CALL+":")
                print("QSO count: "+str(content["QSO count"])+"\nLast seen: "+content["Last seen"])
                data = json.dumps(content)
                print(data, file = fl)


except KeyboardInterrupt:
    print("\n\nENDED BY USER (KeyboardInterrupt)")
    quit()
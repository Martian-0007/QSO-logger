import logfunctions as fx
import json


phoneticalpha = {
    "A" : "Alpha - Adam",
    "B" : "Bravo - Božena",
    "C" : "Charlie - Cyril",
    "Č" : "Čeněk",
    "D" : "Delta - David",
    "Ď" : "Ďáblice",
    "E" : "Echo - Emil",
    "F" : "Foxtrot - František",
    "G" : "Golf - Gustav",
    "Ch" : "Chrudim",
    "H" : "Hotel - Helena",
    "I" : "India - Ivan",
    "J" : "Juliett - Josef",
    "K" : "Kilo - Karel",
    "L" : "Lima - Ludvík",
    "M" : "Mike - Marie",
    "N" : "November - Norbert/Neruda",
    "O" : "Oscar - Oto/Otakar",
    "P" : "Papa - Petr",
    "Q" : "Quebec - Quido",
    "R" : "Romeo - Rudolf",
    "Ř" : "Řehoř",
    "S" : "Sierra - Svatopluk",
    "Š" : "Šimon/Šárka",
    "T" : "Tango - Tomáš",
    "Ť" : "Těšnov",
    "U" : "Uniform - Urban",
    "V" : "Victor - Václav",
    "W" : "Whiskey - Dvojité V",
    "X" : "X-ray - Xaver",
    "Y" : "Yankee - Ypsilon",
    "Z" : "Zulu - Zuzana",
    "1" : "One - Jedna",
    "2" : "Two - Dva",
    "3" : "Three - Tři",
    "4" : "Four - Čtyry",
    "5" : "Five - Pět",
    "6" : "Six - Šest",
    "7" : "Seven - Sedum",
    "8" : "Eight - Osum",
    "9" : "Niner - Devět",
    "0" : "Zero - Nul/a"
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
                datawr = json.dumps(data, ensure_ascii=False, indent=2)
                print(datawr, file = fl)
                

        except FileNotFoundError:
            with open("db/"+CALL+".json", "a", encoding='utf-8') as fl:
                content = {
                    "QSO count" : 1,
                    "Last seen" : fx.CurTime()
                }
                print("\n\n"+CALL+":")
                print("QSO count: "+str(content["QSO count"])+"\nLast seen: "+content["Last seen"])
                data = json.dumps(content, ensure_ascii=False, indent=2)
                print(data, file = fl)


except KeyboardInterrupt:
    print("\n\nENDED BY USER (KeyboardInterrupt)")
    quit()
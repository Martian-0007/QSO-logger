import logfunctions as fx
import json


try:
   
   
    while True:
       
       
        try:
            CALL = input("Callsing:\n")
            CALL = CALL.upper()
            

            with open("db/"+CALL+".json", "r", encoding='utf-8') as fl:
                content = fl.read()
                data = json.loads(content)
                print("\n"+CALL+":")
                data["QSO count"] = data["QSO count"] + 1
                print(data)
            
            with open("db/"+CALL+".json", "w", encoding='utf-8') as fl:
                data = {
                    "QSO count" : data["QSO count"],
                    "Last seen" : fx.CurTime()
                }
                datawr = json.dumps(data)
                print(datawr)
                print(datawr, file = fl)
                

        except FileNotFoundError:
            with open("db/"+CALL+".json", "a", encoding='utf-8') as fl:
                content = {
                    "QSO count" : 1,
                    "Last seen" : fx.CurTime()
                }
                data = json.dumps(content)
                print("\n"+CALL+":\n")
                print(data)
                print(data, file = fl)


except KeyboardInterrupt:
    print("user ended")
    quit()
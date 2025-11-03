import random
import csv

class Use_file:

    @staticmethod
    def open_file(file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            dictionary_list = list(csv.DictReader(f))

        dictionary = random.choice(dictionary_list)

        return dictionary 
        

class Players:
    def __init__(self, number, name, prof, cash, salary, cost ):
        self.number = number  
        self.name = name 
        self.prof = prof 
        self.cash = cash
        self.salary = salary
        self.cost = cost


    def player_info(self):
        print(f"____ГРАВЕЦЬ {self.number}: {self.prof}, {self.name}____")
        print (f"Готівка : {self.cash}")   
        print (f"Дохід:    {self.salary}") 
        print (f"Витрати : {self.cost}") 
        print (f" ") 

class PlayerFactory:
    
    @staticmethod
    def create_players(number, name):

        player_data = Use_file.open_file("professions.csv")

        prof = str(player_data["Prof"])
        cash = float(player_data["Cash"])
        salary = float(player_data["Salary"])
        cost = float(player_data["Cost"])

        player = Players(number, name, prof, cash, salary, cost)

        return player 
    


class Events:
    def __init__(self):
        self.events = ["business"]

        """event_on_market", "spending","tax""" 

    @staticmethod
    def event_info (select_busines, event):

        if select_busines == 1:
            print(f"__ {event["Title"]} __")
            print(f"{event["Description"]}")
            print(f"Вартість: {event["Cash"]} грн.")
            print(f"Дохід: {event["Salary"]} грн.")

        elif select_busines == 2:
            print(f"__ {event["Title"]} __")
            print(f"{event["Description"]}")
            print(f"Вартість: {event["Cash"]} грн.")
            print(f"Дохід: {event["Salary"]} грн.")
            print(f"Витрати: {event["Cost"]} грн ")

    def random_event(self, player):
        
        event = random.choice(self.events)

        if event == "business" :
            print(f"Ви маєте можливість придбати бізнес!!\n")
            select_busines = int(input("Оберіть розмах бізнесу (1 - Малий бізнес , 2 - Великий бізнес)   :"))
            
            if select_busines == 1 :
                event_data = Use_file.open_file("small_events.csv")

                Events.event_info(select_busines, event_data)

            elif select_busines == 2 :
                event_data = Use_file.open_file("big_events.csv")

                Events.event_info(select_busines, event_data) 
            
            select = input("Бажаєте купити (y/n): ").lower()

            if select == "y":
                player.cash += float(event_data["Cash"])
                player.salary += float(event_data["Salary"])
                player.cost += float(event_data["Cost"])

            else:
                print(f"Гравець {player.name} пропустив подію")
        
        elif event == "event_on_market":
            print("Скоро буде")
        
        elif event == "spending":
            print("Скоро буде")

        elif event == "tax": 
            print("Скоро буде")


        player.player_info()



class GamePlay:

    next_event = Events()

    def player_turn(self, player):
        print(f"\n🎲 Хід гравця {player.name}")
        
        self.next_event.random_event(player)

        

            






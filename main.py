
from player import Players, PlayerFactory, GamePlay


def main():

    factoryplayers = PlayerFactory()
    game = GamePlay()

    
    print(f"...Вітаємо в грі CASHFLOW!...")

    players_list   = []
    player_number = int(input("Вкажіть кількість гравців: "))

    
    
    for i in range(player_number):
        number = i+1
        name = str(input(f"Гравець {number}, Вкажіть ваше ім'я: "))
        
        person = factoryplayers.create_players(number, name)
        players_list.append(person)
        
    for i in players_list:
        i.player_info()


    while True:
        for p in players_list:
            game.player_turn(p)

        ready = input("\nПродовжуємо гру? (y/n): ").lower()
        if ready != "y":
            
            break



    text_ed = print(f"Дякую за гру!")
    return text_ed


if __name__=='__main__':
    main()
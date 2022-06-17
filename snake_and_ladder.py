import random

ladder={2:38,8:16,12:35,21:47,31:65,71:91,25:96}
snake={23:3,35:10,55:18,77:5,85:27,98:44}
MAX_VAL=100
position_player1=0
position_player2=0

def move(position):
    dice=random.randint(1,6)
    print(f'Dice:{dice}')
    old_pos=position
    position=position + dice
    if position>MAX_VAL:
        position=old_pos
    if position in snake:
        print('you have been poisioned by snake')
        position=snake[position]
        print(f'position:{position}')
    elif position in ladder:
        print('you have climed the ladder')
        position=ladder[position]
        print(f'position:{position}')
    else:
        print(f'position:{position}')
    return position

while True:
    player1_name =input("Please press enter for player 1 to roll the dice: ")
    position_player1=move(position_player1)
        

    if position_player1==MAX_VAL:
    #     print(f'{player1_name} wait')
    #     return position_player1
    # elif position_player1<100:
    #     print(f'{position_player1} need more')
    # else:
        print('you won')
        break
            
    
        

    player2_name = input("Please press enter for player 2 to roll the dice: ")
    position_player2=move(position_player2)
        
    
    if position_player2==MAX_VAL:
    #     print(f'{player2_name} wait')
    #     return position_player2
    # elif position_player2<100:
    #     print(f'{position_player2} need more')
    # else:
        print('you won')
        break
            
    


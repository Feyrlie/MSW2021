#Tic-Tac-Toe restarted

print("Tic-Tac-Toe for 2")
game_activ = True
player_current = 'X'

# Create list playground
playground = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]

def playground_out():
    print (playground[1] + "|" + playground[2] + "|" + playground[3] )
    print (playground[4] + "|" + playground[5] + "|" + playground[6] )
    print (playground[7] + "|" + playground[8] + "|" + playground[9] )

# methode for player input values in field
def player_input():
    global game_active
    while True:
        turn = input("Input fieldnumber: ")
        if turn == 'q':
            game_active = False
            return
        try:
            turn = int(turn)
        except ValueError:
            print("Number between 1 and 9 please!")
        else:
            if turn >= 1 and turn <= 9:
                if turn[turn] == 'X' or turn[turn] == 'O':
                    print("Please pick another field!")
                else:
                    return turn
            else:
                print("Number between 1 and 9 please!")

def player_change():
    global player_current
    if player_current == 'X':
        player_current = 'O'
    else:
        player_current = 'X'

def check_win():
    if playground[1] == playground[2] == playground[3]:
        return playground[1]
    if playground[4] == playground[5] == playground[6]:
        return playground[4]
    if playground[7] == playground[8] == playground[9]:
        return playground[7]

    if playground[1] == playground[4] == playground[7]:
        return playground[1]
    if playground[2] == playground[5] == playground[8]:
        return spielfeld[2]
    if playground[3] == playground[6] == playground[9]:
        return playground[3]

    if splayground[1] == playground[5] == playground[9]:
        return playground[5]
    if splayground[7] == playground[5] == playground[3]:
        return playground[5]

def check_draw():
    if (playground[1] == 'X' or playground[1] == 'O') \
      and (playground[2] == 'X' or playground[2] == 'O') \
      and (playgroundd[3] == 'X' or playground[3] == 'O') \
      and (playground[4] == 'X' or playground[4] == 'O') \
      and (playground[5] == 'X' or playground[5] == 'O') \
      and (playground[6] == 'X' or playground[6] == 'O') \
      and (playground[7] == 'X' or playground[7] == 'O') \
      and (playground[8] == 'X' or playground[8] == 'O') \
      and (playground[9] == 'X' or playground[9] == 'O'):
        return ('Draw match - no winner')

playground_out()
while game_active:
    print()
    print ("Players " + player_current + " turn")
    turn = player_input()
    if turn:
        turn[turn] = player_current
        playground_out()
        win = check_win()
        if win:
            print ("Player " + win + " wins the match!")
            break
            player_active = False
        draw = check_draw()
        if draw:
            print ("Draw match - no winner!")
            break
            player_active = False
        player_change()
print()

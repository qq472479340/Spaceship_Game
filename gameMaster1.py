import sys
import time
import random
import os
import keyboard

#Initialize the game ground.
def Initialize(length, height, level):
    os.system('cls')
    global board, position
    for i in range(height//2):
        temp = [' ' for k in range(length)]
        #Generates blocks randomly at every two lines.
        if i%2 == 0:
            rand = random.randint(1, length//(7-level))
            for _ in range(rand):
                k = random.randint(0, length-1)
                temp[k] = '-'
        board += ["".join(temp)]
    temp_ss = [' ' for k in range(length)]
    #The lower half of the ground would be blank. That is to make the player have some time to prepare.
    while i<height-1:
        board += ["".join(temp_ss)]
        i += 1
    temp_ss[position] = '*'
    board += ["".join(temp_ss)]
    for m in range(height):
        print(board[m], end = '' if m==height-1 else '\n')

#Detect the input of the keyboard and move the player.
def Control(event):
    global position, press_flag, board
    if event.event_type == 'down' and event.name == 'left' and press_flag == 0:
        press_flag = 1
        if position>0:
            board[height-1] = board[height-1][:position]+' '+board[height-1][position+1:]
            position -= 1
    elif event.event_type == 'up' and event.name == 'left' and press_flag == 1:
        press_flag = 0
    
    if event.event_type == 'down' and event.name == 'right' and press_flag == 0:
        press_flag = 1
        if position<length:
            board[height-1] = board[height-1][:position]+' '+board[height-1][position+1:]
            position += 1
    elif event.event_type == 'up' and event.name == 'right' and press_flag == 1:
        press_flag = 0

#Check if it is the end of the game
def EndGame():
    global board, position
    if board[height-1][position] == '-':
        return True
    return False



length, height = '', ''
level = ''
#Receive the input data and check the validility.
print("Please input the length of the board:")
while (not length.isdigit()) or 0>=int(length):
    length = input("Length(Please input an integer):")
print("Please input the height of the board:")
while (not height.isdigit()) or 0>=int(height):
    height = input("Height(Please input an integer):")
print("Please input the game level:")
while (not level.isdigit()) or (0 >= int(level) or int(level) > 5):
    level = input("Level(1-5):")

length, height = int(length), int(height)
level = int(level)
#At first, set the player at the middle of the line.
position = length//2
board = []
point = 0
press_flag = 0
Initialize(length, height, level)
count_flag = 0 if height%2 == 1 else 1
pre_time = time.time()
end_game = False
while True:
    #Detected the keyboard input.
    keyboard.hook(Control)
    #Check if it is the end of the game. If so, set the player as 'X'. Otherwise, the player would be '*'.
    if not EndGame():
        board[height-1] = board[height-1][:position]+'*'+board[height-1][position+1:]
        #Only needs to re-print the last line.
        print('\r'+board[height-1], end='')
    else:
        board[height-1] = board[height-1][:position]+'X'+board[height-1][position+1:]
        break
    cur_time = time.time()
    #The ground is going down every 1 second.
    if cur_time - pre_time >= 1:
        pre_time = cur_time
        #calculate the point
        point += 1
        #After the ground goind down, check if it is the end of the game.
        if board[height-2][position] == '-':
            end_game = True
            board[height-1] = board[height-2][:position]+'X'+board[height-2][position+1:]
        if not end_game:
            board[height-1] = board[height-2][:position]+'*'+board[height-2][position+1:]
        for i in range(height-2, 0, -1):
            board[i] = board[i-1]

        temp = [' ' for k in range(length)]
        if count_flag == 0:
            #Generates blocks randomly.
            rand = random.randint(1, length//(7-level))
            for j in range(rand):
                k = random.randint(0, length-1)
                temp[k] = '-'
            count_flag = 1
        else:
            count_flag = 0
        board[0] = "".join(temp)

        if end_game:
            break
        #Clear the output and refresh the screen.
        os.system('cls')
        for m in range(height):
            print(board[m], end='' if m== height-1 else '\n')

#Clear the screen and output the last scene of the game.
os.system('cls')
for m in range(height):
    print(board[m])

print("END---------------------------------")
print("point:"+str(point))
    


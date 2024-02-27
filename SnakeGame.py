from tkinter import *
from random import randint as rand
from time import *
import time
import ast
import os
import json

# objective 1:   icon image , snake image
# objective 2:   stars shape in background
# objective 3:   text in menu, instruction, etc
# objective 4:   scoring mechanisam is "life" and "seconds"
# objective 5:   leaderboard shows score in accending order
# objective 6:   scale 1280 x 720
# objective 7:   balls are moving to kill the snake
# objective 8:   snake can be moved by left and right key
# objective 9:   snake and ball collide, game ends
# objective 10:  pause button
# objective 11:  You can select arrow keys
# objective 12:  cheat code c will reduce ball speed
# objective 13:  save the game, continue form where left
# objective 14:  boss key " Space"

#all objectives are achived#
#pep8online also used , only long lines

#if the game lags please restart the game bucause sometime the games runs slow and sometime normal


window = Tk()
window.geometry("1280x720")
window.title("Snake in the Space")
icon = PhotoImage(file=r'snake.png')
window.iconphoto(False, icon)

# initalization for use in the code
global canvas
canvas = Canvas(window, width=1280, height=720)
global score, entry1, is_paused, high_score
global high_score, x, y, my_image, name
global shooter_pos, ball, rest, pos
global start, end, prev, end_save
rest = 0.000001
score = 1
is_paused = False
prev = 0


def configer():
    # this block clear the window,for new window,or frame
    canvas.delete('all')
    canvas.pack_forget()


def tog_pause():
    # this function just pause the game
    global is_paused
    if is_paused is True:
        is_paused = False
    if not is_paused:
        is_paused = True
    return


def boss_key(event):
    # this function show the fake sublime when boss key pressed
    global canvas1
    global sublime
    global icon
    global is_paused
    top = Toplevel()
    top.title('Sublime')
    icon = PhotoImage(file=r'sublime_icon.png')
    top.iconphoto(False, icon)
    top.geometry("2000x1400")
    canvas1 = Canvas(top, width=1280, height=720)
    sublime = PhotoImage(file='sublime.png')
    sublime_label = Label(top, image=sublime)
    sublime_label.place(x=0, y=0, relwidth=1, relheight=1)
    is_paused = True
    canvas1.pack()


window.bind("<space>", boss_key)
canvas = Canvas(window, width=1280, height=720, bg='black')


def game_back():
    # this provides the start background at the back which looks like space
    global canvas
    star = []
    c = ['white', 'red', 'blue']

    for i in range(800):
        x = rand(1, 1280)
        y = rand(1, 720)
        size = rand(2,  5)
        f = rand(0, 2)
        xy = (x, y, x+size, y+size)
        tmp_star = canvas.create_oval(xy, fill=c[f])
        star.append(tmp_star)


def confiq_canvas():
    # removes the non essentials labels and button
    global canvas
    canvas.delete('all')
    # canvas.pack_forget()


def Exit():
    # this function deals with the exit of the program before starting the game
    configer()
    game_back()
    exit = PhotoImage(file='menu4.gif')
    exitbutton = Button(window, text=" Exit ", bg='#060d0d', fg='red', command=window.destroy)
    canvas.create_window(640, 400, window=exitbutton)
    canvas.pack()


def adder(adding):
    with open('save.txt', 'w') as file3:
         file3.write(json.dumps(adding))


def updated():
    global canvas
    global entry
    global name
    global elap
    configer()
    game_back()
    data = open("save.txt", "r")
    content = data.read()
    dictionary = ast.literal_eval(content)
    data.close()
    dictionary[entry.get()] = elap
    name = entry.get()
    
    label8ert = Label(window, text="Hello !!  " + name, bg='#060d0d', fg='white', font=('Cosmic Alien', 25))
    canvas.create_window(600, 200, window=label8ert)
    label8j = Label(window, text=' Updated Sucessfully ', bg='#060d0d', fg='white', font=('Cosmic Alien',  25))
    canvas.create_window(620, 330, window=label8j)
    button23j = Button(window, text=' Exit ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=window.destroy)
    canvas.create_window(620, 600, window=button23j)
    label8 = Label(window, text="Hello !!  " + name, bg='#060d0d', fg='white', font=('Cosmic Alien', 25))
    canvas.create_window(600, 200, window=label8)
    adder(dictionary)
    canvas.pack()


def Name_entre():
    # if the player choose to start the game he will be directed to entre his name and details
    configer()
    game_back()
    global entry
    global diff
    global name
    label7 = Label(window, text=' To Update the leader Board', bg='#060d0d', fg='white', font=('Cosmic Alien',  30))
    canvas.create_window(640, 90, window=label7)
    label8 = Label(window, text=' Entre your Name  : ', bg='#060d0d', fg='white', font=('Cosmic Alien', 25))
    canvas.create_window(300, 200, window=label8)
    entry = Entry(window)
    canvas.create_window(600, 200, width=200, height=40, window=entry)
    label300 = Label(window, text=' Boss Key is ( Space ) ', bg='#060d0d', fg='white', font=('Cosmic Alien', 20))
    canvas.create_window(640, 400, window=label300)
    button4j = Button(window, text=' Update ', bg='#060d0d', fg='white', font=('Times', 25), command=updated)
    canvas.create_window(640, 550, window=button4j)
    canvas.pack()


def end_snake():
    # game end
    global canvas
    global end, start
    global elap
    canvas.delete('all')
    game_back()
    elapse = end - start
    elap = int(elapse)
    label789 = Label(window, text=' Snake in the Space', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien', 35))
    canvas.create_window(640, 140, window=label789)
    label786 = Label(window, text=' Game Ended', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien', 35))
    canvas.create_window(640, 240, window=label786)
    label786o = Label(window, text=' You Played for :   ' + str(elap) + " seconds", bg='#060d0d', fg='#5794A7', font=('Cosmic Alien', 25))
    canvas.create_window(640, 350, window=label786o)
    button417 = Button(window, text=' Update the Leader Board  ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=Name_entre)
    canvas.create_window(640, 470, window=button417)
    button417 = Button(window, text=' Exit the game  ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=window.destroy)
    canvas.create_window(640, 552, window=button417)


def left(event):
    # moves the snake to left if the game is not paused
    global my_image
    global pos
    x = -4.5
    y = 0
    if not is_paused and pos[0] > 30:
        canvas.move(my_image, x, y)
    canvas.pack()


def right(event):
    # moves the snake to the right if the game is not pause
    global my_image
    global pos
    x = 4.5
    y = 0
    if not is_paused and pos[0] < 1247:
        canvas.move(my_image, x, y)
    canvas.pack()


def cheat(event):
    # it will reduce the ball speed by increasing rest time
    global rest
    if rest == 0.000001:
        rest = 0.001

    elif (rest == 0.001):
        rest = 0.000001
    return


def ball_remov(hit):
    # removes the ball if the snake is hit by the ball
    global canvas
    global ball
    x = len(ball)
    if x > 0:
        canvas.delete(hit)
    return


def complete():
    global start
    global entry2
    global end_save
    canvas.delete('all')
    game_back()
    # end = time.time()
    next_game = end_save - start
    next_game = int(next_game)
    rec = open("record.txt", "w")
    rec.write(str(next_game) + '  ' + entry2.get())
    rec.close()
    window.destroy()


def save_game():
    # save the data of game if you choose to save game
    global end_save
    canvas.delete('all')
    game_back()
    label2k = Label(window, text=' Snake in the Space ', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  36))
    canvas.create_window(640, 107.5, window=label2k)
    label20qwert = Label(window, text=" Hello !!" + str(entry2.get()) + " !!", bg='#060d0d', fg='maroon', font=('Cosmic Alien',  25))
    canvas.create_window(640, 290.5, window=label20qwert)
    label20rty = Label(window, text=" Your Game has been recorded ", bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  25))
    canvas.create_window(640, 350.5, window=label20rty)
    button4jjj = Button(window, text=' Complete Save ', bg='#060d0d', fg='white', font=('Times', 25), command=complete)
    canvas.create_window(640, 550, window=button4jjj)


def game_save():
    global entry2
    global end_save
    configer()
    canvas.delete('all')
    game_back()
    end_save = time.time()
    label7 = Label(window, text=' To save the Game ', bg='#060d0d', fg='white', font=('Cosmic Alien',  30))
    canvas.create_window(640, 90, window=label7)
    label8 = Label(window, text=' Entre your Name  : ', bg='#060d0d', fg='white', font=('Cosmic Alien', 25))
    canvas.create_window(300, 200, window=label8)
    entry2 = Entry(window)
    canvas.create_window(600, 200, width=200, height=40, window=entry2)
    label300 = Label(window, text=' Boss Key is ( Space ) ', bg='#060d0d', fg='white', font=('Cosmic Alien', 20))
    canvas.create_window(640, 400, window=label300)
    button4j = Button(window, text=' Save ', bg='#060d0d', fg='white', font=('Times', 25), command=save_game)
    canvas.create_window(640, 550, window=button4j)
    canvas.pack()


def ball_maker():
    # this is the main game
    global shooter_pos, pos1
    global canvas
    global score
    global is_paused
    global my_image
    global ball
    global rest, prev
    global pos
    global start, end
    configer()
    game_back()
    num_balls = 8
    diameter = 30
    start = time.time()

    # life show and cheat code
    txt = " Cheat code :  C " + "                                 Life : " + str(score)
    scoreText = canvas.create_text(250, 25, fill="white", font=("Times 20 italic bold"), text=txt)

    # pause button
    button110 = Button(window, text=' Pause ', bg='#060d0d', fg='white', font=('Times', 25), command=tog_pause)
    canvas.create_window(1210, 25, window=button110)
    button110 = Button(window, text=' Save  Game', bg='#060d0d', fg='white', font=('Times', 25), command=game_save)
    canvas.create_window(800, 25, window=button110)
    ball = []

    colour = ["purple", "maroon", "green", "blue"]

    # snake image implemented
    img = PhotoImage(file='shooter.gif')
    z = Canvas(window)
    z.img = img
    my_image = canvas.create_image(400, 690, anchor=CENTER, image=img)
    shooter_pos = canvas.coords(my_image)

    # binding the keys
    # window.bind("<Left>", left)
    # window.bind("<Right>", right)
    window.bind("<c>", cheat)

    pos2 = canvas.coords(my_image)

    for i in range(num_balls):
        c_col = rand(0, 3)
        x = rand(20, 1210)
        y = rand(20, 550)

        xy = (x, y, x+diameter, y+diameter)

        ball.append(canvas.create_oval(xy, fill=colour[c_col]))

    canvas.pack()

    x = [1] * num_balls
    y = [1] * num_balls

    while True:
        if not is_paused:

            for i in range(num_balls):
                pos1 = canvas.coords(ball[i])
                pos = canvas.coords(my_image)
                if ((pos[0] - pos1[0]) < 55) and ((pos[0] - pos1[0]) > 0) and ((pos[1] - pos1[1]) > 0) and ((pos[1] - pos1[1]) < 55):
                    ball_remov(ball[i])
                    num_balls -= 1
                    end = time.time() + int(prev)
                    sleep(2)
                    end_snake()

                if pos1[3] > 715 or pos1[1] < 0:
                    y[i] = -y[i]

                if pos1[0] < 0 or pos1[2] > 1280:
                    x[i] = -x[i]

                canvas.move(ball[i], x[i], y[i])
                sleep(rest)
                window.update()

        else:
            window.update()



def sel_a():
    # binds arrow keys with a and d
    window.bind("<a>", left)
    window.bind("<d>", right)
    ball_maker()


def sel_arrow():
    # binds arrow keys with snake
    window.bind("<Left>", left)
    window.bind("<Right>", right)
    ball_maker()


def key_sel():
    # deals with the key slection options
    configer()
    game_back()
    label5qqll = Label(window, text=' Welcome to Snake in the Space', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  35))
    canvas.create_window(640, 100, window=label5qqll)
    label5qqlll = Label(window, text=' You can choose the keys', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  28))
    canvas.create_window(640, 240, window=label5qqlll)
    button1kl = Button(window, text=' Use Arrow keys to move the snake ', bg='#060d0d', fg='white', font=('Times', 20), command=sel_arrow)
    canvas.create_window(640, 350, window=button1kl)
    button2kl = Button(window, text=' Use (A) for left and (D) for right', bg='#060d0d', fg='white', font=('Times', 20), command=sel_a)
    canvas.create_window(640, 480, window=button2kl)
    canvas.pack()


def arranger(scr):
    # this will arange the data into asscending order
    done = sorted(scr.items(), key=lambda x: x[1], reverse=True)
    return done


def leader_board():
    # uses content from the txt file to make a leader board
    global canvas
    global high_score
    global score
    configer()
    game_back()
    data = open("save.txt", "r")
    content = data.read()
    dictionary = ast.literal_eval(content)
    data.close()
    label20 = Label(window, text=' Snake in the Space ', bg='#060d0d', fg='purple', font=('Cosmic Alien',  25))
    canvas.create_window(640, 107.5, window=label20)
    label21 = Label(window, text='Leader Board', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  25))
    canvas.create_window(640, 177.5, window=label21)
    cont = arranger(dictionary)
    x = 277.5
    for i in range(5):
        for y in range(1):
            out_lab = cont[i][0], "   score is   ", cont[i][1]
            label21o = Label(window, text=out_lab, bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  35))
            canvas.create_window(620, x, window=label21o)
            x += 60

    button22 = Button(window, text='Begin the Snake Run', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=key_sel)
    canvas.create_window(910, 610.5, window=button22)
    button23 = Button(window, text=' Exit the Game if Afraid ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=window.destroy)
    canvas.create_window(390, 610.5, window=button23)
    canvas.pack()


def retriver():
    # this will retrive the data of saved game
    global prev
    configer()
    game_back()
    
    opener = open("record.txt", "r")
    retrived = opener.read()
    retrived_use = retrived.split()
    opener.close()
    prev = retrived_use[0]
    old_name = retrived_use[1]

    label5qq = Label(window, text=' Welcome to Snake in the Space', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  35))
    canvas.create_window(640, 100, window=label5qq)
    label5qq1 = Label(window, text=' Your Name : ' + old_name, bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  22))
    canvas.create_window(640, 200, window=label5qq1)
    label5qq2 = Label(window, text=' Your active time is : ' + str(prev), bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  22))
    canvas.create_window(640, 300, window=label5qq2)
    button4qq = Button(window, text=' Continue Run, Snake is Ready ', bg='#060d0d', fg='white', font=('Times', 25), command=key_sel)
    canvas.create_window(640, 390, window=button4qq)
    button6qq = Button(window, text=' Exit the Game if Afraid   ', bg='#060d0d', fg='white', font=('Times', 25), command=Exit)
    canvas.create_window(640, 490, window=button6qq)
    button3qq = Button(window, text=' View the instructions ', bg='#060d0d', fg='white', font=('Times', 25),  command=instruction)
    canvas.create_window(640, 590, window=button3qq)
    canvas.pack()


def instruction():
    # display the instruction page
    configer()
    game_back()
    label1 = Label(window, text=' Below are all the instruction for the game ', bg='#060d0d', fg='#19596D', font=('Cosmic Alien',  30))
    canvas.create_window(640, 100, window=label1)
    label2 = Label(window, text=' Simply use the seclected keys to move snake \n and save the snake from enemy bombs roaming around\n Lets see how long you play \n Remember Snake scrolls slowly', bg='#060d0d', fg='white', font=('Cosmic Alien',  17))
    canvas.create_window(640, 220, window=label2)
    label3 = Label(window, text=' Boss Key is ( Space ) ', bg='#060d0d', fg='white', font=('Cosmic Alien',  20))
    canvas.create_window(640, 340, window=label3)
    label700 = Label(window, text=' Cheat code  ( C ), Reduce Ball Speed ', bg='#060d0d', fg='white', font=('Cosmic Alien',  20))
    canvas.create_window(640, 420, window=label700)
    label4 = Label(window, text=' Pause the game using the pause Button ', bg='#060d0d', fg='white', font=('Cosmic Alien',  20))
    canvas.create_window(640, 475, window=label4)
    button1 = Button(window, text=' Menu ', bg='#060d0d', fg='white', font=('Times', 20), command=Menu)
    canvas.create_window(640, 550, window=button1)
    button2 = Button(window, text=' Game Start', bg='#060d0d', fg='white', font=('Times', 20), command=key_sel)
    canvas.create_window(640, 600, window=button2)
    canvas.pack()


def Menu():
    # starting point of the game and this part display the menu
    configer()
    game_back()
    label5 = Label(window, text=' Welcome to Snake in the Space', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  35))
    canvas.create_window(640, 100, window=label5)
    button5 = Button(window, text='Begin the Snake Run  ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=key_sel)
    canvas.create_window(640, 250, window=button5)
    button5 = Button(window, text=' Continue Your Game ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=retriver)
    canvas.create_window(640, 350, window=button5)
    button6 = Button(window, text=' Exit the Game if Afraid   ', bg='#060d0d', fg='white', font=('Times', 25), command=Exit)
    canvas.create_window(640, 650, window=button6)
    button3 = Button(window, text=' View the instructions ', bg='#060d0d', fg='white', font=('Times', 25),  command=instruction)
    canvas.create_window(640, 550, window=button3)
    button4 = Button(window, text=' View the LeaderBoard ', bg='#060d0d', fg='white', font=('Times', 25), command=leader_board)
    canvas.create_window(640, 450, window=button4)
    canvas.pack()


Menu()

window.mainloop()

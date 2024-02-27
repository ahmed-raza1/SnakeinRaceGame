from tkinter import *
from random import randint as rand
from time import *
import ast
import os

# objective 1:   icon image , snake image
# objective 2:   stars shape in background
# objective 3:   text in menu, instruction, etc
# objective 4:   scoring mechanisam is "life" and "score"
# objective 5:   leaderboard shows score in accending order
# objective 6:   scale 1280 x 720
# objective 7:   balls are moving to kill the snake
# objective 8:   snake can be moved by left and right key
# objective 9:   snake and ball collide, game ends
# objective 10:  pause button
# objective 12:  cheat code c will reduce ball speed
# objective 13:  save the game
# objective 14:  boss key " Space"

window = Tk()
window.geometry("1280x720")
window.title("Snake in the Space")
icon = PhotoImage(file=r'snake.png')
window.iconphoto(False, icon)

# setting a background image for menu
global canvas
canvas = Canvas(window, width=1280, height=720)
# background1 = PhotoImage(file='menu4.gif')
# background1_label = Label(window, image = background1)
# background1_label.place(x=0, y=0, relwidth=1 relheight = 1)

global score, entry1, is_paused, high_score
global high_score, x, y, my_image, name 
global shooter_pos, ball, rest, pos
rest = 0.000001
score = 1
is_paused = False

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


def updated():
    global canvas
    global entry
    global name
    configer()
    game_back()
    f = open("save.txt", "a")
    f.write("\nAhmed")
    f.close()
    label8j = Label(window, text=' Updated Sucessfully ', bg='#060d0d', fg='white', font=('Cosmic Alien',  25))
    canvas.create_window(620, 330, window=label8j)
    button23j = Button(window, text=' Exit ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=window.destroy)
    canvas.create_window(620, 600, window=button23j)
    name = entry.get()
    label8 = Label(window, text="Hello !!  " + name, bg='#060d0d', fg='white', font=('Cosmic Alien', 25))
    canvas.create_window(600, 200, window=label8)
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
    global canvas
    canvas.delete('all')
    game_back()
    label789 = Label(window, text=' Snake in the Space', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien', 35))
    canvas.create_window(640, 100, window=label789)
    label786 = Label(window, text=' Game Ended', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien', 35))
    canvas.create_window(640, 200, window=label786)
    button417 = Button(window, text=' Update the Leader Board  ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=Name_entre)
    canvas.create_window(640, 306, window=button417)
    button417 = Button(window, text=' Exit the game  ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=window.destroy)
    canvas.create_window(640, 512, window=button417)


def left(event):
    # moves the snake to left if the game is not paused
    global my_image
    global pos
    x = -10
    y = 0
    if not is_paused and pos[0] > 30:
        canvas.move(my_image, x, y)
    canvas.pack()


def right(event):
    # moves the snake to the right if the game is not pause
    global my_image
    global pos
    x = 10
    y = 0
    if not is_paused and pos[0]<1247:
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


def ball_maker():
    # this is the main game
    global shooter_pos, pos1
    global canvas
    global score
    global is_paused
    global my_image
    global ball
    global rest
    global pos
    configer()
    game_back()
    num_balls = 8
    diameter = 30

    # life show and cheat code
    txt = " Cheat code :  C " + "                                 Life : " + str(score)
    scoreText = canvas.create_text(250, 25, fill="white", font=("Times 20 italic bold"), text=txt)

    # pause button
    button110 = Button(window, text=' Pause ', bg='#060d0d', fg='white', font=('Times', 25), command=tog_pause)
    canvas.create_window(1210, 25, window=button110)

    ball = []

    colour = ["purple", "maroon", "green", "blue"]

    # snake image implemented
    img = PhotoImage(file='shooter.gif')
    z = Canvas(window)
    z.img = img
    my_image = canvas.create_image(400, 690, anchor=CENTER, image=img)
    shooter_pos = canvas.coords(my_image)

    # binding the keys
    window.bind("<Left>", left)
    window.bind("<Right>", right)
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

def arranger(scr):
    done = sorted(scr.items(), key = lambda t:t[0], reverse=True)
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
    label20 = Label(window, text=' Snake in the Space ', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  25))
    canvas.create_window(640, 107.5, window=label20)
    label21 = Label(window, text='Leader Board', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  25))
    canvas.create_window(640, 177.5, window=label21)
    cont = arranger(dictionary)
    print(cont)
    x = 247.5
    for i in range(4):
        for y in range(1):
            out_lab = cont[i][0], cont[i][1]
            label21o = Label(window, text=out_lab, bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  35))
            canvas.create_window(250, x, window=label21o)
            x += 60

    button22 = Button(window, text='Begin the Snake Run', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=ball_maker)
    canvas.create_window(910, 590.5, window=button22)
    button23 = Button(window, text=' Exit the Game if Afraid ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=window.destroy)
    canvas.create_window(390, 590.5, window=button23)
    canvas.pack()


def instruction():
    # display the instruction page
    configer()
    game_back()
    label1 = Label(window, text=' Below are all the instruction for the game ', bg='#060d0d', fg='#19596D', font=('Cosmic Alien',  30))
    canvas.create_window(640, 190, window=label1)
    label2 = Label(window, text=' Simply use the arrow keys to move snake \n and save the snake from enemy bombs roaming around\n Lets see how long you play', bg='#060d0d', fg='white', font=('Cosmic Alien',  17))
    canvas.create_window(640, 280, window=label2)
    label3 = Label(window, text=' Boss Key is ( Space ) ', bg='#060d0d', fg='white', font=('Cosmic Alien',  20))
    canvas.create_window(640, 380, window=label3)
    label700 = Label(window, text=' Cheat code  ( C ), Reduce Ball Speed ', bg='#060d0d', fg='white', font=('Cosmic Alien',  20))
    canvas.create_window(640, 420, window=label700)
    label4 = Label(window, text=' Pause the game using the pause Button ', bg='#060d0d', fg='white', font=('Cosmic Alien',  20))
    canvas.create_window(640, 475, window=label4)
    button1 = Button(window, text=' Menu ', bg='#060d0d', fg='white', font=('Times', 20), command=Menu)
    canvas.create_window(640, 550, window=button1)
    button2 = Button(window, text=' Game Start', bg='#060d0d', fg='white', font=('Times', 20), command=Name_entre)
    canvas.create_window(640, 600, window=button2)
    canvas.pack()


def Menu():
    # starting point of the game and this part display the menu
    configer()
    game_back()
    label5 = Label(window, text=' Welcome to Snake in the Space', bg='#060d0d', fg='#5794A7', font=('Cosmic Alien',  35))
    canvas.create_window(640, 100, window=label5)
    button5 = Button(window, text='Begin the Snake Run  ', bg='#060d0d', fg='#5D6D7E', font=('Times', 25), command=ball_maker)
    canvas.create_window(640, 250, window=button5)
    button6 = Button(window, text=' Exit the Game if Afraid   ', bg='#060d0d', fg='white', font=('Times', 25), command=Exit)
    canvas.create_window(640, 350, window=button6)
    button3 = Button(window, text=' View the instructions ', bg='#060d0d', fg='white', font=('Times', 25),  command=instruction)
    canvas.create_window(640, 450, window=button3)
    button4 = Button(window, text=' View the LeaderBoard ', bg='#060d0d', fg='white', font=('Times', 25), command=leader_board)
    canvas.create_window(640, 550, window=button4)
    canvas.pack()

leader_board()
# updated()
# Menu()
# Name_entre()
window.mainloop()

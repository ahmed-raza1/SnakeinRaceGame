from tkinter import *
from random import randint as rand
from time import *


global score
score = 0
global entry1
global entry2
global is_paused
is_paused = False
global canvas
global high_score
global x, y, my_image, shooter_pos
global invader 
# invader = []

window = Tk()
window.geometry("1280x720")
window.title("Snake in the Space")
icon = PhotoImage( file = r'snake.png')
window.iconphoto(False, icon)
canvas2 = Canvas(window, width = 1280 , height = 720, bg = 'black')

def tog_pause(event):
	#this function just pause the game

	global is_paused

	if is_paused == True:
		is_paused = False

	else:
		is_paused = True

	return

def left(event):
	global my_image
	x = -10
	y = 0
	canvas.move(my_image, x , y)
	canvas.pack()

def right(event):
	global my_image
	x = 10
	y = 0
	canvas.move(my_image, x , y)
	canvas.pack()

canvas = Canvas(window, width = 1280 , height = 720, bg = 'black')

def ball_maker():
	#this part deals wit making balls of different colours and number of ball adnsize depend on difficulty level chosen
	global shooter_pos
	global canvas2
	global score
	global is_paused
	global my_image
	# game_back()
	num_balls = 1
	diameter = 30

	txt = " Score : " + str(score)
	scoreText = canvas2.create_text(50,25, fill = "white", font= ("Times 20 italic bold"), text = txt)



	# ball = []

	colour = ["purple", "maroon", "green", "blue"]
	
	img = PhotoImage(file = 'shooter.gif')
	z = Canvas(window)
	z.img = img
	my_image = canvas2.create_image(400, 690, anchor = CENTER , image = img)
	shooter_pos = canvas2.coords(my_image)
	# window.bind("v", shooter)
	window.bind("<Left>", left)
	window.bind("<Right>", right)


	for i in range(num_balls):
		c_col = rand(0,3)
		x = rand(20, 1280)
		y = rand(20, 550)

		xy = (x, y, x+diameter, y+diameter)

		ball = canvas2.create_oval(xy, fill=colour[c_col])

	canvas2.pack()

	x = [1] * num_balls
	y = [1] * num_balls
 
	window.bind("<p>", tog_pause)


	while True:
		pos = canvas2.coords(ball)
		if not is_paused :

 
				# pos = canvas2.coords(ball)

				if pos[3] > 715 or pos[1] < 0:
					y[i] = -y[i]

				if pos[0] < 0 or pos[2] > 1280:
					x[i] = -x[i]

				canvas2.move(ball, x[i], y[i])
				sleep(0.001)
				window.update()
		else :
			window.update()

def Menu():
	#starting point of the game and this part display the menu
	configer()
	label5 = Label(window , text = ' Welcome to Snake in the Space' , bg = '#060d0d', fg = '#5794A7' , font = ('Cosmic Alien' , 35))
	canvas.create_window(640, 100, window =label5)
	button5 = Button(window , text = 'Begin the Snake Run  ' , bg = '#060d0d', fg = '#5D6D7E' , font = ('Times' , 25), command = ball_maker)
	canvas.create_window(640, 250, window =button5)
	button6 = Button(window , text = ' Exit the Game if Afraid   ' , bg = '#060d0d', fg = 'white' , font = ('Times' , 25),command = Exit)
	canvas.create_window(640, 350, window =button6)
	button3 = Button(window , text = ' View the instructions ' , bg = '#060d0d' , fg = 'white' , font = ('Times' , 25),  command = instruction)
	canvas.create_window(640, 450, window =button3)
	button4= Button(window ,text = ' View the LeaderBoard ' , bg = '#060d0d' , fg = 'white' , font = ('Times' , 25), command = leader_board)
	canvas.create_window(640, 550, window =button4)
	canvas.pack()

ball_maker()
window.mainloop()
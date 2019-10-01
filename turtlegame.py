from turtle import* 

scoreturtle = Turtle()
myScreen= scoreturtle.getscreen()
scoreturtle.penup()
scoreturtle.goto(myScreen.window_width() / 2 - 200, myScreen.window_height() / 2- 50)
scoreturtle.hideturtle()
score = 0

def updateScore():
	scoreturtle.clear()
	scoreturtle.write("Score: " + str(score), False, "left", font= ("Arial", 20, "normal"))

	updateScore()

	myScreen.mainloop()
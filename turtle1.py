import turtle

t = turtle.Pen()
t.color('red')
t.circle(50)
t.color('white')
t.forward(100)
t.color('blue')
t.circle(50, steps=4)
t.color('white')
t.forward(25)
t.color('green')
t.right(75)
t.forward(100)
 
for i in range(4):
    t.right(144)
    t.forward(100)
     
turtle.done()

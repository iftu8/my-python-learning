import turtle
import colorsys

# স্ক্রিন সেটআপ
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("The Mystic Eye - Created by Iftu8")

# টার্টল সেটআপ
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

hue = 0.0

# গোপন ইল্যুশন প্যাটার্ন তৈরি
for i in range(160):
    # রঙের ম্যাজিক (রং পরিবর্তন হওয়ার জন্য)
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    hue += 0.006
    
    # জ্যামিতিক ফর্মুলা
    t.right(i)
    t.circle(50, i)
    t.forward(i)
    t.right(90)

# স্ক্রিন ধরে রাখার জন্য
turtle.done()

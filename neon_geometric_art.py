import turtle
import colorsys

# --- Screen Setup ---
screen = turtle.Screen()
screen.bgcolor("black")  # Dark background for neon colors
screen.title("Cyberpunk Neon Geometric Mandala")
screen.setup(width=800, height=800)

# --- Turtle Setup ---
artist = turtle.Turtle()
artist.speed(0)  # Maximum drawing speed
artist.hideturtle()
turtle.tracer(0, 0)  # Disables animation lag for instant complex rendering

# --- Drawing Logic ---
# Number of geometric iterations
total_lines = 210  

print("Generating beautiful neon artwork... Please check your python window!")

for i in range(total_lines):
    # Generating vibrant neon colors using HSV to RGB conversion
    hue = i / total_lines
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    artist.pencolor(color)
    
    # Mathematical geometric patterns
    artist.forward(i * 2)
    artist.right(59)  # Creating a sharp, complex spiral angle
    artist.circle(i * 0.5, 90)  # Adding smooth curved layers
    artist.right(119)
    
    # Adjusting line thickness gradually for a 3D depth effect
    artist.width(i // 100 + 1)

# --- Final Updates ---
turtle.update()  # Renders the complete drawing instantly
print("Artwork generated successfully!")

# Keeps the window open until clicked
screen.exitonclick()

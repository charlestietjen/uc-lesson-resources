import pgzrun

## This code snippet defines the constants WIDTH and HEIGHT as 800 and 600, 
##and then calculates and assigns the tuple CENTER as the center point of the screen based on the WIDTH and HEIGHT.
WIDTH = 800
HEIGHT = 600
CENTER = (WIDTH / 2, HEIGHT / 2)

## This code defines the variable alien as an Actor object with the image "green".
alien = Actor("green")
## This code sets the position of the alien to the center of the screen, with an offset of -50 pixels in the x direction.
alien.pos = CENTER[0] - 50,CENTER[1]

## This code defines a function called draw that clears the screen and then draws the text "Hello, World!" at the center of the screen 
## and draws the alien.
def draw():
    screen.clear()
    screen.draw.text("Hello, World!", CENTER)
    alien.draw()

## This code calls the function pgzrun.go() to start the game.
pgzrun.go()
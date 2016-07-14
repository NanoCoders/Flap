from random import randint
from processing import *
from time import sleep
from math import *
 


def setup():
  frameRate(30)
  size(500, 500)
  
  

class Bird:
  
  def __init__ (self):
    self.x = 100
    self.y = 250
    self.v = 0
    self.playing = 2
  
  def display (self):
    stroke(0)
    fill(252, 33, 73)
    rectMode(CENTER)
    fc = environment.frameCount
    radius = 25 + 2*sin(fc /4)
    ellipse(self.x, self.y, radius, radius);
   
  
  def isTouching(self, wall):
    if (wall.x < bird.x < wall.x + 75):
      
      if (bird.y < wall.y - 75) or (bird.y > wall.y + 75):
        bird.playing = 3
    else:
      bird.playing = 1
      
    
  
class Wall:
  def __init__ (self):
    self.spacing = 75
    self.x = 500
    self.y = randint(10 + self.spacing, 500 - (10 + self.spacing))
   
    
    
  def display (self):
    rectMode(CORNER)
    
    stroke(80)
    fill(240, 103, 133)
    
    rect(self.x, self.y - (500 + self.spacing), 75, 500)
    rect(self.x, self.y + self.spacing, 75, 500)

class Counter:
  def __init__ (self):
    self.count = 0
    self.highscore = 0
    
  def display (self):
    ellipseMode(CENTER)
    fill(300, 300, 300)
    ellipse(10, 10, 200, 100)
    
    fill(270, 50, 100)
    textSize(32)
    text(self.count, 10, 30)
    

class Cloud:
  def __init__ (self):
    self.x = 250
    self.y = 100
    self.size = 4
    
  def display(self):
    
   
    fill(300, 300, 300)
    noStroke()
    
    
    for i in range(self.size):
      if i % 2 == 0:
        ellipse(self.x + (i * 40), self.y + 20, 85, 65)
      else: 
        ellipse(self.x + (i * 40), self.y - 20, 85, 65)
        
      
        
    

x = 10
wall1 = Wall()
wall2 = Wall()
wall2.x = 800

g = .8

bird = Bird()

counter = Counter()

cloud1 = Cloud()
cloud2 = Cloud()
cloud1.x = 500
cloud2.x = 800
cloud2.size = 7


def draw():

  
  if bird.playing == 1:
    
    background(192, 226, 237) 
    
    fill(42, 115, 53)
    
    
    rectMode(CORNER)
    rect(0, 400, 500, 100)
    
    
    
    cloud1.display()
    cloud2.display()
    
    if cloud1.x == -500:
      cloud1.x = 500
      
    if wall2.x == -700:
      wall2.x = 500
    
    cloud1.x -= 2
    cloud2.x -= 2
    
    
    wall1.display()
    
    wall2.display()
    
    
    
    wall1.x -= 5
    wall2.x -= 5 
    
    
    bird.display()
    
    bird.v += g
    
    bird.y += bird.v
    
    
    if wall1.x == -100:
      wall1.x = 500
      
    if wall2.x == -100:
      wall2.x = 500
      
    if (wall1.x == bird.x - 30) or (wall2.x == bird.x -30):
      counter.count += 1
    
    bird.isTouching(wall1)
    if bird.playing == 1:
      bird.isTouching(wall2)
      
    if bird.y < 0 or bird.y > 500:
      bird.playing = 3
    
    counter.display()
      
    
   
      
    
  elif bird.playing == 2:
    background(192, 226, 237)

    textSize(62)
    fill(94, 11, 27)
    text("Click to Start", 80, 250)
    
    textSize(18)
    fill(0, 0, 0)
    text("Flappy Bird by Naveen", 165, 150)
    
  elif bird.playing == 3:
    
    if counter.count >= counter.highscore:
      counter.highscore = counter.count
    
    background(192, 226, 237)

    textSize(62)
    fill(94, 11, 27)
    text("Click to Try Again", 10, 250)
    
    textSize(30)
    fill(0, 0, 0)
    text("Score: " + str(counter.count), 185, 120)
    text("Highscore: " + str(counter.highscore), 145, 170)
    
    wall2.x = 800
    wall1.x = 500
    
    bird.x = 100
    bird.y = 250
    
    
    
    
  
def keyPressed():
  key = keyboard.keyCode
  
  if key == UP or key == 32:
    bird.v = -10
  elif key == 82:
    bird.playing = 3
    
    
def mousePressed(): 
  if 0 < mouseX() < 500 and 0 < mouseY() < 500:
    if bird.playing == 3:
      counter.count = 0
    bird.playing = 1
    
  bird.v = -10




  

  
  
run()

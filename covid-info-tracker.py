# importing the libraries
from covid import Covid
import pygame

# initializing
pygame.init()
covid = Covid()

# data for the world
ta = f"Total active cases in the world: {covid.get_total_active_cases()}"
tr = f"Total recovered cases in the world: {covid.get_total_recovered()}"
td = f"Total deaths in the world: {covid.get_total_deaths()}"

# load background
background = pygame.image.load('covid.jpg')

# taking input for country name 
# getting data according to country name
# data will be stored as a dictionary
country = input("Enter your country name : ")
cases = covid.get_status_by_country_name(country)

# setting font and font size
covid_font = pygame.font.Font('freesansbold.ttf', 18)

# running status variable
running = True

# creating a 400*400 screen
screen = pygame.display.set_mode((400, 400))

# title
pygame.display.set_caption('Covid info Tracker @ankush_singh_gandhi')

# main loop
while running:
    z=10
    y=100

    # for loop to quit the 400*400 screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # filling black colour on screen
    screen.fill((0,0,0))

    # background
    screen.blit(background, (0, 0))

    # printing world data on 400*400 screen
    covid_text = covid_font.render(ta, True, (255, 255, 255))
    screen.blit(covid_text, (z,10))
    covid_text = covid_font.render(tr, True, (255, 255, 255))
    screen.blit(covid_text, (z,30))
    covid_text = covid_font.render(td, True, (255, 255, 255))
    screen.blit(covid_text, (z,50))

    # printing country's data using for loop
    for x in cases:
        text = f"{x}: {cases[x]}"
        covid_text = covid_font.render(text, True, (255, 255, 255))
        screen.blit(covid_text, (z,y))
        y+= 20

    # updating display
    pygame.display.update()
pygame.quit()
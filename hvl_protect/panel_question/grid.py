import pygame
import random
import math
from inventory.item.energy import Energy

PADDING = 40
LINE_WIDTH = 96

class Grid:
    def __init__(self, screen, energy_manager: Energy, base=[0,0]) -> None:
        self.base = base
        self.screen = screen
        self.color = "lightblue4"
        self.width = screen.get_width()
        self.height = int(screen.get_height()*(1/3))
        self.question = self.getQuestion()
        self.selection = 0
        self.last_key = None
        self.answer_screen = False
        self.energy_manager = energy_manager

    def update(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.base[0], self.base[1], self.width, self.height))

        if self.answer_screen:
            self.displayWrong()
        else:
            # render two rectangles as layout for the question and options
            pygame.draw.rect(self.screen, "grey", pygame.Rect(self.base[0] + 4, self.base[1] + 4, self.width - 8, self.height - 8))
            pygame.draw.rect(self.screen, "lightblue4", pygame.Rect(self.base[0] + 8, self.base[1] + 8, self.width - 16, self.height - 16))
            
            # display the question
            self.displayQuestion()


        # grab keyboard input for left and right through a and d
        keys = pygame.key.get_pressed()
        if keys != self.last_key:
            self.last_key = keys
            if keys[pygame.K_a]:
                self.changeSelection("left")
            elif keys[pygame.K_d]:
                self.changeSelection("right")
            elif keys[pygame.K_SPACE]:
                if self.answer_screen:
                    self.answer_screen = False
                    self.question = self.getQuestion()
                    self.selection = 0
                else:
                    if self.verifyAnswer():
                        self.energy_manager.add_energy(3)
                        self.question = self.getQuestion()
                        self.selection = 0
                    else:
                        self.answer_screen = True
            

    def displayWrong(self):
        # display red background with "wrong" text for 4 seconds
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.base[0] + 8, self.base[1] + 8, self.width - 16, self.height - 16))

        # display the question
        pygame.font.init()
        myfont = pygame.font.Font('assets/geo_regular.ttf', 30)
        text_surface = myfont.render("Wrong answer!", False, (255, 255, 255))
        self.screen.blit(text_surface, (self.base[0] + PADDING, self.base[1] + 2*PADDING))
    

    def changeSelection(self, direction):
        if direction == "left":
            if self.selection > 0:
                self.selection -= 1
        elif direction == "right":
            if self.selection < len(self.question)-3:
                self.selection += 1


    def getQuestion(self):
        
        # load a question from the questions csv file
        questions = []
        with open("assets/questions_cat1.csv", "r") as file:
            for line in file:
                questions.append(line.strip().split(","))

        # pick a random question
        question = random.choice(questions)

        return question
    

    def verifyAnswer(self):
        return self.question[self.selection+1] == self.question[len(self.question)-1]
        


    def displayQuestion(self):

        # display the question
        pygame.font.init()
        myfont = pygame.font.Font('assets/geo_regular.ttf', 30)

        # select sections of 60 characters from the question for
        question_wrapped = []
        if len(self.question[0]) < LINE_WIDTH:
            question_wrapped.append(self.question[0])
        else:
            for i in range(0, math.ceil(len(self.question[0])/LINE_WIDTH)):
                end_idx = LINE_WIDTH+i*LINE_WIDTH
                if end_idx > len(self.question[0]):
                    end_idx = len(self.question[0])

                question_wrapped.append(self.question[0][0+i*LINE_WIDTH:end_idx])
    
        for i in range(0, len(question_wrapped)):
            text_surface = myfont.render(question_wrapped[i], False, (255, 255, 255))
            self.screen.blit(text_surface, (self.base[0] + PADDING, self.base[1] + (i+1)*PADDING))

        # divide space into equally sized sections
        offset = int((self.width - 16 - self.base[0] + 8) / (len(self.question)-2))
        for i in range(0, len(self.question)-2):
            if self.selection == i:
                pygame.draw.polygon(self.screen, "white", ((self.base[0] + PADDING + i*offset, self.base[1] + 4*PADDING+10),(self.base[0] + PADDING + 12 + i*offset, self.base[1] + 4*PADDING+16),(self.base[0] + PADDING + i*offset, self.base[1] + 4*PADDING + 22)))

            text_surface = myfont.render(self.question[i+1], False, (255, 255, 255))
            self.screen.blit(text_surface, (self.base[0] + PADDING+24 + i*offset, self.base[1] + 4*PADDING))


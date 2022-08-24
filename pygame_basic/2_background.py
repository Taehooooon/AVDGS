from cgitb import scanvars
from turtle import _Screen
import pygame

pygame.init() #초기화(반드시 필요)

#화면 크기 설정
screen_width = 640 #가로
screen_height = 480 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hoooooni's Game") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("/Users/ththth/PythonWorkspace/pygame_basic/background.jpg")


#이벤트 루프
running = True #게임이 진행중인가?
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    pygame.display.update()#게임 화면을 다시 그리기 필수호출
#pygame 종료
pygame.quit()
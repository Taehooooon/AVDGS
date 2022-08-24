import pygame
################################################
#기본 초기화
pygame.init() #초기화(반드시 필요)

#화면 크기 설정
screen_width = 640 #가로
screen_height = 480 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hoooooni's Game") #게임 이름

#FPS
clock = pygame.time.Clock()
################################################

#사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트 등)
#배경 이미지 불러오기
background = pygame.image.load("/Users/ththth/PythonWorkspace/pygame_basic/background.jpg")

#스프라이트 불러오기
character = pygame.image.load("/Users/ththth/PythonWorkspace/pygame_basic/background.jpg")
character_size = character.get_rect().size
character_width = character_size[0]

#이벤트 루프
running = True #게임이 진행중인가?
while running :
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    pygame.display.update()#게임 화면을 다시 그리기 필수호출
#pygame 종료
pygame.quit()
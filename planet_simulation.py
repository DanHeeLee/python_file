import pygame
import math
from PIL import Image


# 초기화

pygame.init()


# 화면 크기 설정
width, height = 1200, 1000
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('spacebg.png')


# 색상 정의
white = (0, 0, 0)

# 타원의 초기 위치와 속도 설정
a = width // 2
b = height // 2


angle = 0
velocity = 2 * math.pi / 120  # 1회전을 60초 동안 완료하도록

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 타원의 새로운 위치 계산
    x = a * math.cos(angle) + width // 2
    y = b * math.sin(angle) + height // 2

    x2 = a * math.cos(angle+3) + width // 2
    y2 = b * math.sin(angle+3) + height // 2

    x3 = a * math.cos(angle+4) + width // 2
    y3 = b * math.sin(angle+4) + height // 2

    x4 = a * math.cos(angle+5) + width // 2
    y4 = b * math.sin(angle+5) + height // 2

    x5 = a * math.cos(angle+6) + width // 2
    y5 = b * math.sin(angle+6) + height // 2


    x6 = a * math.cos(angle+7) + width // 2
    y6 = b * math.sin(angle+7) + height // 2   


    x7 = a * math.cos(angle+8) + width // 2
    y7 = b * math.sin(angle+8) + height // 2

    
    x8 = a * math.cos(angle+9) + width // 2
    y8 = b * math.sin(angle+9) + height // 2
    # 화면 지우기
    screen.fill(white)


    # 타원 그리기
    pygame.draw.circle(screen, (255, 51, 51), (int(x3), int(y3)), 5) #수성
    pygame.draw.circle(screen, (255, 128, 0), (int(x4), int(y4)), 8) # 금성
    pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), 10) # 지구
    pygame.draw.circle(screen, (255, 255, 0), (int(x2), int(y2)), 8) # 화성
    pygame.draw.circle(screen, (0, 255, 255), (int(x5), int(y5)), 20) # 목성
    pygame.draw.circle(screen, (0, 0, 255), (int(x6), int(y6)), 20) # 토성
    pygame.draw.circle(screen, (178, 102, 255), (int(x7), int(y7)), 30) # 천왕성   
    pygame.draw.circle(screen, (255, 204, 229), (int(x8), int(y8)), 35) # 해왕성
    pygame.draw.circle(screen, (255, 225, 204), (width/2,height/2), 70) 

    pygame.display.flip()

    angle += velocity

    clock.tick(60)  # 초당 60프레임으로 제한

pygame.quit()

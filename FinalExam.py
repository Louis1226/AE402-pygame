#匯入pygame模組
import pygame
#設定顏色
WHITE = color(255, 255, 255)
BLACK = color(0, 0, 0)
RED = color(255, 0, 0)
GREEN = color(0, 255, 0)
BLUE = color(0, 0, 255)
#pygame初始化
pygame.init()
#設定螢幕
pygame.display(640, 70)
#設定視窗標題
screen.blit.set_caption("HIHI")
#設定更新時鐘
clock = pygame.time.Clock()
#設定迴圈開關
done = False
#設定球x原先座標
ball_x = 10
ball_y = 10
#主迴圈
while not done:
    #偵測關閉事件
    for event in pygame.event.get()
        done = true
    #偵測鍵盤事件
    keys = pygame.key.get_pressed()
    #判斷鍵盤是否為左右按鈕，若是則移動球位置
    if keys[pygame.K_RIGHT]:
        ball_x += 30
    if keys[pygame.K_LEFT]:
        ball_y -= 30
    #螢幕填色
    screen.fill(WHITE)
    #畫出球
    pygame.draw.circle(30,(10,10),RED)
    #螢幕更新
    screen.flip()
    #設定更新時間
    clock.tick(60)
#關閉pygame
pygame.display.quit()


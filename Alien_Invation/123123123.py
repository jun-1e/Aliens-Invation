import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("按键测试 - 点击后按任意键")
    clock = pygame.time.Clock()
    
    # 创建一个红色方块
    rect = pygame.Rect(375, 275, 50, 50)
    moving_left = False
    moving_right = False
    
    print("="*50)
    print("程序运行中...")
    print("请点击窗口，然后按 A 和 D 键")
    print("="*50)
    
    while True:
        # 方法1：使用 pygame.event.get()
        for event in pygame.event.get():
            print(f"事件: {event}")  # 打印所有事件
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(f"KEYDOWN: {event.key}")
                if event.key == pygame.K_a:
                    moving_left = True
                    print("向左移动")
                elif event.key == pygame.K_d:
                    moving_right = True
                    print("向右移动")
            elif event.type == pygame.KEYUP:
                print(f"KEYUP: {event.key}")
                if event.key == pygame.K_a:
                    moving_left = False
                elif event.key == pygame.K_d:
                    moving_right = False
        
        # 移动
        if moving_left and rect.left > 0:
            rect.x -= 5
        if moving_right and rect.right < 800:
            rect.x += 5
        
        # 绘制
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (255, 0, 0), rect)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
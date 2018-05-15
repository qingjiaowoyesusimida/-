import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,400,600)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite):
		def __init__(self,image_name,speed =2):
			#调用父级方法
			super().__init__()
			#加载图像
			self.image = pygame.image.load(image_name)
			#设置尺寸
			self.rect = self.image.get_rect()
			#记录速度
			self.speed = speed
		def update(self):
			self.rect.y +=self.speed
class Background(GameSprite):
	def __init__(self,is_alt=False):
		image_name = './4.png'
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super().update()
		if self.rect.y >SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class Enemy(GameSprite):
	def __init__(self):
		image_name ='./9.png'
		super().__init__(image_name)
		self.speed = random.randint(1,3)
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)#随机位置
		self.rect.bottom = 0
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
	def __del__(self):
		print('消除敌机')
#英雄精灵
class Hero(GameSprite):
	def __init__(self):
		#设置初始位置
		super().__init__('./1.png',0)
		self.rect.centerx= SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullets = pygame.sprite.Group()
		self.speed1 = 0
	def update(self):
	#飞机水平移动
		self.rect.x += self.speed
		self.rect.y += self.speed1
		if self.rect.left<0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		if self.rect.y<0:
			self.rect.y = 0
		if self.rect.bottom > SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height
	def fire(self):
		print('发射子弹')
		for i in (1,2,3):
			#创建子弹精灵
			bullet = Bullet()
			bullet1 = Bullet()
			bullet2 = Bullet() 
			
			bullet.rect.bottom = self.rect.y + 20
			bullet.rect.centerx = self.rect.centerx
			bullet1.rect.bottom = self.rect.y + 30
			bullet1.rect.centerx = self.rect.centerx + 15
			bullet2.rect.bottom = self.rect.y + 30
			bullet2.rect.centerx = self.rect.centerx - 15
			#将精灵添加到精灵组
			self.bullets.add(bullet,bullet1,bullet2)
class Bullet(GameSprite):
	def __init__(self):
		super().__init__('./23.png',-2)
	def update(self):
		super().update()
		if self.rect.bottom <0:
			self.kill()
	def __def__(self):
		print('消除子弹')
	

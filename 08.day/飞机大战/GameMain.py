import pygame
HERO_FIRE_EVENT = pygame.USEREVENT+1 #英雄发射子弹事件
from PlanSprite import *
class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		self.wanjia1 = 0
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		self.enemy_group = pygame.sprite.Group()
		pygame.time.set_timer(HERO_FIRE_EVENT,500)
	def __create_sprites(self):
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)
	def start_game(self):
		print('游戏开始...')
		while True:
			self.clock.tick(FRAME_PER_SEC)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			self.print_score()
			pygame.display.update()
	def __event_handler(self):
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 8
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -8
		else:
			self.hero.speed = 0
		if keys_pressed[pygame.K_UP]:
			self.hero.speed1 = -8
		elif keys_pressed[pygame.K_DOWN]:
			self.hero.speed1 = 8
		else:
			self.hero.speed1 = 0
		for event in pygame.event.get():
			#判断是否退出游戏
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:#定时器事件
				enemy = Enemy()
				self.enemy_group.add(enemy)
			elif event.type == HERO_FIRE_EVENT:#发射子弹
				self.hero.fire()
	def __check_collide(self):
		if pygame.sprite.groupcollide(self.enemy_group,self.hero.bullets,True,True):
			self.wanjia1 +=1
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		if len(enemies)>0:
			self.hero.kill()
			PlanGame.__game_over()
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)
	
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullets.update()
		self.hero.bullets.draw(self.screen)
	def print_score(self):
		pygame.font.init()
		pos1 = (100,0)
		color =(255,255,255)
		text1 = 'player1:'+str(self.wanjia1)
		cur_font = pygame.font.SysFont('楷体',30)
		text_fort1 = cur_font.render(text1,1,color)
		self.screen.blit(text_fort1,pos1)
	@staticmethod
	def game_over():
		pygame.quit
		exit()
if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()

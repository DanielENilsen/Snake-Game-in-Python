import pygame, sys, random

class Food(object):

	def __init__(self, window, screen_x, screen_y):
		self.window = window
		self.screen_x = screen_x
		self.screen_y = screen_y
		self.food_arr = [random.randint(0,(self.screen_x-10)//10) *10 , random.randint(0,(self.screen_y-10)//10)*10]
		self.foodColor = (45, 245, 20)

	def draw_food(self) -> None:		
		pygame.draw.rect(self.window,self.foodColor,(self.food_arr[0],self.food_arr[1],10,10))


class Snake(object):

	def __init__(self, window, screen_x, screen_y):
		self.window = window 
		self.screen_x = screen_x
		self.screen_y = screen_y
		self.snakeColor = (255,255,255)
		self.snake_head = [self.screen_x, self.screen_x]
		self.snake_body =[ [self.screen_x, self.screen_y], [self.screen_x-1,self.screen_y], [self.screen_x-2,self.screen_y]]
		self.direction = 'rigth'		

	def draw_snake(self) ->None: 
		for snx_block in self.snake_body:
			pygame.draw.rect(self.window, self.snakeColor,(snx_block[0],snx_block[1],10,10))
		self.snake_movement()

	def snake_movement(self) -> None:

		if self.direction == 'rigth':
			self.snake_head[0] += 10
		if self.direction == 'left':
			self.snake_head[0] -= 10
		if self.direction == 'up':
			self.snake_head[1] -= 10
		if self.direction == 'down':
			self.snake_head[1] += 10		

	def snake_direction(self) -> None:

		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT] and self.direction != 'left':
			self.direction = 'rigth'
		if keys[pygame.K_LEFT] and self.direction != 'rigth':
			self.direction = 'left'
		if keys[pygame.K_UP] and self.direction != 'down':
			self.direction = 'up'
		if keys[pygame.K_DOWN] and self.direction != 'up':
			self.direction = 'down'

	def snake_collition_food(self, foodObject) -> None:

		self.snake_body.insert(0,list(self.snake_head))
		
		if self.snake_head[0] == foodObject.food_arr[0] and self.snake_head[1] == foodObject.food_arr[1]:
			foodObject.food_arr[0] = random.randint(1,foodObject.screen_x//10) *10
			foodObject.food_arr[1] = random.randint(1,foodObject.screen_y//10) *10			
		else:
			self.snake_body.pop()

	def snake_collition(self, xWall, yWall) -> None:

		if self.snake_head[0] >= xWall or self.snake_head[0] < 0:
			sys.exit()

			
		if self.snake_head[1] >= yWall or self.snake_head[1] < 0:
			sys.exit()

		if [self.snake_head[0], self.snake_head[1]] in self.snake_body[1:]:
			sys.exit()


class PyGameEngine(object):
	pygame.init()
	def __init__(self):
		self.screen_w = int(600)
		self.screen_h = int(400)
		self.window = pygame.display.set_mode((self.screen_w,self.screen_h))
		self.clock = pygame.time.Clock()
		self.backgroundColor = (21, 21, 28)
		self.food = Food(self.window, self.screen_w, self.screen_h)
		self.snake = Snake(self.window, self.screen_w/4, self.screen_h/2)
		self.engine()

	def engine(self) -> None:

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				self.snake.snake_direction()

			self.window.fill(self.backgroundColor)
			self.food.draw_food()
			self.snake.draw_snake()
			self.snake.snake_collition_food(self.food)
			self.snake.snake_collition(self.screen_w, self.screen_h)

			pygame.display.update()
			self.clock.tick(25)
 

if __name__ == "__main__":
	PyGameEngine()

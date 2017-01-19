class Bird(object):
	def chirp(self):
		print("make sound")

class Chicken(Bird):
	def chirp(self):
		print("ji")

bird = Bird()
bird.chirp()

summer = Chicken()
summer.chirp()
class Bird(object):
	"""docstring for Bird"""
	def __init__(self, sound):
		self.sound = sound
		print("My sound is:", sound)

	def chirp(self):
		print(self.sound)

summer = Bird("ji")
summer.chirp()
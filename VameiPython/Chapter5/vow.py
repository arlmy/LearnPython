class Vow(object):
	def __init__(self, text):
		self.text = text
	def __enter__(self):
		self.text = "I say:" + self.text + "!"
		return self
	def __exit__(self, exc_type, exc_value, trackback):
		self.text = self.text + "!"

with Vow("I'm fine") as myVow:
	print(myVow.text)

print(myVow.text)
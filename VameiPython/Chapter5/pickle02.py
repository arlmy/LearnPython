import pickle

class Bird(object):
	have_feather = True
	reprodoction = "egg"

summer = Bird()
with open("summer.pkl", "wb") as f:
	pickle.dump(summer, f)
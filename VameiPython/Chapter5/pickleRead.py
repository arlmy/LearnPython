import pickle

class Bird(object):
	have_feather = True
	reprodoction = "egg"

with open("summer.pkl", "rb") as f:
	summer = pickle.load(f)

print(summer.have_feather)
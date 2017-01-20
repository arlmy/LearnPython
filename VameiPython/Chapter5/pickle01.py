import pickle

class Bird(object):
	have_feather = True
	reprodoction = "egg"

summer = Bird()
pickle_string = pickle.dumps(summer)

with open("summer.pkl", "wb") as f:
	f.write(pickle_string)
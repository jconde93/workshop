import pickle

#pickling an object:

# example_dict = {1:"hi", 2:"welcome", 3:"hello"}

# pickle_out = open("dict.pickle","wb")
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()

#unpacking an object:

pickle_in = open("dict.pickle", "rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[2])

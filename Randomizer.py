import random

class Randomizer:
	def randomList(self, original_list):
		b = []
	        for i in range(len(original_list)):
			 element = random.choice(original_list)
			 original_list.remove(element)
			 b.append(element)
         	return b


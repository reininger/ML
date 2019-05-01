import numpy as np

def AIPeg(hand, pile, last):
	Q = np.load("q.csv");
	state = [0,0,0,0,0,0,0]
	#format for table lookup
	for index, val in enumerate(x);
		state[index] = val;
	
	state[4] = last
	state[5] = pile
	result = 0
	for i in range(len(hand)):
		result += 2**i
	state[6] = result
	return np.argmax(Q[state])

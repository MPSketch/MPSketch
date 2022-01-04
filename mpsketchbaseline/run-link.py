#!/usr/bin/env python

import os

denses = [0.5, 0.6, 0.7, 0.8, 0.9]
datasets = ['blog'];

iterations = [1,2,3,4,5]
turns = [1,2,3,4,5]

method = 'mpsketchbaseline'
os.system("rm "+method);
os.system("g++ -std=c++11 -lm -O3 -march=native -Wall -funroll-loops -ffast-math -Wno-unused-result "+method+".cpp -o "+method+" -lgsl -lm -lgslcblas");

for i_data, data in enumerate(datasets):

	print(data)

	path = "../results/" + data + "/"
	folder = os.path.exists(path)
 
	if not folder:          
		os.makedirs(path) 

	for turn in turns:
		for dense in denses:
			for iteration in iterations:
				os.system("./"+method+" -network ../data/" + data + "/" + data + ".adjlist." + str(dense) + \
					" -feature ../data/" + data + "/features.txt -hashdim 200 -iteration " + str(iteration) + \
					" -embedding ../results/" + data + "/" + data + ".dense." + str(dense) +"." +method + ".iteration." +str(iteration) + ".embedding.turn." +str(turn) + 
					" -time ../results/" + data + "/" + data + ".dense." + str(dense) + "."+ method+ ".iteration." + str(iteration) + ".time.turn." +str(turn));


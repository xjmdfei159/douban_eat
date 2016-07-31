__author__ = 'hzfanyaling'
#!/usr/bin/env python

import random
sword = "1:9,30|2:9,30|3:99,300|5:4,15|9:2,9"
sword_split = sword.split('|')

type_weights_map = {}
result_weights_map = {}
for data in sword_split:
	attr_type,weight_type = data.split(':')
	type_weights_map[attr_type] = weight_type.split(',')

sword_attr_time = []    #sword prob list
base_num = 1
sword_simu_num = 0
sword_max_num = 15
sword_extra_num = 0

#sword num
sword_fif_num = 1
sword_fif_coe = 0.05
sword_ten_num = 1
sword_ten_coe = 0.01

sword_min_coe = 0.1
sword_max_coe = 0.5
sword_baodi_coe = 0.3  #baodi

sword_result = sword_fif_num*sword_fif_coe + sword_ten_num*sword_ten_coe

def attr_real():
	for k,v in type_weights_map.items():
		for i in range(2):
			type_weights_map[k][i] = float(type_weights_map[k][i])*(sword_result + sword_min_coe)
			#print(type_weights_map)

def sword_attr_func():
	attr_real()
	for i in range(5):
		sword_attr_num = 1 + random.randint(0,3)
		sword_attr_time.append(sword_attr_num)
		#print(sword_attr_time)
	sword_simu_num = sum(sword_attr_time)
	# compare sword_simu_num vs sword_max_num
	if (sword_simu_num == sword_max_num):
		sword_attr_cal()

def sword_attr_cal():

	probA = []
	test = []
	for k in type_weights_map.iterkeys():
		haha = type_weights_map[k]
		test.append(haha)

	print(test)
	print(sword_attr_time)
	for i in range(5):
		for j in range(sword_attr_time[i]):
			kabi = round(random.uniform(test[i][0],test[i][1]),2)
			probA.append(kabi)
	print(probA)


def main():
	sword_attr_func()
	sword_attr_cal()


if __name__ == '__main__':
	main()

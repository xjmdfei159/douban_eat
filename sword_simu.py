__author__ = 'hzfanyaling'

import random

sword = "1:9,30|2:9,30|3:99,300|5:4,15|9:2,9"
sword_split = sword.split('|')
sword_prob = []
prob1_num = 1
prob2_num = 1
prob3_num = 1
prob4_num = 1
prob5_num = 1
sword_prob_num = [prob1_num,prob2_num,prob3_num,prob4_num,prob5_num]
sword_beat_max_num = 4
sword_beat_num = 15

for i in range(5):
	sword_prob_sp = sword_split[i]
	sword_prob.append(sword_prob_sp)

for i in range(1):
	num = random.randint(0,sword_beat_num-5)
	print(num)
	if(num>sword_beat_max_num-1):
		num = sword_beat_max_num - 1
		print(num)


def main():

 print('haha')



if __name__ == '__main__':
	main()
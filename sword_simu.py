__author__ = 'hzfanyaling'
#!/usr/bin/env python



import random

sword = "1:9,30|2:9,30|3:99,300|5:4,15|9:2,9"
sword_split = sword.split('|')
sword_prob = []
base_num = 1
probA_num = 1+random.randint(0,3)
probB_num = 1+random.randint(0,3)
probC_num = 1+random.randint(0,3)
probD_num = 1+random.randint(0,3)
probE_num = 1+random.randint(0,3)
sword_prob_num = [probA_num,probB_num,probC_num,probD_num,probE_num]
sword_simu_num = sum(sword_prob_num)
sword_extra_num = 0
sword_max_num = 15
print(sword_prob_num)
print(sword_prob_num.index(min(sword_prob_num)))
def simu_num():
	if(sword_simu_num==sword_max_num):
		print(sword_prob_num)
	elif (sword_simu_num<15):
		sword_extra_num = sword_max_num - sword_simu_num

		print('sword_simu_num' + str(sword_simu_num))
	else:

		sword_extra_num = sword_simu_num - sword_max_num

		print(sword_extra_num)
def main():
	simu_num()



if __name__ == '__main__':
	main()
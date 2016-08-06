import sys
import operator
n, m = raw_input("Enter the number of places and the number of paths").split(' ')
n = int(n)
m = int(m)
state_table = {}
for i in range(1, n):
	state_table[i] = {}
	state_table[i]['dist'] = sys.maxint
	state_table[i]['visit_status'] = 'No'
	state_table[i]['previous_station'] = 'nil'
state_table[0] = {}
state_table[0]['dist'] = 0
state_table[0]['visit_status'] = 'No'
state_table[0]['previous_station'] = 0
def get_next_place():
	minimum = sys.maxint
	global state_table
	for i in state_table:
		if state_table[i]['dist'] < minimum and state_table[i]['visit_status'] == 'No':
			minimum = state_table[i]['dist']
			place = i
	return place
	
distance_matrix = []
for i in range(0, n):
    distance_matrix.append([])
    for j in range(0 , n):
        if i == j:
            distance_matrix[i].append(0)
            continue
        print "Enter the route distance from {} to {}".format(i, j)
        route_distance = input()
        distance_matrix[i].append(route_distance)
while(1):
	place = get_next_place()
	for index, i in enumerate(distance_matrix[place]):
		if i > 0:
			if state_table[index]['dist'] >  state_table[place]['dist'] + i:
				state_table[index]['dist'] = state_table[place]['dist'] + i
				state_table[index]['previous_station'] = place
		state_table[place]['visit_status'] = 'Yes'
	print state_table
	for i in state_table:
		if state_table[i]['visit_status'] == 'Yes':
			terminate_check_flag = 1
		else:
			terminate_check_flag = 0
	if terminate_check_flag == 1:
		break










    

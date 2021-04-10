spiralized_matrix_values = [x for x in range(1,251001)]
print(spiralized_matrix_values)
print ([x for x in spiralized_matrix_values[1:9]])
print ([x for x in spiralized_matrix_values[9:25]])
print ([x for x in spiralized_matrix_values[25:49]])
#I don't know how to code this by looping. Brute forcing it will take to long
#I wanted to create a different list containing the different spirals. After 1, each spiral incremets by 8
#After 1, 1st spiral values that you want from the diagonals are increased by 2
#the values will be 3,5,7,9
#for the 2nd spiral the values you want will be 13,17,21,25
#each spiral following the last value from the last spiral, are incremented by 2
    

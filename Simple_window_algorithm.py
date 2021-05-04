# implementing the simple window algorithm using brute force approach
# check readme file for the understanding of the algorithm and it best use

array = str(input('input the numbers separted by commmas\t')) #collecting inputs
array = [int(i) for i in array.split(',')]
K = int(input('input the size of the window\t'))

size_array = len(array)
allowed_comb = size_array - K # this variable represents the possible index the window can be slided to for it to accumalate the window frame
Max_sum = 0

#approach 1
for i in range(allowed_comb + 1):
    Window_sum = 0
    for j in range(K):
        Window_sum  = Window_sum + array[i + j]
        #print('{} + {}'.format( Window_sum ,array[i + j]))
    Max_sum = max(Window_sum, Max_sum)
print(Max_sum)

#approach 2
for i in range(allowed_comb + 1):
    summer = array[i:i+allowed_comb]
    print('{} equals {}'.format(summer,sum(summer)))

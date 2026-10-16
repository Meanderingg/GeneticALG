import numpy as np
import math
import matplotlib.pyplot as plt
from genetic import encoding, decoding, select, crossover, mutation, fit

def bin_src(no, intervals, low, high):
    if low == high:
        return low

    mid = low + (high - low) // 2

    if no >= intervals[mid] and no < intervals[mid + 1]:
        return mid + 1
    
    elif no < intervals[mid]:
        return bin_src(no, intervals, low, mid)

    else:
        return bin_src(no, intervals, mid, high)

parameters = open("parameters.in")
try:
    output = open("output.txt", "x")
except FileExistsError:
    output = open("output.txt", "w")

chromosome_nr = int(parameters.readline().split()[0])
minimum, maximum = (int(i) for i in parameters.readline().split()[:2])
coef1, coef2, coef3 = (int(i) for i in parameters.readline().split()[:3]) 
precision = int(parameters.readline().split()[0])
PComb = float(parameters.readline().split()[0])
PMut = float(parameters.readline().split()[0])
steps = int(parameters.readline().split()[0])

generation = sorted(np.random.uniform(minimum, maximum, chromosome_nr).tolist())
binary = [encoding(minimum, maximum, precision, number) for number in generation]
ch_len = math.ceil(math.log2((maximum - minimum) * (10**precision)))
fitness = [fit(coef1, coef2, coef3, i) for i in generation]
selection = [i/sum(fitness) for i in fitness]
cummulative = select(coef1, coef2, coef3, len(generation), generation)
print("Bi: ", binary, "Xi: ", generation, "fit: ", fitness, "Selection probability: ", 
      selection, "Intervals: ", cummulative, sep='\n', file=output)

for step in range(steps):
    selected = []
    max_index = fitness.index(max(fitness))
    selected.append(binary[max_index])
    nums = np.random.rand(chromosome_nr - 1)
    for no in nums:
        index = bin_src(no, cummulative, 0, len(cummulative) - 1)
        selected.append(binary[index - 1])
        if step == 0:
            print(no, cummulative[index - 1], cummulative[index], generation[index - 1], file=output)

    for i in range(1, chromosome_nr - 1, 2):
        if np.random.rand() < PComb:
            cross_index = np.random.randint(1, ch_len)
            mut1, mut2 = crossover(ch_len, cross_index, selected[i], selected[i + 1])
            selected[i] = mut1
            selected[i + 1] = mut2
            if step == 0:
                print("Recombinare: ", selected[i], selected[i+1], cross_index, mut1, mut2, file=output)

    if step == 0:
        print("Populatia dupa recombinare: ", selected, sep='\n', file=output) 

    for i in range(1, chromosome_nr):
        if np.random.rand() < PMut:
            mut_no = int(np.random.uniform(0, ch_len + 1))
            mut_indexes = (sorted(np.random.randint(0, ch_len + 1, mut_no).tolist()))
            selected[i] = mutation(ch_len, mut_no, selected[i], mut_indexes)

    if step == 0:
        print("Populatia dupa mutatii: ", selected, sep='\n', file=output) 
    

    binary = selected
    generation = [decoding(minimum, maximum, precision, i) for i in selected]
    fitness = [fit(coef1, coef2, coef3, i) for i in generation]
    cummulative = select(coef1, coef2, coef3, len(generation), generation)
    print("Maximum :", max(fitness), file=output)
    print("Media: ", sum(fitness) / len(fitness), file=output)

plt.figure()
xaxis = np.linspace(minimum, maximum, 1000)
yaxis = [ coef1 * x ** 2 + coef2 * x + coef3 for x in xaxis]
plt.plot(xaxis, yaxis)
my = max(fitness)
mx = generation[fitness.index(my)]
plt.plot(mx, my, 'ro')
plt.show()

parameters.close()
output.close()

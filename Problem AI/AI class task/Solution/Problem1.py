'''
1.	Generate 100 random integer and 100 random floating-point numbers and save them in
separate file. Write two separate functions and save integer in random-int.txt, float in random-float.txt

'''

import numpy as np

#Iniger Number Generate,
def generateInt(numberData,fileName):
    IntDataList = []

    for x in range(numberData):
        IntDataList.append(np.random.randint(100))

        file = open(fileName,"w")
        file.write(str(IntDataList))
        file.close()

    return np.array(IntDataList)

#Float Number Generate, 
def generate_float(size,fileName):
    FloatDataStore = []

    for x in range(size):
        FloatDataStore.append(np.random.uniform(100))

        file = open(fileName,"a")
        file.write(str(FloatDataStore))
        file.close()


    return np.array(FloatDataStore)







print("100 Integer Number : ", generateInt(100,"problem6_1_IntNum.txt"))
print("100 Float  Number : ", generate_float(100,"problem6_1_FloatNum.txt"))
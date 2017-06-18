# Answer Question
# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
# Given the following formula,
#  speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
#  Where g = 9.8 m/s^2 (gravitational constant)
# Write a program to read in the data files from disk, it must then print the names
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.
#  $ cat dataset1.csv
#  NAME,LEG_LENGTH,DIET
#  Hadrosaurus,1.2,herbivore
#  Struthiomimus,0.92,omnivore
#  Velociraptor,1.0,carnivore
#  Triceratops,0.87,herbivore
#  Euoplocephalus,1.6,herbivore
#  Stegosaurus,1.40,herbivore
#  Tyrannosaurus Rex,2.5,carnivore
#
#  $ cat dataset2.csv
#  NAME,STRIDE_LENGTH,STANCE
#  Euoplocephalus,1.87,quadrupedal
#  Stegosaurus,1.90,quadrupedal
#  Tyrannosaurus Rex,5.76,bipedal
#  Hadrosaurus,1.4,bipedal
#  Deinonychus,1.21,bipedal
#  Struthiomimus,1.34,bipedal
#  Velociraptor,2.72,bipedal 


# Read both files into two dict
# Process file 2

from heapq import *

def sol():
    A, B = {}, []           # 1. Read files into containers
    with open("dataset1.csv") as f1:
        f1.readline()
        for line in f1:
            fields = line.strip().split(',')
            A[fields[0]] = fields[1:]
        print(A)
        
    with open("dataset2.csv") as f2:
        f2.readline()
        for line in f2:
            B.append(line.strip().split(','))
        print(B)

    hq = []
    for name, stride_length, stance in B:
        if name not in A: continue
        if stance != "bipedal": continue
        leg_length = float(A[name][0])

#  speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
        speed = (( float(stride_length) / leg_length)  - 1 ) * (( leg_length * 9.8 ) ** 0.5)
        heappush(hq, [-speed, name])

    while hq:
        print(hq[0][1], -hq[0][0])
        heappop(hq)

sol()

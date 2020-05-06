import sys

observations = input("enter observations: ")

outFile = open("results.txt", 'w+')

#print input info
outFile.write("Observation sequence Q: " + observations + "\n")
outFile.write("Length of Q: " + str(len(observations)) + "\n")
outFile.write("\n")

h1 = [0.1, 1, 0]
h2 = [0.2, 0.75, 0.25]
h3 = [0.4, 0.50, 0.50]
h4 = [0.2, 0.25, 0.75]
h5 = [0.1, 0, 1]

bags = [h1, h2, h3, h4, h5]

for i in observations:
    #get desired candy index
    candyIndex = 0
    if i == "C":
        candyIndex = 1
    elif i == "L":
        candyIndex = 2
    else:
        print("ERROR: INVALID OBSERVATION")
        sys.exit()
    #calculate the general probability of the candy being chosen from all bags
    genCandyProb = 0
    for j in bags:
        genCandyProb += j[candyIndex] * j[0]
    #Update prior probabilities
    for j in bags:
        j[0] = (j[candyIndex] * j[0])/genCandyProb
bagIndex = 1
#print a posteriori bag probabilities
for i in bags:
    outFile.write("(h" + str(bagIndex) + "|Q)= " + str("{:.5f}".format(round(i[0], 5))) + "\n")
    bagIndex += 1
#print a posteriori candy probabilities
genCandyProb = 0
for i in bags:
    genCandyProb += i[0] * i[1]
outFile.write("\n")
outFile.write("Probability that the next candy we pick will be C, given Q: " + str("{:.5f}".format(round(genCandyProb, 5))) + "\n")
outFile.write("Probability that the next candy we pick will be L, given Q: " + str("{:.5f}".format(round(1- genCandyProb, 5))) + "\n")
    
#HAMMING DISTANCE

def hammingDistanceLoop(sentence1, sentence2):
    distance = 0
    #print("sentence1 =", sentence1)
    #print("sentence2 =", sentence2)
    
    if len(sentence1) == len(sentence2):
        #print("length of sentence1 =", len(sentence1))
        #print("length of sentence2 =", len(sentence2))
        counter = 0
        #print("while {} <= {}".format(counter, len(sentence1)))
        #print("sentence1{} is {}".format(counter, sentence1[counter]))
        #print("sentence2{} is {}".format(counter, sentence2[counter]))
        while counter < len(sentence1): #if string1 and string2 are equal length
            #print("*****COUNTER: {}:".format(counter))
            if sentence1[counter] != sentence2[counter]:
                distance += 1
                #print(distance)

            counter += 1
    else:
        difference = abs(len(sentence1) - len(sentence2))
        minimum = min(len(sentence1), len(sentence2))
        distance = difference + minimum

    return distance

def hammingDistance(sentence1, sentence2):
    #NO LOOPS
    #use filter(), map()


    pass


def main():

    #string1 = "[To be or not to be, that is the question]"
    #string2 = "[To be~orAnoa [OBbej tVat i.Xt<eLju(s2ion]"

    string1 = "Trisha Lapiz"
    string2 = "Tr1$ha L@p!z aaaa"

    print("The Hamming Distance between {} and {} is".format(string1, string2), hammingDistanceLoop(string1, string2))
    print("The Hamming Distance between {} and {} is".format(string1, string2), hammingDistance(string1, string2))

main()

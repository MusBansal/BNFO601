#This program was written to answer the following question: Defines a function that generates random DNA sequences of some specified length given a dict describing the probability distribution of A, C, G, T 
#In this method; I invoked the Random function with the use of random.choices specifically. 

import random

def nseqCreator(seqLen= 4):
  nProb={'A':20,'T':20,'C':30,'G':30} #Dictionary with weights
  seq=''
  randN= random.choices(list(nProb.keys()),weights=list(nProb.values()),k=seqLen) #outputs a list of random choices
  for i in range(len(randN)): #converting list to a single string
    seq+=randN[i]
  return seq

seqRand=nseqCreator(100)
print(seqRand.count("A"))
print(seqRand.count("C"))
print(seqRand.count("G"))
print(seqRand.count("T"))

#test function; unweighted random function.
def trialnseqCreator(seqLen= 4):
  nProb={'A':'.20','T':'.20','C':'.30','G':'.30'}
  seq=''
  for i in range(0,seqLen):
    randN= random.choice(list(nProb))
    seq+=randN
  return seq



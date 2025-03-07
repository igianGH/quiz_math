import math as mt
import random as rn
from collections import defaultdict
from datetime import date
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
matplotlib.rcParams.update({'font.size': 28})

def Qu(line,fgs=(.1, .1),dpi=80):
  plt.figure(figsize=fgs, dpi=dpi)
  plt.grid(False)
  plt.axis('off')
  plt.text(.0,.0,r''+line)
  plt.draw()
  plt.show()

def mquiz():
  Q,A=defaultdict(),defaultdict()

  with open("mtDB.txt",'r') as f:
    nline=0
    for line in f:
      nline+=1
      if(nline%2==1):
        Q[nline//2+1]=line[:-3].replace('\t',' ')
        res=line[-2]
      else:
        A[nline//2]=res,line[:-1].replace('\t',' ')
  N=nline//2
  quiz=rn.sample(range(1,N+1),10)
  vathmos=0
  aa=0
  start=time.time()
  for i in quiz:
    aa+=1
    Qu(Q[i][Q[i].find('.')+1:])
    if(A[i][0]==input("\n> ")):
    #if(A[i][0]==input(str(aa)+'.'+Q[i][Q[i].find('.')+1:]+"\n> ")):
      print("\nΣωστή Απάντηση!\n")
      vathmos+=10
    else:
      print("\nΛάθος Απάντηση:\t"+A[i][1]+'\n')
  print("\n______________________________________\nΗμερομηνία: "+time.strftime("%a, %d %b %Y, %H:%M:%S",time.gmtime(time.time())))
  end=time.time()
  print("\nΤελικός Βαθμός:",vathmos,"/ 100\nΧρόνος:",int(end-start),"seconds")

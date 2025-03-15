import math as mt
import random as rn
from collections import defaultdict
from datetime import date
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from IPython.display import display as idisplay
from IPython.display import Math as iMath
from IPython.display import Latex as iLatex
matplotlib.rcParams.update({'font.size': 25})

def _Q2p(line, fgs=(22,.1),dpi=80):
  #ND rt to plot plus
  if(r"\ltx" not in line):
    Q2p(line,fgs,dpi)
  else:
    pos1=line.find(r"\ltx")
    pos2=line[pos1+4:].find(r"\ltx")+pos1+4
    Q2p(line[:pos1],fgs,dpi)
    print()
    idisplay(iMath(r''+line[pos1:pos2+4].replace('\ltx','$')))
    print()
    _Q2p(line[pos2+4:],fgs,dpi)

def Q2p(line,fgs=(22,.1),dpi=80):
  if(line==''):
    return
  #1D rt to plot
  plt.figure(figsize=fgs, dpi=dpi)
  plt.grid(False)
  plt.axis('off')
  plt.text(.0,.0,r''+line)
  plt.draw()
  plt.show()

def mquiz(M=10,rquiz=True,frange=(1,2)):
  Q,A=defaultdict(),defaultdict()
  line=r"""$\bullet$ Να απαντήσετε με Σ/Λ στις παρακάτω ερωτήσεις:
  """
  Q2p(line)
  with open("mtDB.txt",'r') as f:
    nline=0
    for line in f:
      line=line.replace('\t',' ')
      if(len(line)<3):    # κενή γραμμή
        continue
      if(line[0] in "0123456789"):  #Question  ##if(nline%2==1):
        nline+=1
        Q[nline]=line[:-3]#.replace('\t',' ')
        res=line[-2]  #Σ/Λ
        A[nline]=[res,r'']
      else:
        A[nline][1]+='\n'+line[:-1]#.replace('\t',' ')
  N=nline#//2
  if(M>N or M<1):
    M=10
  if(frange[0]<1 or frange[0]>=frange[1] or frange[1]>N+1):
    frange=[1,N+1]
  quiz=range(frange[0],frange[1])
  step=100/(frange[1]-frange[0])
  if(rquiz):
    quiz=rn.sample(range(1,N+1),M)
    step=100/M
  vathmos=0
  aa=frange[0]-1
  start=time.time()
  for i in quiz:
    aa+=1
    _Q2p(str(aa)+". "+Q[i][Q[i].find('.')+1:])
    apantisi=input("\n> ")
    if(A[i][0]==apantisi):#if(A[i][0]==input(str(aa)+'.'+Q[i][Q[i].find('.')+1:]+"\n> ")):
      print("Σωστή Απάντηση!\n")
      _Q2p("$\hookrightarrow$ "+A[i][1])
      print("\n")
      vathmos+=step
    elif(apantisi in ['telos','τελος','τελοσ']):
      break
    else:
      print("Λάθος Απάντηση!")
      _Q2p("$\hookrightarrow$ "+A[i][1])
      print("\n")
  print("\n______________________________________\nΗμερομηνία: "+time.strftime("%a, %d %b %Y, %H:%M:%S",time.gmtime(time.time())))
  end=time.time()
  print("\nΤελικός Βαθμός:",int(vathmos*10)/10,"/ 100.0\nΧρόνος:",int(end-start),"seconds")

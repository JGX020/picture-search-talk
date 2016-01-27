import os
import re
import histsimilar
filename='database/test.txt'
filename2='database/test2.txt'
oldlines=histsimilar.data(filename)
def replace(list):
    p=oldlines.index(eval(list[0])[0])
    oldlines[p]=histsimilar.data(filename2)[p]
    b=str(oldlines)	
    fp=open(filename,'w')
  #  for s in oldlines:
    fp.write(b)
    fp.close()
  #  newcase+=1
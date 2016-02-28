#!/usr/bin/python
# Filename: histsimilar.py
# -*- coding: utf-8 -*-

import Image
import os
import time
import datetime
from decimal import * 
fp1=open('database/test3.txt','w')
fp=open('database/test1.txt','w')
up=eval(open('database/test4.txt').read())
down=eval(open('database/test4.txt').read())
fp.truncate()
fp1.truncate()
def make_regalur_image(img, size = (256, 256)):
	return img.resize(size).convert('RGB')

def split_image(img, part_size = (64, 64)):
	w, h = img.size
	pw, ph = part_size
	
	assert w % pw == h % ph == 0
	
	return [img.crop((i, j, i+pw, j+ph)).copy() \
				for i in xrange(0, w, pw) \
				for j in xrange(0, h, ph)]

def hist_similar(lh, rh):
	assert len(lh) == len(rh)
	return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)

def calc_similar(li, ri):
#	return hist_similar(li.histogram(), ri.histogram())
	return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 16.0
			

def calc_similar_by_path(lf, rf):
	li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
	return calc_similar(li, ri)

def make_doc_data(lf, rf):
	li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
	li.save(lf + '_regalur.png')
	ri.save(rf + '_regalur.png')
	fd = open('stat.csv', 'w')
	fd.write('\n'.join(l + ',' + r for l, r in zip(map(str, li.histogram()), map(str, ri.histogram()))))
#	print >>fd, '\n'
#	fd.write(','.join(map(str, ri.histogram())))
	fd.close()
	import ImageDraw
	li = li.convert('RGB')
	draw = ImageDraw.Draw(li)
	for i in xrange(0, 256, 64):
		draw.line((0, i, 256, i), fill = '#ff0000')
		draw.line((i, 0, i, 256), fill = '#ff0000')
	li.save(lf + '_lines.png')
def list(filename):
    for root,dirs,files in os.walk(filename):
        for file in files:
		    print 'test_case_: %.3f%%'%( \
			calc_similar_by_path('uploads/1.jpg', 'uploads'+os.sep + file)*100)
            #print 'uploads'+os.sep + file
def dicts(dicts):
    list="{'imgurl':'"+dicts['imgurl']+"','title':'"+dicts['title']+"','name':'"+dicts['name']+"'}"
    return eval(list)
def clean(file):
    file.truncate()
def list2(file):
    list=[]
    for dicts in data0('database/test.txt'):
	r=calc_similar_by_path('uploads/'+open('database/temp.txt').read(), 'uploads'+os.sep + dicts['name'])*100
	# list="[{'imgurl':'"+dict[1]['imgurl']+"','title':'"+dict[1]['title']+"','name':'"+dict[1]['name']+"'}]"
	# b=20.000
	#print '%.3f%%'(calc_similar_by_path('uploads/1.JPG', 'uploads'+os.sep + dict[0]['name']))
        if  Decimal(r)>=Decimal(50.000):
	         list.append(dicts)
	fp=open('database/test1.txt','w')
	fp1=open('database/test3.txt','w')
	if len(list)>9:
	    fp1.write(str(list))
    if len(list)<=9:
	    fp.write(str(list))
    return list[0:9]
def data0(filename):
	return eval(open(filename).read())
def filesave(filetxt):
	open('database/temp.txt','w').write(filetxt)
	print filetxt
	return filetxt
def data(filename):
    #f = open(filename)
	dict = open(filename).read()
	#f.close()
	lines=eval(dict)
	if len(lines)>=9:
	   return lines[0:9]
	else:
	   return lines[0:len(lines)]
def writecontent(content):
    filesfile=open('database/test5.txt')
    filestr=filesfile.read()
    files=filestr.split(',')
    b    =len(files)
    for file in files:
        b=b-1
        if len(open('database/'+file).read())==0:
			open('database/'+file,'w').write(content)
	                if b>0:
			    break
    open('database/'+str(time.time())+'.txt','w')	#
    open('database/test5.txt','a').write(','+str(time.time())+'.txt')
    filesfile.close()
def writecontent1(content,i):
   open('database/testtopic'+(i*9-7)+'.txt','w').write(content)
def writecontent2(content):
   open('database/testtopic'+(i*9-6)+'.txt','w').write(content)
def writecontent3(content):
   open('database/testtopic'+(i*9-5)+'.txt','w').write(content)
def writecontent4(content):
   open('database/testtopic'+(i*9-4)+'.txt','w').write(content)
def writecontent5(content):
   open('database/testtopic'+(i*9-3)+'.txt','w').write(content)
def writecontent6(content):
   open('database/testtopic'+(i*9-2)+'.txt','w').write(content)
def writecontent7(content):
   open('database/testtopic'+(i*9-1)+'.txt','w').write(content)
def writecontent8(content):
   open('database/testtopic'+(i*9)+'.txt','w').write(content)
def addlistup(i):
	up[i]['up']=int(up[i]['up'])+1
	if up[i]['up']>up[i]['down']:
	   up[i]['value']='1'
	else:
	   up[i]['value']='0'
	write('database/test4.txt',str(up))
	return up[i]['up']
def addlistdown(i):
	down[i]['down']=int(down[i]['down'])+1
	if down[i]['up']>down[i]['down']:
	   down[i]['value']='1'
	else:
	   down[i]['value']='0'
	write('database/test4.txt',str(down))
	return down[i]['down']
def writelist():
        filesfile1=open('database/test5.txt')
        filestr1=filesfile1.read()
	file1=filestr1.split(',')
	filesfile1.close()
	return file1
def writecontentcount(content,i):
    if len(open('database/testtopic'+int(i*9-8)+'.txt').read()) == 0:				# 
	writecontent(content,i)
    else:
        if len(open('database/testtopic'+(int(i)*9-7)+'.txt').read()) == 0:
	       writecontent1(content,i)
        else:
		    if len(open('database/testtopic'+(int(i)*9-6)+'.txt').read()) == 0:
		      writecontent2(content,i)
		    else:
		        if len(open('database/testtopic'+(int(i)*9-5)+'.txt').read()) == 0:
				    writecontent3(content,i)
			else:
				if len(open('database/testtopic'+(int(i)*9-4)+'.txt').read()) == 0:
				    writecontent4(content,i)
				else:
				    if len(open('database/testtopic'+(int(i)*9-3)+'.txt').read()) == 0:
					    writecontent5(content,i)
				    else:
				        if len(open('database/testtopic'+(int(i)*9-2)+'.txt').read()) == 0:writecontent6(content,i)
					else:
					    if len(open('database/testtopic'+(int(i)*9-1)+'.txt').read())==0:writecontent7(content,i)
					    else:
						    if len(open('database/testtopic'+(int(i)*9)+'.txt').read())==0:writecontent8(content,i)
def data2(filename,i):
    #f = open(filename)
	dict = open(filename).read()
	dict1=open("database/test3.txt").read()
	dict3=open("database/test1.txt").read()
	#f.close()
	lines=eval(dict)
	t=9*int(i)
	t2=int(t)-9
	if dict1!="" and len(eval(dict1))>t:
	    return eval(dict1)[t2:t]
	if dict1!="" and len(eval(dict1))<=t:
	    return eval(dict1)[t2:len(eval(dict1))]
	if dict3!="" and len(eval(dict3))>t:
	   return eval(dict3)[t2:t]
	if dict3!="" and len(eval(dict3))<=t:
	   return lines[t2:len(eval(dict3))]
	if len(lines)>t:
	   return lines[t2:t]
	if len(lines)<=t:
	   return lines[t2:len(lines)]
def write(filename,txt):
    file_object = open(filename, 'w')
    file_object.write(txt)
    file_object.close( )
if __name__ == '__main__':
	path = r'testpic/TEST%d/%d.jpg'
	for i in xrange(1, 10):
		print 'test_case_%d: %.3f%%'%(i, \
			calc_similar_by_path('testpic/TEST%d/%d.jpg'%(i, 1), 'testpic/TEST%d/%d.jpg'%(i, 2))*100)
	
#	make_doc_data('test/TEST4/1.JPG', 'test/TEST4/2.JPG')


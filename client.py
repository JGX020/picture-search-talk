#!/usr/bin/python
from socket import *
import os
import sys
import time
ipstr=open('ippool.txt').read()
ips=ipstr.split(',')
def selname(username,password):
        fa=open('5.txt','w')
        fa.write(username+':'+password)
        fa.close()
        for ip in ips:
            send_file ('5.txt',ip)
        time.sleep(2)
        if open('temp/tmp.txt').read()=='true':
           return username
        else:
           return None
def seladdr(username):
         fb=open('6.txt','w')
         fb.write(username)
         fb.close()
         for ip in ips:
                 send_file('6.txt',ip)
         time.sleep(2)
         if open('temp/tmp2.txt').read() is not None:
                 return open('temp/tmp2.txt').read()
         else:
                 return None
def insertmes(values):
        fc=open('7.txt','w')
        fc.write(values)
        fc.close()
        for ip in ips:
                 send_file('7.txt',ip)
        time.sleep(2)
def get_header (name):
        leng = len(name)
        assert leng < 250
        return chr(leng) + name

def send_file (name,ip):
        basename = os.path.basename(name)
        header = get_header(basename)
        cont = open(name).read()
        s = socket (AF_INET, SOCK_STREAM)
        s.connect((ip,1234))
        s.sendall (header)
        s.sendall (cont)
        s.close()
def send_file2 (name,ip):
        basename = os.path.basename(name)
        header = get_header(basename)
        cont = open(name).read()
        s = socket (AF_INET, SOCK_STREAM)
        s.connect((ip,12345))
        s.sendall (header)
        s.sendall (cont)
        s.close()

if __name__=='__main__':
            send_file2 ('validate.txt','101.200.167.44')
            send_file ('5.txt','101.200.167.44')

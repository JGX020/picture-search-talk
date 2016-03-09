#!/usr/bin/python
import SocketServer

# Format: name_len      --- one byte
#         name          --- name_len bytes
#         data          --- variable length
# Save data to name into current directory
addr = ('120.25.244.89', 12345)
class MyTCPHandler (SocketServer.StreamRequestHandler):
        def handle (self):
                name_len = ord(self.rfile.read(1))
                name = self.rfile.read(name_len)
                print "Get request:%s"%name
                fd = open("temp/"+name, 'w')
                cont = self.rfile.read(4096)    
                while cont:
                        fd.write(cont)
                        cont = self.rfile.read(4096)
                fd.close()
                print "Out :%s"%name

server = SocketServer.TCPServer(addr, MyTCPHandler)
server.serve_forever()

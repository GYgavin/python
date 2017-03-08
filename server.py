#!/usr/bin/env python
from socket import *
import time
HOST = '127.0.0.1'
PORT = 9500
BUFSIZ = 1024000
ADDR = (HOST,PORT)

def recv_file(filename):
	print 'Starting receive file...'
	filename = open(filename,'wb')
	tcpCliSock.send('File will be received!')
	while True:
        	data = tcpCliSock.recv(4096000)
        	if data == 'EOF':
     	    		print 'File received successfully!'
            		break
        	filename.write(data)
	filename.close()
def send_file(filename):
	print 'Starting send file...'
	tcpCliSock.send('File will be sent...')
	filename = open(filename,'rb')
	while True:
        	data = filename.read(4096000)
       		if not data:
            		break
        	tcpCliSock.send(data)
	filename.close()
	time.sleep(1)
	tcpCliSock.send('EOF')
	print 'send file success!'

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(1)

while True:
	print('waiting for connection...')
	tcpCliSock,addr = tcpSerSock.accept()
	print('Tcpserver have connected with :',addr)
	while True:
		command = tcpCliSock.recv(4096000)
		act,filename = command.split()
		if act == 'put':
			print 'receiving file from client,please waiting...'
			recv_file(filename)
		elif act == 'get':
			print 'sending file to client,please waiting...'
			send_file(filename)
		else:
			print 'Error:no command,please input put or get + filename'
			continue

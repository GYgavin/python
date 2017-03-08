#!/usr/bin/env python
import socket
import time

HOST = '127.0.0.1'
PORT = 9500
BUFSIZ = 1024000
ADDR = (HOST,PORT)

tcpCliSock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def recv_file(filename):
    print 'transfer from:',ADDR
    filename = open(filename,'wb')
    while True:
        data = tcpCliSock.recv(4096000)
        if data == 'EOF':
            print 'File received successfully!'
            break
        filename.write(data)
    filename.close
def send_file(filename):
    print 'transfer from:',ADDR
    filename = open(filename,'rb')
    while True:
        data = filename.read(4096000)
        if not data:
             break
        tcpCliSock.send(data)
    filename.close()
    time.sleep(1)
    tcpCliSock.send('EOF')
    print 'send file successfully!'


try:
    tcpCliSock.connect(ADDR)
    while True:
        client_command = raw_input('File transfer >>')
        if not client_command:
            continue
	tcpCliSock.send(client_command)
        act,filename = client_command.split()
        if act == 'put':
		print 'File sending...'
		send_file(filename)
        elif act == 'get':
                print 'File receiving...'
		recv_file(filename)
        else:
            print 'command error!'
except socket.error,e:
    print 'ERROR',e
finally:
    tcpCliSock.close()


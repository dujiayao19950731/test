import socket
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #套接字类型AF_INET，  socket.SOCK_STREAM  流式socket  for tcp协议
ip = 'localhost'                 #本机IP
port =  6666                     #设置本机端口号

try:
    server.connect((ip, port))      #建立连接
except Exception as e:
    print('server not find or not open')
    print(e)
    if True:
        server.close()
    else:
        sys.exit()
while True:
    message = input("send:")
    server.sendall(message.encode())        #发送数据到服务端
    data = server.recv(1024)                #接收服务端数据
    data = data.decode()
    print('recieved:', data)
    if message.lower() == '1':              #发送1结束连接
        break
server.close()        
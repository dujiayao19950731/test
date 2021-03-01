import socket

#创建一个TCP套接字server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #套接字类型AF_INET，  socket.SOCK_STREAM  流式socket  for tcp协议

ip = 'localhost'           #本机IP
port =  6666                   #设置本机端口号

#绑定端口号
server.bind((ip,port))           #要以元组形式输入

#开启监听
server.listen(5)

while True:
    conn,addr = server.accept()         #accept表示接受用户端的连接
    print('listen at port:', port)      #输出开启监听的服务端端口
    print('connected by ', addr)        #输出开启监听的服务端地址
    while True:
        data = conn.recv(1024)          #设置接收的数据大小
        data = data.decode()            #解码
        if not data:
            break
        print('recieved message:', data)
        send = input('return:')
        conn.sendall(send.encode())       #再编码发送
    conn.close()
#关闭服务器
server.close()            
    
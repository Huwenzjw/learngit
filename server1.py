import socket
import time
import threading
def sendsock(i,data):
    global user
    for key in user:
        if user.index(key)==i or key==1:
            continue
        key.send(data.encode('utf-8'))
      
def tcplink(i,addr):
    global user
    print('Accept new connection from  %s:%s...\n'% addr)
    user[i].send(b'Welcome')
    while True:
        data = user[i].recv(1024).decode('utf-8')
 
        time.sleep(1)
        s=sock
        if not data or data =='exit' :
            break
        sendsock(i,data)
    user[i].close()
    user[i]=1
    print('Connection from %s:%s closed.'%addr)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
i=-1
user=[]
s.bind(('127.0.0.1',9000))
s.listen(5)
print('listen....')

while True:
    global i
    i=i+1
    sock,addr=s.accept()
    user.append(sock)  
    t=threading.Thread(target=tcplink,args=(i,addr))

    t.start()



import socket,threading
def run_thread1(s,data):
    while True:
        data=input()
        s.send(data.encode('utf-8'))
def run_thread2(s,data):
    while True:
        cdata=s.recv(1024).decode('utf-8')
        print('%s\n'%cdata)


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',9000))
data='Welcome!'
t1=threading.Thread(target=run_thread1,args=(s,data))
t2=threading.Thread(target=run_thread2,args=(s,data))
t1.start()
t2.start()


import socket
import os, sys, stat
import threading

answers = [
    "when the volume of data exceeds the storage capacity of the memory buffer",
    "C/C++",
    "PERL, Java, JavaScript, and C#"
]

class myThread(threading.Thread):
    def __init__(self,s,add):
        threading.Thread.__init__(self)
        self.sock=s
        self.add=add

    def run(self):
        self.chatting()

    def chatting(self):
        while True:
            print("Got a connection from %s" % str(self.add))
            req = self.sock.recv(2024)
            msg = req.decode("utf-8")
            print(msg)

            if (msg == "Admin 1234"):
                data = "Login success"
                self.sock.send(data.encode('utf-8'))

            elif (msg.isnumeric()):
                if (int(msg) < len(answers)):
                    self.sock.send(answers[int(msg)].encode('utf-8'))

                elif (int(msg) == len(answers)):
                    print("client:%s has ended connection" %str(self.add))
                    self.sock.close()
                    break

                else:
                    data = "Wrong index"
                    self.sock.send(data.encode('utf-8'))
            
            else:
                data = "Wrong username or password"
                self.sock.send(data.encode('utf-8'))
            

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 17091
serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    t1=myThread(clientsocket, addr)
    t1.start()
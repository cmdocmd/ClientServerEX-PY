import socket

question = [
    "When does buffer overflow occurs?",
    "In which programming languages mostly buffer overflow occurs?",
    "Which progrmming languages have built-in safety mechanisms that minimize the likelihood of buffer overflow"
]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 17091
#s.connect((host, port))

logged = False

print("Please use this account to login username: Admin and password: 1234\nin this way:\nAdmin 1234\n")

s.connect((host, port))
while True:
    if (logged == False):
        msg = input("login with the given username and password\n")
        s.send(msg.encode('utf-8'))
        

    msg=s.recv(2024)

    data = msg.decode('utf-8')
    print(data)

    print("\n\n")

    if (data == "Login success"):
        logged = True

    if (logged == True):
        msg = ""
        for i in range(len(question)):
            msg += "(" + str(i) + ") " + question[i] + "\n"
        msg += "(" + str(len(question)) + ") Terminate connection\n"
        print(msg)

        msg = input("choose a number: ")
        s.send(msg.encode("utf-8"))

        if (int(msg) == len(question)): #   Terminate connections becouse done packet is sent to server 
            break
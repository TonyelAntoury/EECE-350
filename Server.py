import socket
import datetime

Host = "127.0.0.1"
Port = 2000
EchoMessage = " 127.0.0.1, 2000"
server_address = (Host, Port)
BytesToSend = str.encode(EchoMessage)
Buffer = 2020

S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
S.bind(server_address)

while (True):
    print("Awaiting Request......")
    data = S.recvfrom(Buffer)
    print(datetime.datetime.now()," : arrived")
    if data:
        sent = S.sendto(BytesToSend, data[1])


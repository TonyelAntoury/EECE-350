import socket
import time

Host = "127.0.0.1"
Port = 2000
EchoMessage = " 127.0.0.1, 2000"
server_address = (Host, Port)
BytesToSend = str.encode(EchoMessage) #pythonic.com
Buffer = 2020

S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #DGRAM for UDP
RTT = 0.0

for i in range(0,5):
    x = time.time()
    sent = S.sendto(BytesToSend, server_address)
    data = S.recvfrom(sent)
    RTT+= time.time()-x
    print("answer within ", time.time()-x, "s")
    
print("Avg RTT: " ,RTT/5)
input()
S.close

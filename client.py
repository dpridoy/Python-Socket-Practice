import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))
complete_info = ''
while True:
    msg=s.recv(8)
    if len(msg)<=0:
        break
    complete_info += msg.decode("utf-8")
print(complete_info)
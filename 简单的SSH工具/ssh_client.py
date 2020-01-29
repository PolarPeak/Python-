import socket

cilent = socket.socket() #声明socket类型，同时生成socket对象

cilent.connect(('localhost',6969))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    cilent.send(cmd.encode("utf-8"))
    cmd_res_size = cilent.recv(1024)#接收命令长度
    print("命令结果大小:",cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = cilent.recv(1024)
        received_size += len(data) #每次收到的实际长度
        received_data += data
    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode())
        
cilent.close()


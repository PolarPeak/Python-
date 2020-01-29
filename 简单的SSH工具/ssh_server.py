import socket
import os

server = socket.socket()
server.bind(('localhost',6969))#绑定监听端口
server.listen(5)#监听


while True:
    conn,addr = server.accept()
    print('new conn:',addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        #print('recv',data)
        if not data:
            print("客户端已断开")
            break
        print("执行指令:",data)
        cmd_res = os.popen(data.decode()).read()#接收字符串，执行结果也是字符串
        print("before send",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))#先发送大小给客户端
        conn.send(cmd_res.encode("utf-8"))
        print("send done")

server.close()



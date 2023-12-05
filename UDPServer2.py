#运行在ubuntu上，端口号和IP在代码里面设置好
#https://github.com/nanyanhhh/-
import socket  # 导入 socket 模块

def main():  # 定义主函数
    # 创建 UDP 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 定义服务器的 IP 地址和端口号
    server_addr = ("192.168.136.128", 12000)
    # 将套接字绑定到指定的地址和端口号
    udp_socket.bind(server_addr)
    
    while True:  # 进入循环，等待客户端传输数据
        # 接收文件名和客户端地址
        filename, client_addr = udp_socket.recvfrom(1024)
        # 接收数据和客户端地址
        recv_data, client_addr = udp_socket.recvfrom(1024)
        
        # 输出接收到的数据
        print("%s" % recv_data.decode("gbk"))

        # 将接收到的数据写入文件
        with open(filename.decode('utf-8'), 'w') as file:
            file.write(recv_data.decode('utf-8'))

        # 准备发送数据
        send_data = "%s" % recv_data.decode("utf-8")
        # 发送数据给客户端
        udp_socket.sendto(send_data.encode("utf-8"), client_addr)

    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":  # 判断是否为主程序
    main()  # 调用主函数

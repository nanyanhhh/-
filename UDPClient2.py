#运行在Windows的终端，手动输入服务器IP和端口号，可以发送同一目录下的文件
#https://github.com/nanyanhhh/-
import socket

# 创建套接字，AF_INET表示IPv4，SOCK_DGRAM表示UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务器地址和端口
ipaddr = input("请输入服务器的IP地址：")
port = int(input("请输入端口号："))

# 将套接字绑定到地址，在AF_INET中，以元组(host, port)的形式表示地址
server_addr = (ipaddr, port)

while True:
    # 输入要发送的文件名
    file_name = input("请输入要发送的文件名：")

    # 发送UDP数据，将数据发送到连接的套接字，返回值为发送的字节数
    udp_socket.sendto(file_name.encode('utf-8'), server_addr)

    try:
        # 打开文件并读取内容
        with open(file_name, 'r', encoding='utf-8') as file:
            # 读取文件内容并保存在file_content中并准备发送
            file_content = file.read()

            # 发送文件内容
            udp_socket.sendto(file_content.encode('utf-8'), server_addr)
            print("文件内容已发送")
    except FileNotFoundError:
        print("文件不存在，请重新输入")

    # 接收服务器响应，数据以字符串形式返回，1024表示最大数据量
    # recvfrom函数返回(data, address)，address为发送数据的套接字地址
    recv_data, _ = udp_socket.recvfrom(1024)
    print("从服务器收到的响应：%s" % recv_data.decode("utf-8"))

# 关闭套接字
udp_socket.close()

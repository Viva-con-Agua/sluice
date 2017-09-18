from ssh_server.ssh_server import ssh_server

if __name__ == "__main__":
    socket = ssh_server()
    while(True):
        socket.start_socket()


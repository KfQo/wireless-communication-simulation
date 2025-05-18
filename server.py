import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("Server is running...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received data: {data.decode()} from {addr}")

if __name__ == "__main__":
    start_server()

import socket

def send_data(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(message.encode(), ('localhost', 12345))
    print("Data sent.")

if __name__ == "__main__":
    message = input("Enter the message to send: ")
    send_data(message)

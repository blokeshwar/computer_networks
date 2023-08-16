import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Error receiving message.")
            break

def send_messages():
    while True:
        recipient_id = input("Enter recipient's unique ID (or 'list' to see online clients): ")
        if recipient_id.lower() == "list":
            client_socket.send(recipient_id.encode('utf-8'))
        else:
            message = input("Enter your message: ")
            full_message = f"{recipient_id}:{message}"
            client_socket.send(full_message.encode('utf-8'))

HOST = 'localhost'
PORT = 12345

client_id = input("Enter your unique ID: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(client_id.encode('utf-8'))

recv_thread = threading.Thread(target=receive_messages)
recv_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print("\n", " -> ", message)
        except:
            print("Connection closed")
            break

def client_program():
    host = input("Enter server IP: ")
    port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to server. You can create or join rooms.")
    print("Commands: CREATE room_name password | JOIN room_name password")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input(" <- ")

        if message.strip().upper() == 'EXIT':
            client_socket.close()
            break

        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    client_program()


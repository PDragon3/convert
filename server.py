import socket
import threading

rooms = {}

def broadcast_message(room_name, message, sender_socket):
    for client in rooms[room_name]['clients']:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                rooms[room_name]['clients'].remove(client)

def handle_client(client_socket, addr):
    current_room = None
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            command, *args = message.split(' ', 1)
            if command == 'CREATE':
                room_name, password = args[0].split()
                if room_name in rooms:
                    client_socket.send("Room already exists\n".encode('utf-8'))
                else:
                    rooms[room_name] = {'password': password, 'clients': [client_socket]}
                    current_room = room_name
                    client_socket.send(f"Room {room_name} created\n".encode('utf-8'))
            elif command == 'JOIN':
                room_name, password = args[0].split()
                if room_name in rooms:
                    if rooms[room_name]['password'] == password:
                        rooms[room_name]['clients'].append(client_socket)
                        current_room = room_name
                        client_socket.send(f"Joined room {room_name}\n".encode('utf-8'))
                    else:
                        client_socket.send("Incorrect password\n".encode('utf-8'))
                else:
                    client_socket.send("Room does not exist\n".encode('utf-8'))
            else:
                if current_room:
                    broadcast_message(current_room, message, client_socket)
                else:
                    client_socket.send("Invalid command or not in a room\n".encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break

    if current_room:
        rooms[current_room]['clients'].remove(client_socket)
    client_socket.close()

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Server started on port {port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server(9999)


import socket
import command_class

class Server(socket.socket):
    def __init__(self) -> None:
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self, ip, port, listen) -> None:
        self.bind((ip, port))
        self.listen(listen)

    def stop(self) -> None:
        self.shutdown()
        self.close()

    def thread(self, client):
        while True:
            data = client.recv(1024)
            command_response = command_class.Command(data)
            response = f'HTTP/1.1 200 OK\r\n\r\n{command_response.execute()}'.encode()
            print(response)
            client.send(response)
            client.close()
import socket
import request_class
import http_functions

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

    def execute_http_request(self, request: dict) -> None:
        assert isinstance(request, dict)

        method = http_functions.methods[request['header']['line'][0]]
        target = request['header']['line'][1]

        response = method(target, request['header']['headers'])

        return response

    def thread(self, client) -> None:
        brute_request = client.recv(1024)
        request = request_class.Request(brute_request)

        response = self.execute_http_request(request.request).get()
        client.send(response.encode())

        client.close()
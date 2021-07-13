import threading
import server_class

server = server_class.Server()
server.start(
    'localhost',
    8080,
    5,
)

while True:
    client, address = server.accept()
    threading.Thread(target=server.thread, args=(client,)).start()
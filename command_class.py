class Command:
    def __init__(self, data) -> None:
        self.command = [line.split(' ') for line in data.decode().split('\r\n')]

        print(self.command)

        self.commands = {
            'GET': self.get,
        }

        self.documents = {
            '/': 'index.html',
            '/sobre': 'sobre.html',
            '/404': '404.html',
        }

    def execute(self):
        return self.commands[self.command[0][0]](self.command[0][1])

    def get(self, target):
        document = self.documents.get(target) or self.documents['/404']

        with open(document, 'r') as required_file:
            return ''.join(required_file.readlines())
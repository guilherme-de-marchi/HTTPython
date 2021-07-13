class Request:
    def __init__(self, brute_request: bytes) -> None:
        assert isinstance(brute_request, bytes)
        self.brute_request = brute_request
        
        readable_request = str(self)
        splitted_request = readable_request.split('\r\n\r\n', 1)
        header = splitted_request[0].split('\r\n')
        body = splitted_request[1].split('\r\n') if len(splitted_request) >= 2 else '#'
        
        self.request = {
            'header': {
                'line': header[0].split(' '),
                'headers': dict([header_line.split(': ') for header_line in header[1:]]),
            },
            'body': body,
        }
        

    def __str__(self) -> str:
        return self.brute_request.decode()
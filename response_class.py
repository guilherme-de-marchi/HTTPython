class Response:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs

    def get(self) -> str:
        return f"{self.kwargs.get('http_version')} {self.kwargs.get('status_code')} {self.kwargs.get('status_text')}\r\n\r\n{self.kwargs.get('content')}"

class OK(Response):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.kwargs['Status-Code'] = 200
        self.kwargs['Status-Text'] = 'OK'

class NotFound(Response):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.kwargs['Status-Code'] = 404
        self.kwargs['Status-Text'] = 'Oh shit!'
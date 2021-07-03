import response_class

def get(target: str, headers: dict = {}):
    assert isinstance(target, str)
    assert isinstance(headers, dict)

    accepted_types = headers['Accept'].split(',')

    try:
        with open(f'{target[1:]}.{archive_types[accepted_types[0]]}') as archive:
            content = archive.read()
            return response_class.Successful(
                http_version='HTTP/1.1',
                status_code=200,
                status_text='OK',
                content=content,
            )
        
    except Exception:
        return response_class.Successful(
                http_version='HTTP/1.1',
                status_code=404,
                status_text='Oh shit!',
            )

archive_types = {
    'text/html': 'html',
}

methods = {
    'GET': get,
}
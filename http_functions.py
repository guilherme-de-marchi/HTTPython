import os
import response_class

def get(target: str, headers: dict = {}):
    assert isinstance(target, str)
    assert isinstance(headers, dict)

    accepted_types = headers['Accept'].split(',')

    try:
        available_types = []
        for archive in os.listdir(os.getcwd() + '/' + '/'.join(target.split('/')[:-1])):
            if archive.split('.')[-1] in [archive_types.get(x) for x in accepted_types]:
                available_types.append(archive.split('.')[-1])
            

        with open(f'{target[1:]}.{available_types[0]}', 'r') as archive:
            content = archive.read()
            return response_class.OK(
                http_version='HTTP/1.1',
                status_code=200,
                status_text='OK',
                content=content,
            )
        
    except Exception as error:
        with open('404.html', 'r') as archive:
            content = archive.read()

        return response_class.NotFound(
            http_version='HTTP/1.1',
            status_code=404,
            status_text='Not Found',
            content=content,
        )

archive_types = {
    'text/html': 'html',
    'image/webp': 'jpeg',
    '*/*': '*',
}

methods = {
    'GET': get,
}
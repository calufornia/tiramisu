import requests

apikey="NEeYQKLjtZyWXlcUBor348kuPY5C3N8K"

def get_json(basename, **kwargs):
    request_string = basename
    for key in kwargs:
        request_string += key + "=" + kwargs[key] + "&"
    request_string += "apikey=" + apikey
    r = requests.get(request_string)
    data = r.json()['results']
    return data

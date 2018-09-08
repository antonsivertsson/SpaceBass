import requests
from PIL import Image
from io import BytesIO

_base_url = "https://mtf-sat.synvinkel.org"


class _Frame:

    def __init__(self, client, data):
        self._client = client
        self._data = data

    def __getitem__(self, k):
        return self._data[k]

    def __getattr__(self, k):
        return self._data[k]

    def fetch_rgba(self):
        url = self._data["url"]
        r = self._client.get(url)
        return Image.open(BytesIO(r.content))


class _Series:

    def __init__(self, client, data):
        self._client = client
        self._data = data

    def data(self):
        return self._data

    def frames(self):
        for d in self._data["images"]:
            yield _Frame(self._client, d)

    def __len__(self):
        return len(self._data)

    def fetch_data(self, i):
        url = self._data["images"][i]["rawUrl"]
        #url = url.replace(".png", ".zip")
        r = self._client.get(url)
        raise Exception("not implemented")
        # TODO: unzip and combine tiff files.

    def fetch_rgba(self, i):
        url = self._data["images"][i]["url"]
        r = self._client.get(url)
        return Image.open(BytesIO(r.content))


class Client:

    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, url, **kwargs):
        p = { "apikey": self.api_key }
        for k in kwargs:
            p[k] = kwargs[k]
        res = requests.get(url, params=p)
        res.raise_for_status()
        return res

    def get_image(self, url):
        r = self.get(url)
        return Image.open(BytesIO(r.content))

    def get_route(self, path, **kwargs):
        return self.get(_base_url + '/' + path, **kwargs)

    def fetch_series(self, lng, lat):
        return _Series(self, self.get_route("timeseries", lng=lng, lat=lat).json())

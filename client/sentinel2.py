import requests
from PIL import Image
from io import BytesIO

_base_url = "https://mtf-sat.synvinkel.org"


class _Series:

    def __init__(self, client, data):
        self.client = client
        self.data = data

    def frames(self):
        return self.data

    def __len__(self):
        return len(self.data)

    def fetch_data(self, i):
        url = self.data["images"][i]["url"]
        url = url.replace(".png", ".zip")
        r = self.client._get_url(url)
        raise Exception("not implemented")
        # TODO: unzip and combine tiff files.

    def fetch_rgba(self, i):
        url = self.data["images"][i]["url"]
        r = self.client._get_url(url)
        return Image.open(BytesIO(r.content))


class Client:

    def __init__(self, api_key):
        self.api_key = api_key

    def _get_url(self, url, **kwargs):
        p = { "apikey": self.api_key }
        for k in kwargs:
            p[k] = kwargs[k]
        res = requests.get(url, params=p)
        res.raise_for_status()
        return res

    def get(self, path, **kwargs):
        return self._get_url(_base_url + '/' + path, **kwargs)

    def fetch_series(self, lng, lat):
        return _Series(self, self.get("timeseries", lng=lng, lat=lat).json())

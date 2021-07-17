import requests
import json
from random import choice


class GimmeSomeJazzGifs:
    def __init__(self, apikey):
        self.apikey = apikey
        self.search_terms = [
            "jazz",
            "birthday",
            "36",
            "piano",
            "love",
            "kiss",
            "kisses"
        ]
        self.lmt = 512
        self.buffer = []
        self.buffer_size = 128

    def draw(self):
        r = requests.get(
            "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (choice(self.search_terms),
                                                                    self.apikey,
                                                                    self.lmt)
        )
        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            top_gifs = json.loads(r.content)
            url = [m for m in choice(top_gifs['results'])['media'] if 'mediumgif' in m][0]['mediumgif']['url']
            if url not in self.buffer:
                self.buffer.append(url)
                if len(self.buffer) > self.buffer_size:
                    self.buffer.pop(0)
                return url
            else:
                return self.draw()
        else:
            return None


def main():
    g = GimmeSomeJazzGifs()
    print(g.draw())


if __name__ == '__main__':
    main()

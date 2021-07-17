import json
from random import choice
import re
import numpy as np


class GimmeSomeJazz:
    def __init__(self, json_file=None):
        with open(json_file) as f:
            self.library = json.load(f)

    @staticmethod
    def _draw(v):
        if isinstance(v, list) and np.all([isinstance(vi, dict) for vi in v]):
            weights = [d['weight'] for d in v]
            data = [d['library'] for d in v]
            return GimmeSomeJazz._draw(np.random.choice(data, p=weights / np.sum(weights)))
        elif isinstance(v, list):
            return GimmeSomeJazz._draw(choice(v))
        else:
            return v

    def draw(self):
        book = self._draw(self.library)
        with open(book) as f:
            data = json.load(f)
        e = self._draw(data)
        if 'desc' in e:
            desc = e['desc']
            keys = [('@' + re.sub(r'[^\w]', '', w))
                    for w in desc.split() if w.startswith('@')]
        if 'randomizers' in e:
            v = [np.prod([len(r[k]) for k in r]) for r in e['randomizers']]
            r = np.random.choice(e['randomizers'], p=v / np.sum(v))
            if 'desc' in r:
                desc = r['desc']
                keys = [('@' + re.sub(r'[^\w]', '', w))
                        for w in desc.split() if w.startswith('@')]
            for key in r:
                desc = desc.replace(key, self._draw(r[key]))
        for key in keys:
            if key in e:
                desc = desc.replace(key, self._draw(e[key]))
        return desc
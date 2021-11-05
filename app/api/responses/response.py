from typing import Any


class Response(object):
    def __init__(self, data: Any):
        self._data = data

    def to_dict(self):
        return {}

from ..response import Response


class Creature(Response):
    def to_dict(self):
        return {
            "id": self._data.id,
            "ip_address": self._data.ip_address,
        }

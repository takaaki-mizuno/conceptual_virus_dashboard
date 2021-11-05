from ..response import Response


class CreatureSummary(Response):
    def to_dict(self):
        return {
            "id": self._data.id,
            "ip_address": self._data.ip_address,
        }

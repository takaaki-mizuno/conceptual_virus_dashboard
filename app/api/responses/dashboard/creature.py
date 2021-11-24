from typing import Any

from ..response import Response


class Creature(Response):
    def __init__(self, data: Any, status: Any):
        super().__init__(data)
        self._status = status

    def to_dict(self):
        if self._status:
            status = self._status.status
        else:
            status = []
        return {
            "id": self._data.id,
            "ip_address": self._data.ip_address,
            "status": status
        }

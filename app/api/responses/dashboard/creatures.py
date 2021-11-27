from ..response import Response
from .creature_summary import CreatureSummary
from typing import Any


class Creatures(Response):
    def to_dict(self):
        result = []
        for creature, status in self._data:
            result.append(CreatureSummary(creature, status).to_dict())

        return {"creatures": result}

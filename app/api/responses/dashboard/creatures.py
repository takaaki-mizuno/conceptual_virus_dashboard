from ..response import Response
from .creature_summary import CreatureSummary


class Creatures(Response):
    def to_dict(self):
        result = []
        for creature in self._data:
            result.append(CreatureSummary(creature).to_dict())

        return {
            "creatures": result
        }

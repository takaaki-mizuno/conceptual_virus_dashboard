from .creature import Creature


class CreatureSummary(Creature):
    def to_dict(self):
        return {
            "id": self._data.id,
            "ip_address": self._data.ip_address,
            "viruses": self.get_summary()
        }

    def get_summary(self) -> dict:
        result = {
            "total_count": len(self._status.status)
        }
        virus_hash = {}
        for status in self._status.status:
            if "h" not in status:
                continue
            if status["h"] in virus_hash:
                virus_hash[status["h"]] = virus_hash[status["h"]] + 1
            else:
                virus_hash[status["h"]] = 1

        result["trends"] = dict(sorted(virus_hash.items(), key=lambda item: item[1]))

        return result


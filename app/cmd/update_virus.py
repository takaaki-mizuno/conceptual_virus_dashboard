from ..database import SessionLocal
from ..services import CreatureService
import requests
from typing import Optional, Tuple


class UpdateVirus(object):
    def __init__(self):
        self._service = CreatureService()

    def execute(self):
        db = SessionLocal()
        creatures = self._service.get_active_creatures(db)
        for creature, snapshot in creatures:
            memo = {}
            for virus in snapshot.status:
                if "h" in virus and virus["h"] not in memo:
                    memo[virus["h"]] = 1
                    virus_model = self._service.get_virus(db, virus["h"])
                    if virus_model is None and "i" in virus:
                        _hash, sequence = self._get_virus_sequence(
                            creature.ip_address, virus["i"])
                        if sequence is not None and _hash == virus["h"]:
                            self._service.set_virus(db, virus["h"], sequence)

    def _get_virus_sequence(self, ip_address: str,
                            index: str) -> Tuple[Optional[str], Optional[str]]:
        url = "http://{}/dump".format(ip_address)
        r = requests.get(url=url, params={"index": index})
        data = r.json()
        if isinstance(data, str):
            elements = data.split(":")
            if len(elements) != 2:
                return None, None
            return elements[0], elements[1]

        return None, None

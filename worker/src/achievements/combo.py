from typing import List

from src.core import AchievementBase
from src.core.models import Score


class Combo(AchievementBase):
    base = {
        "id": "osu-combo-{mode}-{index}",
        "name": "{index} Combo (osu!{mode})",
        "description": "{index} big ones! You're moving up in the world!",
        "icon": "osu-combo-{index}"
    }

    keys = {
        "index": [500, 750, 1000, 2000],
        "mode": ["std", "taiko", "ctb", "mania"]
    }

    struct = {
        "index": 1,
        "mode": 4
    }

    def __init__(self):
        super().__init__()

    def handle(self, score: Score) -> List[str]:
        achievement_ids = []

        for ach in self.achievements:
            if ach.index > score.maxcombo:
                continue

            achievement_ids.append(ach.id)

        return achievement_ids
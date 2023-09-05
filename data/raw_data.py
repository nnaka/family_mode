from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Any, Union, Optional

data: List[Dict[str, Any]] = [
    {
        "id": "1488258600",
        "ts": "2017-02-28T05:10:00.000Z",
        "stages": [
            {"stage": "awake", "duration": 1024},
            {"stage": "light", "duration": 1020},
        ],
        "score": 93,
        "timeseries": {
            "tnt": [
                ["2017-02-28T06:20:00.000Z", 1],
                ["2017-02-28T06:21:00.000Z", 2],
                ["2017-02-28T06:30:00.000Z", 1],
            ],
            "tempRoomC": [["2017-02-28T05:00:00.000Z", 19.7874]],
            "tempBedC": [["2017-02-28T05:00:00.000Z", 34.1514]],
            "respiratoryRate": [["2017-02-28T05:00:00.000Z", 16.6667]],
            "heartRate": [["2017-02-28T05:00:00.000Z", 48]],
        },
    },
    {
        "id": "1488258600",
        "ts": datetime.now().isoformat(),
        "stages": [
            {"stage": "awake", "duration": 1024},
            {"stage": "light", "duration": 1020},
        ],
        "score": 93,
        "timeseries": {
            "tnt": [
                ["2017-02-28T06:20:00.000Z", 1],
                ["2017-02-28T06:21:00.000Z", 2],
                ["2017-02-28T06:30:00.000Z", 1],
            ],
            "tempRoomC": [
                [(datetime.now() - timedelta(hours=12)).isoformat(), 19.7874]
            ],
            "tempBedC": [[(datetime.now() - timedelta(hours=12)).isoformat(), 34.1514]],
            "respiratoryRate": [
                [(datetime.now() - timedelta(hours=12)).isoformat(), 16.6667]
            ],
            "heartRate": [[(datetime.now() - timedelta(hours=12)).isoformat(), 48]],
        },
    },
    {
        "id": "1488258600",
        "ts": datetime.now().isoformat(),
        "stages": [
            {"stage": "awake", "duration": 1024},
            {"stage": "light", "duration": 1020},
        ],
        "score": 93,
        "timeseries": {
            "tnt": [
                ["2017-02-28T06:20:00.000Z", 1],
                ["2017-02-28T06:21:00.000Z", 2],
                ["2017-02-28T06:30:00.000Z", 1],
            ],
            "tempRoomC": [
                [(datetime.now() - timedelta(hours=12)).isoformat(), 19.7874]
            ],
            "tempBedC": [[(datetime.now() - timedelta(hours=12)).isoformat(), 34.1514]],
            "respiratoryRate": [
                [(datetime.now() - timedelta(hours=12)).isoformat(), 16.6667]
            ],
            "heartRate": [[(datetime.now() - timedelta(hours=12)).isoformat(), 48]],
        },
    },
]


class Relationship(Enum):
    FAMILY = 0


# ID to set of IDs for which the user has view permissions
family_data: Dict[str, Dict[str, Relationship]] = {
    "1488258600": {
        "1": Relationship.FAMILY,
    },
    "1": {
        "1488258600": Relationship.FAMILY,
        "2": Relationship.FAMILY,
    },
}

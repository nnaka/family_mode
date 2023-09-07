from datetime import datetime, timedelta
from flask import Flask, jsonify, request, Request, Response
import json
from typing import List, Dict, Any, Union, Optional, Tuple

from data.raw_data import data, family_data
from models.user_models import Relationship

app = Flask(__name__)

data: List[Dict[str, Any]] = data


def _get_start_end_times(request: Request) -> Tuple[str, str]:
    now: datetime = datetime.now()
    # TODO: change based on user preferences
    # Default to show a week's worth of data
    start_time: str = request.args.get(
        "start_time", (now - timedelta(days=7)).isoformat()
    )
    end_time: str = request.args.get("end_time", now.isoformat())
    return start_time, end_time


@app.route("/temperature", methods=["GET"])
# def get_temperature() -> Union[List[Dict[str, Dict[str, Union[str, float]]]], str]:
def get_temperature() -> Response:
    """
    Endpoint to return room and bed temperature over time

    Args:
        start_time: Start time.
        end_time: End time.

    Returns:
        List of data points which contain room and bed temperatures along with
        the timestamp

    Raises:
        KeyError: Raises an exception.
    """
    start_time: str
    end_time: str
    start_time, end_time = _get_start_end_times(request)

    temperature_data: List[Dict[str, Dict[str, Union[str, float]]]] = []
    # TODO: filter based on request.args.get("id", None)
    for interval in data:
        if "timeseries" in interval:
            datapoint: Dict[str, Dict[str, Union[str, float]]] = {}
            if "tempRoomC" in interval["timeseries"]:
                for timestamp, temp in interval["timeseries"]["tempRoomC"]:
                    if start_time <= timestamp <= end_time:
                        datapoint["room"] = {
                            "timestamp": timestamp,
                            "temperature": temp,
                        }
            if "tempBedC" in interval["timeseries"]:
                for timestamp, temp in interval["timeseries"]["tempBedC"]:
                    if start_time <= timestamp <= end_time:
                        datapoint["bed"] = {"timestamp": timestamp, "temperature": temp}
            if "room" in datapoint or "bed" in datapoint:
                temperature_data.append(datapoint)

    return jsonify(temperature_data)


@app.route("/sleep_stages", methods=["GET"])
# def get_sleep_stages() -> Union[List[Dict[str, Union[str, str]]], str]:
def get_sleep_stages() -> Response:
    """
    Endpoint to return sleep stages over time

    Args:
        start_time: Start time.
        end_time: End time.

    Returns:
        This is a description of what is returned.
    """
    start_time: str
    end_time: str
    start_time, end_time = _get_start_end_times(request)

    sleep_stages_data: List[Dict[str, Union[str, str]]] = []
    # TODO: filter based on request.args.get("id", None)
    for interval in data:
        for stage in interval["stages"]:
            if start_time <= interval["ts"] <= end_time:
                sleep_stages_data.append(
                    {"timestamp": interval["ts"], "stage": stage["stage"]}
                )

    return jsonify(sleep_stages_data)


@app.route("/sleep_score", methods=["GET"])
# def get_sleep_score() -> Union[Dict[str, Optional[int]], str]:
def get_sleep_score() -> Response:
    """
    Endpoint to return overall sleep score for a given time period

    Args:
        start_time: Start time.
        end_time: End time.

    Returns:
        Average sleep score within the time range
    """
    start_time: str
    end_time: str
    start_time, end_time = _get_start_end_times(request)

    sleep_score: float = 0.0
    count: int = 0
    # TODO: filter based on request.args.get("id", None)
    id: Optional[str] = request.args.get("id", None)
    if id is None:
        return jsonify({})

    for interval in data:
        if start_time <= interval["ts"] <= end_time:
            sleep_score += interval["score"]
            count += 1
    sleep_score = sleep_score / max(count, 1)

    return jsonify({"sleep_score": sleep_score})


@app.route("/family_members", methods=["GET"])
def get_family_members() -> Response:
    """
    Endpoint to return family members of the given ID

    Args:
        id: User ID

    Returns:
        Response with list of IDs of family members
    """
    # for interval in data.filter(x => family_data):
    id: Optional[str] = request.args.get("id", None)
    if id is None or id not in family_data:
        return jsonify([])
    family_members: List[str] = [
        id
        for id, relationship in family_data[id].items()
        if relationship == Relationship.FAMILY
    ]
    return jsonify(family_members)


if __name__ == "__main__":
    app.run(debug=True)

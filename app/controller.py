import json

from .utils.storage import Storage
from .utils.socket_client import socket_client


def post_event(events_list):
    for event in events_list:
        event_type = event.get("event")
        event_time = event.get("ts")
        event_id = event.get("_id")
        single_event_object = {"event": event_type,
                               "time": event_time,
                               "id": event_id}
        Storage().set_key(event_id, json.dumps(single_event_object))
        socket_client(event_type)
    return True


def get_event(event_id):
    stored_objects = Storage().get_key(event_id)
    if stored_objects:
        response = {'data': json.loads(stored_objects)}
    else:
        response = {'data': {}}
    return response

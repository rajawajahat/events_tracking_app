from fastapi import Request, Body
from fastapi import FastAPI

from .controller import post_event

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": True}


@app.post("/events_webhook")
def events_webhook(request: Request, payload=Body(...)):
    events_list = payload.get("mandrill_events")
    response = post_event(events_list)
    return response


@app.get("/events/{event_id}")
def events(request: Request, event_id: str):
    response = get_event(event_id)
    return response


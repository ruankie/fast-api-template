from fastapi import FastAPI
from src.utils import Greetings

app = FastAPI()
my_greeting = Greetings()


@app.get("/")
async def get_greeting():
    """
    Return greeting message in the following format:
    {"greeting": "<greeting>"}
    """
    return {"message": my_greeting.get_greeting()}

@app.post("/set-greeting")
def set_greeting(payload:dict):
    """
    Set new greeting message.
    Payload must be in the following format:
    {"greeting": "<new-greeting>"}
    """
    my_greeting.set_greeting(payload["greeting"])
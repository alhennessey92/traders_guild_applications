from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageRequest(BaseModel):
    message: str

@app.post("/message")
async def message_reply(req: MessageRequest):
    return {"reply": f"FastAPI received: {req.message}"}
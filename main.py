from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()
router = APIRouter()


class Command(BaseModel):
    command: str
    metadata: str | None = None


@router.post(path="/on_flashlight", response_model=str | None, status_code=200)
async def on_flashlight(command: Command):
    if command.command == "ON":
        return "Flashlight was on"


@router.post(path="/off_flashlight", response_model=str | None, status_code=200)
async def off_flashlight(command: Command):
    if command.command == "OFF":
        return "Flashlight was off"


@router.post(path="/flashlight_color", response_model=str | None, status_code=200)
async def flashlight_color(command: Command):
    if command.command == "COLOR" and command.metadata:
        return f"Flashlight color changed to {command.metadata}"


app.include_router(router=router, prefix="/flashlight", tags=["FLASHLIGHT"])


def connect(app: FastAPI, host: str, port: int):
    uvicorn.run(app=app, host=host, port=port)


if __name__ == "__main__":
    host = input("Enter host: ")
    port = input("Enter port: ")
    if host and port:
        try:
            connect(app=app, host=host, port=int(port))
        except:
            print("Incorrect host or port.")
    else:
        connect(app=app, host="127.0.0.1", port=9999)

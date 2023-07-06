from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Command(BaseModel):
    command: str
    metadata: float = None


async def process_command(command, metadata):
    if command == "ON":
        return await turn_on()
    elif command == "OFF":
        return await turn_off()
    elif command == "COLOR":
        return await change_color(metadata)
    else:
        pass


async def turn_on():
    message = "Lamp turned on"
    print(message)
    return message


async def turn_off():
    message = "Lamp turned off"
    print(message)
    return message


async def change_color(color):
    message = f"Lamp color changed to {color}"
    print(message)
    return message


@app.post("/")
async def handle_command(command: Command):
    return await process_command(command.command, command.metadata)


if __name__ == "__main__":
    host = input("Введите хост (по умолчанию 127.0.0.1): ") or '127.0.0.1'
    port = input("Введите порт (по умолчанию 9999): ") or '9999'
    try:
        uvicorn.run(app, host=host, port=int(port))
    except:
        print(f"Wrong host or port.")


import websockets
import asyncio

async def listen():
    url = "ws://localhost:7890"
    # Connect to the server
    async with websockets.connect(url) as websocket:
        # Send a greeting message
        await websocket.send("Hello Server!")
        # Stay alive forever, listening to incoming msgs
        while True:
            msg = await websocket.recv()
            print(msg)

# Start the connection
asyncio.get_event_loop().run_until_complete(listen())
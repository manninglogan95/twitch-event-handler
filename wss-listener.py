#!/usr/bin/env python

import asyncio
import websockets

async def test():
    async with websockets.connect('wss://pubsub-edge.twitch.tv') as websocket:

        msg = { "type": "PING"}
        await websocket.send(msg.__str__())
        print("> {}".format(msg))

        res = await websocket.recv()
        print("< {}".format(res))

asyncio.get_event_loop().run_until_complete(test())
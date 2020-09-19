#!/usr/bin/env python3
"""
Check websocket connection can be built
prerequisite: pip3 install websocket_client
"""
import sys
import websocket
from websocket import WebSocketBadStatusException


def main(argv):
    length = len(argv)
    if length < 1:
        print("usage: cws [url]")
        sys.exit()

    ws = websocket.WebSocket()
    url = argv[0]
    try:
        ws.connect(url)
    except ValueError as e:
        print(str(e))
    except WebSocketBadStatusException:
        print("Connection is broken!")
    else:
        if ws.connected:
            print("Connection is OK!")


if __name__ == "__main__":
    main(sys.argv[1:])

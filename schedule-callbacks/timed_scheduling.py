__author__ = 'psuresh'

import asyncio
import time


def callback(n, loop):
    print('callback {} invoked at {}'.format(n, loop.time()))


@asyncio.coroutine
def main(loop):
    now = loop.time()
    print('clock time: {}'.format(time.time()))
    print('loop  time: {}'.format(now))

    print('registering callbacks')
    loop.call_at(now + 0.2, callback, 1, loop)
    loop.call_at(now + 0.1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)

    yield from asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()


# Output
# ------------------------------------------
# python timed_scheduling.py
# entering event loop
# clock time: 1486548417.856184
# loop  time: 116201.834386072
# registering callbacks
# callback 3 invoked at 116201.834468813
# callback 2 invoked at 116201.93956538601
# callback 1 invoked at 116202.038945256
# closing event loop
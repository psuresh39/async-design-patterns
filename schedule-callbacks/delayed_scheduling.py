__author__ = 'psuresh'

import asyncio


def callback(n):
    print('callback {} invoked'.format(n))


@asyncio.coroutine
def main(loop):
    print('registering callbacks')
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)

    yield from asyncio.sleep(0.4)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()


# Output
# --------------------------------
# python delayed_scheduling.py
# entering event loop
# registering callbacks
# callback 3 invoked
# callback 2 invoked
# callback 1 invoked
# closing event loop

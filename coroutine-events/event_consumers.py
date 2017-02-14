__author__ = 'psuresh'

import asyncio
import functools


def set_event(event):
    print('setting event in callback')
    event.set()

@asyncio.coroutine
def coro1(event):
    print('coro1 waiting for event')
    yield from event.wait()
    print('coro1 triggered')


@asyncio.coroutine
def coro2(event):
    print('coro2 waiting for event')
    yield from event.wait()
    print('coro2 triggered')


@asyncio.coroutine
def main(loop):
    # Create a shared event
    event = asyncio.Event()
    print('event start state: {}'.format(event.is_set()))

    loop.call_later(
        0.2, functools.partial(set_event, event)
    )

    yield from asyncio.wait([coro1(event), coro2(event)])
    print('event end state: {}'.format(event.is_set()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()


# Output
# ----------------------------------------------------------------
# python event_consumers.py
# event start state: False
# coro1 waiting for event
# coro2 waiting for event
# setting event in callback
# coro1 triggered
# coro2 triggered
# event end state: True

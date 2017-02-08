__author__ = 'psuresh'

import asyncio


lock = asyncio.Lock()

@asyncio.coroutine
def coro1():
    print('coro1 waiting for the lock')
    with (yield from lock):
        print('coro1 acquired lock')
        yield from asyncio.sleep(3)
        print('coro1 released lock')


@asyncio.coroutine
def coro2():
    print('coro2 waiting for the lock')
    yield from lock
    try:
        print('coro2 acquired lock')
    finally:
        print('coro2 released lock')
        lock.release()

@asyncio.coroutine
def main():
    # Run the coroutines that want to use the lock.
    yield from asyncio.wait([coro1(), coro2()])


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())
finally:
    event_loop.close()

# Output:
# ----------------------------
# python locking.py
# coro1 waiting for the lock
# coro1 acquired lock
# coro2 waiting for the lock
# coro1 released lock
# coro2 acquired lock
# coro2 released lock
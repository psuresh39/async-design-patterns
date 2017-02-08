__author__ = 'psuresh'

import asyncio

@asyncio.coroutine
def coro1(number):
    print("Task #{0} started".format(number))
    yield from asyncio.sleep(2)
    print("Task #{0} ended".format(number))

loop = asyncio.get_event_loop()
asyncio.ensure_future(coro1(1))
asyncio.ensure_future(coro1(2))
try:
    loop.run_forever()
except KeyboardInterrupt:
    print("program closed")

# Output
# -----------------------------
# python background_task_infinite_loop.py
# Task #1 started
# Task #2 started
# Task #1 ended
# Task #2 ended
# ^Cprogram closed
__author__ = 'psuresh'

import asyncio

@asyncio.coroutine
def coro1(number):
    print("Task #{0} started".format(number))
    yield from asyncio.sleep(2)
    print("Task #{0} ended".format(number))
    future = asyncio.Future()
    future.set_result(number)
    return future

@asyncio.coroutine
def coro2():
    print("In coro2")
    future = asyncio.Future()
    # gather will collect exceptions too
    future.set_exception(ValueError)
    return future

loop = asyncio.get_event_loop()
# gather collects all coroutine futures and returns them as a list
results = loop.run_until_complete(asyncio.gather(
    coro1(1),
    coro1(2),
    coro1(3),
    coro2(),
    return_exceptions=True
))
print(results)
loop.close()

# Output
# -----------------------------
# python parallel_ioloop_tasks.py
# Task #3 started
# Task #1 started
# Task #2 started
# In coro2
# Task #3 ended
# Task #1 ended
# Task #2 ended
# [<Future finished result=1>, <Future finished result=2>, <Future finished result=3>, ValueError()]
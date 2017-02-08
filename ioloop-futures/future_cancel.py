__author__ = 'psuresh'

import asyncio
import concurrent.futures


@asyncio.coroutine
def slow_operation(future):
    print("running task")
    yield from asyncio.sleep(5)
    try:
        future.result()
    except concurrent.futures.CancelledError:
        print('future has been cancelled by another task')

@asyncio.coroutine
def another_operation(future):
    print('cancelling future')
    future.cancel()
    print('future cancelled:', future.cancelled())


loop = asyncio.get_event_loop()
future = asyncio.Future()
print("future created")
print("task scheduled")
asyncio.ensure_future(another_operation(future))
loop.run_until_complete(slow_operation(future))
print("loop complete")
loop.close()


# Output
# --------------------------------------
# python future_cancel.py
# future created
# task scheduled
# cancelling future
# future cancelled: True
# running task
# future has been cancelled by another task
# future complete
__author__ = 'psuresh'

import asyncio


@asyncio.coroutine
def slow_operation(future):
    print("running task")
    yield from asyncio.sleep(1)
    future.set_result('result!!!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
print("future created")
print("task scheduled")
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)
print("future complete")
print(future.result())
loop.close()


# Output
# --------------------------------------
# python future_complete.py
# future created
# task scheduled
# running task
# future complete
# result!!!
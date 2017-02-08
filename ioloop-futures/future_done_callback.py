__author__ = 'psuresh'

import asyncio


@asyncio.coroutine
def slow_operation(future):
    print("inside task")
    yield from asyncio.sleep(1)
    print("task done")
    future.set_result('Future is done!')


def got_result(future):
    print("inside callback")
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop()
future = asyncio.Future()
print("future initialized")
print("task scheduled")
asyncio.ensure_future(slow_operation(future))
future.add_done_callback(got_result)
try:
    loop.run_forever()
finally:
    loop.close()


# Output
# ------------------------------
# python future_done_callback.py
# future initialized
# task scheduled
# inside task
# task done
# inside callback
# Future is done!

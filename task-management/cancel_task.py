__author__ = 'psuresh'

import asyncio

@asyncio.coroutine
def task_func():
    print('in task_func')
    return 'the result'

@asyncio.coroutine
def main(loop):
    print('creating task')
    task = loop.create_task(task_func())

    print('canceling task')
    task.cancel()

    print('canceled task {!r}'.format(task))
    try:
        yield from task
    except asyncio.CancelledError:
        print('caught error from canceled task')
    else:
        print('task result: {!r}'.format(task.result()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

# Output
# ---------------------------------------------------------------------
# python cancel_task.py
# creating task
# canceling task
# canceled task <Task cancelling coro=<coro() running at /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/coroutines.py:204>>
# caught error from canceled task
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
    print('waiting for {!r}'.format(task))
    return_value = yield from task
    print('task completed {!r}'.format(task))
    print('return value: {!r}'.format(return_value))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

# Outlook
# ------------------------------------------------------------------------------------------------------------------
# python create_task.py
# creating task
# waiting for <Task pending coro=<coro() running at /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/coroutines.py:204>>
# in task_func
# task completed <Task finished coro=<coro() done, defined at /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/coroutines.py:204> result='the result'>
# return value: 'the result'

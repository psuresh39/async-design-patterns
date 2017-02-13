__author__ = 'psuresh'

import asyncio

@asyncio.coroutine
def bug():
    raise Exception("not consumed")

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(bug())
loop.run_until_complete(task)


# Output
# python uncaught_exception.py
# Traceback (most recent call last):
#   File "uncaught_exception.py", line 11, in <module>
#     loop.run_until_complete(task)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/base_events.py", line 337, in run_until_complete
#     return future.result()
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/futures.py", line 274, in result
#     raise self._exception
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/tasks.py", line 239, in _step
#     result = coro.send(None)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/coroutines.py", line 206, in coro
#     res = func(*args, **kw)
#   File "uncaught_exception.py", line 7, in bug
#     raise Exception("not consumed")
# Exception: not consumed

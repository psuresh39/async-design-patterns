__author__ = 'psuresh'

import asyncio

@asyncio.coroutine
def bug():
    raise Exception("not consumed")


# Catch exception method #1
@asyncio.coroutine
def handle_exception():
    try:
        yield from bug()
    except Exception:
        print("exception consumed")

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(handle_exception())
loop.run_until_complete(task)


# Catch exception method #2
task = asyncio.ensure_future(bug())
try:
    loop.run_until_complete(task)
except Exception:
    print("exception consumed")

# Output
# ---------------------------------------------------------------
# python caught_exceptions.py
# exception consumed
# exception consumed

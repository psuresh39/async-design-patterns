__author__ = 'psuresh'

# Use when the tasks are fixed, known and well-defined

import asyncio


@asyncio.coroutine
def phase1():
    print('in phase1')
    yield from asyncio.sleep(2)
    print('done with phase1')
    return 'phase1 result'


@asyncio.coroutine
def phase2():
    print('in phase2')
    yield from asyncio.sleep(1)
    print('done with phase2')
    return 'phase2 result'


@asyncio.coroutine
def main():
    print('starting main')
    print('waiting for phases to complete')
    results = yield from asyncio.gather(
        phase1(),
        phase2(),
    )
    print('results: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())
finally:
    event_loop.close()

# Output
# -----------------------------------------------------------------
# python gather_tasks.py
# starting main
# waiting for phases to complete
# in phase1
# in phase2
# done with phase2
# done with phase1
# results: ['phase1 result', 'phase2 result']
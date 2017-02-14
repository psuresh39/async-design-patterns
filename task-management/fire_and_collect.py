__author__ = 'psuresh'

# Use when the number of tasks fired are unknown and dynamic

import asyncio

@asyncio.coroutine
def phase(i):
    print('in phase {}'.format(i))
    yield from asyncio.sleep(0.1 * i)
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


@asyncio.coroutine
def main(num_phases):
    print('starting main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('waiting for phases to complete')
    completed, pending = yield from asyncio.wait(phases, timeout=0.2)

    results = [t.result() for t in completed]
    print('results: {!r}'.format(results))

    # Kill pending tasks
    for t in pending:
        print("cancelling task: ", t)
        t.cancel()


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

# Output
# --------------------------------------------------------------------
# python fire_and_collect.py
# starting main
# waiting for phases to complete
# in phase 1
# in phase 0
# in phase 2
# done with phase 0
# done with phase 1
# results: ['phase 1 result', 'phase 0 result']
# cancelling task:  <Task pending coro=<phase() running at fire_and_collect.py:9> wait_for=<Future finished result=None>>

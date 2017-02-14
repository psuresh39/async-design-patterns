__author__ = 'psuresh'

# Use when you need to fire multiple coroutines in parallel and collect results as they finish

import asyncio


@asyncio.coroutine
def phase(i):
    print('in phase {}'.format(i))
    yield from asyncio.sleep(0.5 - (0.1 * i))
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


@asyncio.coroutine
def main(num_phases):
    results = []
    phases = [phase(i) for i in range(num_phases)]
    for task in asyncio.as_completed(phases):
        result = yield from task
        results.append(result)
    print(results)


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

# Output
# --------------------------------------------------------------------------
# python coroutines_as_they_finish.py
# in phase 0
# in phase 2
# in phase 1
# done with phase 2
# done with phase 1
# done with phase 0
# ['phase 2 result', 'phase 1 result', 'phase 0 result']


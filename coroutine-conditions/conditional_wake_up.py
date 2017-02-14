__author__ = 'psuresh'

import asyncio
import concurrent.futures
import functools


def predicate(n):
    return n % 2 == 0

@asyncio.coroutine
def consumer(condition, n):
    try:
        with (yield from condition):
            print('consumer {} is waiting'.format(n))
            yield from condition.wait_for(functools.partial(predicate, n))
            print('consumer {} triggered'.format(n))
        print('ending consumer {}'.format(n))
    except concurrent.futures.CancelledError:
        pass


@asyncio.coroutine
def manipulate_condition(condition):
    print('starting manipulate_condition')

    # pause to let consumers start
    yield from asyncio.sleep(0.2)

    for i in range(1, 3):
        with (yield from condition):
            print('notifying {} consumers'.format(i))
            condition.notify(n=i)
        yield from asyncio.sleep(0.1)

    with (yield from condition):
        print('notifying remaining consumers')
        condition.notify_all()

    # kill all pending tasks
    for task in asyncio.Task.all_tasks():
        task.cancel()

    print('ending manipulate_condition')


@asyncio.coroutine
def main(loop):
    # Create a condition
    condition = asyncio.Condition()

    # Set up tasks watching the condition
    consumers = [
        consumer(condition, i)
        for i in range(10)
    ]

    # Schedule a task to manipulate the condition variable
    loop.create_task(manipulate_condition(condition))

    # Wait for the consumers to be done
    yield from asyncio.wait(consumers)


event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(main(event_loop))
except concurrent.futures.CancelledError:
    pass
finally:
    event_loop.close()

# Output
# ------------------------------------------------------------------------
# python conditional_wake_up.py
# starting manipulate_condition
# consumer 1 is waiting
# consumer 8 is waiting
# consumer 8 triggered
# ending consumer 8
# consumer 9 is waiting
# consumer 2 is waiting
# consumer 2 triggered
# ending consumer 2
# consumer 3 is waiting
# consumer 4 is waiting
# consumer 4 triggered
# ending consumer 4
# consumer 5 is waiting
# consumer 6 is waiting
# consumer 6 triggered
# ending consumer 6
# consumer 7 is waiting
# consumer 0 is waiting
# consumer 0 triggered
# ending consumer 0
# notifying 1 consumers
# notifying 2 consumers
# notifying remaining consumers
# ending manipulate_condition

__author__ = 'psuresh'


import asyncio
import concurrent.futures
import logging
import sys
import time


def blocks(n):
    log = logging.getLogger('blocks({})'.format(n))
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    return n ** 2


@asyncio.coroutine
def run_blocking_tasks(executor):
    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')

    log.info('creating executor tasks')
    loop = asyncio.get_event_loop()
    blocking_tasks = [
        loop.run_in_executor(executor, blocks, i)
        for i in range(6)
    ]
    log.info('waiting for executor tasks')
    completed, pending = yield from asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))

    log.info('exiting')


if __name__ == '__main__':
    # Configure logging to show the name of the thread
    # where the log message originates.
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    # Create a limited thread pool.
    executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=3,
    )

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            run_blocking_tasks(executor)
        )
    finally:
        event_loop.close()


# Output
# ------------------------------------------------------------------------
# python thread_executor.py
# MainThread run_blocking_tasks: starting
# MainThread run_blocking_tasks: creating executor tasks
#   Thread-1          blocks(0): running
#   Thread-2          blocks(1): running
#   Thread-3          blocks(2): running
# MainThread run_blocking_tasks: waiting for executor tasks
#   Thread-1          blocks(0): done
#   Thread-1          blocks(3): running
#   Thread-3          blocks(2): done
#   Thread-2          blocks(1): done
#   Thread-3          blocks(4): running
#   Thread-2          blocks(5): running
#   Thread-1          blocks(3): done
#   Thread-2          blocks(5): done
#   Thread-3          blocks(4): done
# MainThread run_blocking_tasks: results: [1, 0, 25, 9, 16, 4]
# MainThread run_blocking_tasks: exiting
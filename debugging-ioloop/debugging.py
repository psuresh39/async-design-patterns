__author__ = 'psuresh'

import argparse
import asyncio
import logging
import sys
import time
import warnings

parser = argparse.ArgumentParser('debugging asyncio')
parser.add_argument(
    '-v',
    dest='verbose',
    default=False,
    action='store_true',
)
args = parser.parse_args()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)7s: %(message)s',
    stream=sys.stderr,
)
LOG = logging.getLogger('asyncio')

@asyncio.coroutine
def inner():
    LOG.info('inner starting')
    # Use a blocking sleep to simulate
    # doing work inside the function.
    time.sleep(3)
    LOG.info('inner completed')


@asyncio.coroutine
def outer(loop):
    LOG.info('outer starting')
    yield from asyncio.ensure_future(loop.create_task(inner()))
    LOG.info('outer completed')


event_loop = asyncio.get_event_loop()

if args.verbose:
    LOG.info('enabling debugging')

    # Enable debugging
    event_loop.set_debug(True)

    # Make the threshold for "slow" tasks very very small for
    # illustration. The default is 0.1, or 100 milliseconds.
    event_loop.slow_callback_duration = 0.001

    # Report all mistakes managing asynchronous resources.
    warnings.simplefilter('always', ResourceWarning)

LOG.info('entering event loop')
event_loop.run_until_complete(outer(event_loop))


# python debugging.py
#   DEBUG: Using selector: KqueueSelector
#    INFO: entering event loop
#    INFO: outer starting
#    INFO: inner starting
#    INFO: inner completed
#    INFO: outer completed
#
#
# python debugging.py -v
#   DEBUG: Using selector: KqueueSelector
#    INFO: enabling debugging
#    INFO: entering event loop
#    INFO: outer starting
# WARNING: Executing <Task pending coro=<outer() running at debugging.py:38> wait_for=<Task pending coro=<coro() running at /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/coroutines.py:204> cb=[Task._wakeup()] created at debugging.py:38> cb=[_run_until_complete_cb() at /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/base_events.py:118] created at /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/base_events.py:317> took 0.002 seconds
#    INFO: inner starting
#    INFO: inner completed
# WARNING: Executing <Task finished coro=<coro() done, defined at /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/coroutines.py:204> result=None created at debugging.py:38> took 3.005 seconds
#    INFO: outer completed
# /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/asyncio/base_events.py:379: ResourceWarning: unclosed event loop <_UnixSelectorEventLoop running=False closed=False debug=True>
#   DEBUG: Close <_UnixSelectorEventLoop running=False closed=False debug=True>

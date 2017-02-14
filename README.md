# async-design-patterns
Async code is different from regular code. This repo has small snippets of async code that solve specific async problems. These patterns could apply to web services and embedded systems alike.

To run any of these patterns simply `cd` to the folder and run individual file with `python`.

Supports `Python 3.4` . For `Python 3.5`, code will need to be refactored as follows:

* use `async def` instead of `@asyncio.coroutine` decorator in coroutine definition
* use `await` instead of `yield from` as the yield statement

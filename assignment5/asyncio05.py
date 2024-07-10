from random import random
import asyncio

#coroutine to execute in a new task
async def RICE():
    value = 1 + random()
    print(f'Rice is cooking : {value} seconds')
    await asyncio.sleep(value)
    #report the value
    return f'> Rice done with {value} seconds'

async def NOODLE():
    value = 1 + random()
    print(f'Noodle is cooking : {value} seconds')
    await asyncio.sleep(value)
    #report the value
    return f'> Noodle done with {value} seconds'

async def CURRY():
    value = 1 + random()
    print(f'Curry is cooking : {value} seconds')
    await asyncio.sleep(value)
    #report the value
    return f'> Curry done with {value} seconds'

#main coroutine
async def main():
    #create many tasks
    tasks = [asyncio.create_task(RICE()), 
             asyncio.create_task(NOODLE()),
             asyncio.create_task(CURRY())
            ]
    #wait for all tasks to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    #report results
    #get the first task to complete
    first = done.pop()
    print(first.result(), '\n', 'task', {len(pending)} ,'Unfinished')
#start the asyncio program
asyncio.run(main())
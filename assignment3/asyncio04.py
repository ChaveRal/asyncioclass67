# Starting task
from time import ctime
import asyncio

async def wash(basket):
    print(f'{ctime()} : Washing Machine ({basket}):Put the coin') #coming after run from line 22
    print(f'{ctime()} : Washing Machine ({basket}):Start Washing...')
    await asyncio.sleep(5)
    print(f'{ctime()} : Washing Machine ({basket}):Finished Washing...')
    return f'{ctime()} : {basket} is completed' #Return the finishing basket

async def main ():
    #create coroutine
    coro = wash('Basket A') #return object name coroutine 
    print(f'{ctime()} : {coro}')
    print(f'{ctime()} : {type(coro)}')
    #Create task
    task = asyncio.create_task(coro) #create task from cotoutine but didn't run 
    print(f'{ctime()} : {task}')
    print(f'{ctime()} : {type(task)}')
    #run the task
    result = await task #start washing by the command await task => use coroutine to run task 
    print(f'{ctime()} : {result}')

if  __name__=='__main__':
    asyncio.run(main())
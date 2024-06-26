# example of running a coroutine
import asyncio
#define a coroutine
async def custom_coro():
    #await another coroutine
    await asyncio.sleep(1)# sleep without wating for any task
    #whenever has async has await follow with asynchronous function and don't block

#main coroutine
async def main(): #coroutine call custom_coro without waiting for result
    #execute my custom coroutine
    await custom_coro()
#start the coroutine program
asyncio.run(main()) #creat something for control

import asyncio

async def brew_coffee():
    print("Brewing starts..")
    await asyncio.sleep(2)
    print("Ready to serve!")

asyncio.run(brew_coffee())

## async/await runs on the main thread (or the calling thread) without blocking or freezing it while it waits

import asyncio

async def brew_coffee(name):
    print(f"{name} starts brewing..")
    await asyncio.sleep(3)
    print(f"{name} is ready")
    
async def main():
    await asyncio.gather(brew_coffee("Capuccino"), brew_coffee("Latte"), 
    brew_coffee("Mocha"))
    
asyncio.run(main())

## non blocking thread, so will process whole thing in 3 seconds

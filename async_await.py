import asyncio

async def get_user():
    
    print("Initializing the user......")
    
    await asyncio.sleep(3) ## After 3 seconds
    
    print("Done!")
    
async def main():
    await get_user()
    
print("Execution started...")
asyncio.run(main())

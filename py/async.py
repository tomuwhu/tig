import asyncio

async def gen(s):
    for i in range(len(s)+1):
        await asyncio.sleep(0.2)
        yield s[:i]

async def main():
    async for i in gen('géza_kék_az_ég'):
        print(i)

asyncio.run(main())
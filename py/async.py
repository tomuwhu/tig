import asyncio

async def gen(s):
    for i in range(len(s)+1):
        await asyncio.sleep(0.2)
        yield s[:i]

async def main():
    async for i in gen('géza kék az ég'):
        print(i)

asyncio.run(main())
import time 
import asyncio
import requests
# Async function is used to run all the functions simultaneously
async def function1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram1.ico", "wb").write(response.content)
    
    print("func 1")

async def function2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram2.ico", "wb").write(response.content)

    print("func 2")

async def function3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)

    print("func 3")

async def main():
    # L = await asyncio.gather(
    #     function1(),
    #     function2(),
    #     function3(),
    # )
    # print(L)

    task = asyncio.create_task(function1())
    await function1()
    await function2()
    await function3()
asyncio.run(main())
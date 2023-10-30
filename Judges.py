import aiohttp
import asyncio

async def check_judges_status_async(websites):
    online_websites = []

    async with aiohttp.ClientSession() as session:
        tasks = [check_website(session, website, online_websites) for website in websites]
        await asyncio.gather(*tasks)

    with open("judges.txt", "w") as file:
        for item in online_websites:
            file.write(f"{item}\n")

    return online_websites

async def check_website(session, website, online_websites):
    try:
        async with session.get(website) as response:
            if response.status == 200:
                online_websites.append(website)
                print(f"{website} is online")
            else:
                print(f"{website} is offline (Status Code: {response.status})")
    except aiohttp.ClientError:
        print(f"{website} is offline (Connection Error)")

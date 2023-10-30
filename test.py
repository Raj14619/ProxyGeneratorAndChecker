

import aiohttp
import asyncio
import random  # Add the random module for website selection

# Function to read proxy IP:Port combinations from a text file
def read_proxies(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Function to read websites to test from a text file
def read_websites(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Function to test a single proxy with a random website asynchronously
async def test_single_proxy(session, proxy, websites):
    working_proxies = []
    website = random.choice(websites)  # Randomly select a website
    try:
        async with session.get(website, proxy=proxy, timeout=15) as response:
            if response.status == 200:
                print(f'Proxy {proxy} works for {website}')
                working_proxies.append(proxy)
            else:
                print(f'Proxy {proxy} does not work for {website}')
    except Exception as e:
        print(f'Proxy {proxy} failed for {website}: {str(e)}')
    return working_proxies

async def http_test():
    # Read proxy IP:Port combinations from the 'proxies.txt' file
    proxy_lines = read_proxies('http_to_test.txt')

    # Read websites to test from the 'websites.txt' file
    websites = read_websites('judges.txt')

    # Create a list of proxy URLs
    proxies = [f'http://{proxy}' for proxy in proxy_lines]

    working_proxies = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for proxy in proxies:
            tasks.append(test_single_proxy(session, proxy, websites))
        results = await asyncio.gather(*tasks)
        for result in results:
            if result:
                working_proxies.extend(result)

    # Write the working proxies to a new text file without "http://"
    with open('working_proxies.txt', 'w') as output_file:
        for proxy in working_proxies:
            # Remove "http://" from the beginning of each proxy
            proxy = proxy.replace('http://', '')
            output_file.write(f'{proxy}\n')

    print(f'Number of working proxies: {len(working_proxies)}')


import aiohttp
import asyncio
import datetime
import os
import time


async def main(date_dir, tokens):
    async with aiohttp.ClientSession() as session:
        for i in range(0, len(tokens)):
            headers = {"Authorization": f"OAuth {tokens[i]}"}
            response = await session.get("https://id.twitch.tv/oauth2/validate", headers=headers)
            if response.status == 200:
                open(f"{date_dir}/good-tokens.txt", "a").write(f"{tokens[i]}\n")
            else:
                open(f"{date_dir}/bad-tokens.txt", "a").write(f"{tokens[i]}\n")
    open(f"{date_dir}/all-tokens.txt", "w").write(open("all-tokens.txt", "r").read())


if __name__ == '__main__':
    start_time = time.time()
    date = datetime.datetime.now().strftime("%m.%d.%Y-%H.%M.%S")
    os.mkdir(date)
    all_tokens = open("all-tokens.txt", "r").read().splitlines()
    asyncio.get_event_loop().run_until_complete(main(date, all_tokens))
    print("--- %s seconds ---" % (time.time() - start_time))

import asyncio

async def async_pr(st, delay=1):
	for line in st.splitlines():
	    print(line)
	    await asyncio.sleep(delay)

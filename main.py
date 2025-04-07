import asyncio
import httpx

async def test_httpx():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get('https://httpbin.org/get')
            response.raise_for_status()
            print(f"Status Code: {response.status_code}")
            print(f"Response Data: {response.json()}")
        except httpx.HTTPError as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(test_httpx())

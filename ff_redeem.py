from perplexity import AsyncPerplexity
import asyncio
import re
import os
from datetime import datetime
import dotenv

dotenv.load_dotenv()

client = AsyncPerplexity(api_key=os.getenv("PERPLEXITY_API_KEY"))

async def get_ff_codes(for_date=None):
    if for_date is None:
        # Use today's date by default
        for_date = datetime.now()
    # Format date string as "26 October 2025"
    date_str = for_date.strftime("%d %B %Y")
    query = f"Free Fire redeem codes for {date_str}"

    search_res = await client.search.create(query=query, max_results=20)
    codes = set()
    for item in search_res.results:
        found = re.findall(r"\bFF[A-Z0-9\-]{7,}\b", item.snippet)
        codes.update(code.replace("-", "") for code in found)
    return list(codes)

# Example: Use today
codes_today = asyncio.run(get_ff_codes())
print("Today's codes:", codes_today)

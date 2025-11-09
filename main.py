# import asyncio
# import os
# import json
# import dotenv
# from perplexity import AsyncPerplexity

# # Load environment variables
# dotenv.load_dotenv()

# client = AsyncPerplexity(api_key=os.getenv("PERPLEXITY_API_KEY"))

# async def batch_search(queries, batch_size=2, delay_ms=1000):
#     results = []

#     for i in range(0, len(queries), batch_size):
#         batch = queries[i:i + batch_size]
#         batch_tasks = [client.search.create(query=query, max_results=5) for query in batch]

#         batch_results = await asyncio.gather(*batch_tasks)

#         # Extract relevant fields from the Pydantic object
#         for search_response in batch_results:
#             for item in search_response.results:
#                 results.append({
#                     "description": (item.snippet or "").strip().replace("\n", " "),
#                     "date": item.date or "unknown",
#                     "source": item.url or "unknown"
#                 })

#         if i + batch_size < len(queries):
#             await asyncio.sleep(delay_ms / 1000)

#     return results


# # Usage
# queries = ["AI developments", "Space News", "Quantum Computing"]
# final_results = asyncio.run(batch_search(queries))

# # Pretty-print formatted JSON
# print(json.dumps(final_results, indent=2, ensure_ascii=False))
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

if __name__ == "__main__":
    app.run()

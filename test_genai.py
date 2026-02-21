import asyncio
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')

async def main():
    print("Testing generate_content_async")
    try:
        response = await model.generate_content_async("Say hi in 1 word")
        print("Response:", response.text)
    except Exception as e:
        print("Error:", type(e), e)

if __name__ == '__main__':
    asyncio.run(main())

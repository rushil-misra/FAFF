import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from langchain_ollama import ChatOllama


async def main():
    agent = Agent(
        task="search what is a dog and print the first result",
        llm=ChatOllama(model="llama3.2:1b"),
    )
    await agent.run()

asyncio.run(main())
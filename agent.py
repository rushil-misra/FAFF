import asyncio
from dotenv import load_dotenv
load_dotenv()
import os
from browser_use import Agent, Controller, ActionResult, BrowserSession,BrowserProfile
from langchain_openai import ChatOpenAI

controller = Controller()

# aadhar_number = str(input('write down your aadhar number without gaps --'))
# firstName = str(input('give your first name -- '))
# yob = str(input('give your year of birth (eg - 2004) -- '))

aadhar_number = 681993142042

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# browser_session = BrowserSession(
#     browser_profile= BrowserProfile(accept_downloads=True,keep_alive=True,downloads_path="")
# )


async def main():
    agent = Agent(
        task=f"open new tab - https://myaadhaar.uidai.gov.in/genricDownloadAadhaar/en, enter aadhar number - {aadhar_number}. after this the user will complete the process so leave browser open",
        llm=llm,
        save_conversation_path='logs/browserAgent',
        browser_profile=BrowserProfile(accept_downloads=True,keep_alive=True,downloads_dir=r'/document'),
        
        
    )
    # await agent.run()

    while True:
        await agent.run()
        allow = str(input('did you recieve the document ? (yes/no) --'))
        if allow == 'yes':
            break
        else:
            continue

        




# @controller.action('Ask human to fill captcha')   # pass allowed_domains= or page_filter= to limit actions to certain pages
# def ask_human(question: str) -> ActionResult:
#     answer = input(f'\n{question}\nInput: ')
#     return ActionResult(extracted_content=answer, include_in_memory=True)


# def user_allows():
#     allow = str(input('did you recieve the document ? (yes/no) --'))
#     if allow == 'yes':
#         pass



asyncio.run(main())

# problems with the code - uses workaround instead of the correct way, i did this 
# due to lack of the knowledge of the library and limited time
# sensitive data like aadhar number not handled properly
# intervention of user is not correct

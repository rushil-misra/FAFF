import asyncio
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import ChatOpenAI
from browser_use import Agent,BrowserProfile, BrowserSession

aadhar_number = str(input('write down your aadhar number without gaps --'))





sensitive_data = {'aadhar_number' : aadhar_number}

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(model="gpt-4o", temperature=0)

Browser_Session = BrowserSession(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',keep_alive = True,browser_profile=BrowserProfile(accept_downloads=True,downloads_path= 'downloads',keep_alive=0))


async def main():
    
    agent = Agent(
        task=f"open new tab - https://myaadhaar.uidai.gov.in/genricDownloadAadhaar/en, enter aadhar number . after this the user will complete the process so leave browser open",
        llm=llm,
        save_conversation_path='logs/browserAgent',
        browser_session=Browser_Session,
        sensitive_data=sensitive_data
            
            
        )
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

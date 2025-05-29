from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, BrowserConfig, Browser
from browser_use.browser.context import BrowserContextConfig, BrowserContext
from dotenv import load_dotenv
import asyncio
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure browser settings
browser_config = BrowserConfig(
    headless=False,  # Set to True for headless mode
    disable_security=True
)

# Initialize browser and context
browser = Browser(config=browser_config)

browser_session = Browser(config=browser_config)
actual_browser = browser_session.browser 

context_config = BrowserContextConfig(
    wait_for_network_idle_page_load_time=3.0,
    browser_window_size={'width': 1280, 'height': 1100},
    locale='en-US',
    highlight_elements=True,
    viewport_expansion=500,
)

context = BrowserContext(browser=actual_browser, config=context_config)

# Initialize the AI model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17", google_api_key=api_key)

# Define the task for the AI agent
task = "Find the cheapest nonstop flight from Dubai to COK (Cochin) in economy class for tomorrow for one passenger."

# Define the main async function
async def main():
    agent = Agent(
        browser=actual_browser,
        # context_config=context_config,
        task=task,
        llm=llm,
    )
    result = await agent.run()
    print("Cheapest Flight Details:", result)

# Run the async function
asyncio.run(main())
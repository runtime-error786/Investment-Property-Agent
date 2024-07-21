
import os
from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama
from tools import search_tool
from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     verbose=True,
#     temperature=0.5,
#     google_api_key="AIzaSyDx1SB8FSX6UbzSpFG9vtC8dDA6WLXKtXw"
# )

llm = Ollama(model="openhermes")
researcher = Agent(
    llm=llm,
    role="Property Researcher",
    goal="Find promising investment properties in {country}.",
    backstory="You are an experienced property analyst specializing in identifying profitable investment opportunities.",
    allow_delegation=True,
    tools=[search_tool],
    verbose=True,
)



writer = Agent(
    llm=llm,
    role="Property Analyst",
    goal="Summarize property facts into a report for investors of {country}.",
    backstory="You are a skilled real estate analyst with a knack for creating insightful reports.",
    allow_delegation=False,
    verbose=True,
    tools=[search_tool]
)





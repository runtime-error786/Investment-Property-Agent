
from crewai_tools import SerperDevTool
import os

# Set environment variables
# if search throgh internet
os.environ["SERPER_API_KEY"] = "3af0a4b6c908b084bae181b6e2dbfd67dbd76aa1"
search_tool = SerperDevTool()
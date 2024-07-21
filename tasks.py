from crewai import Agent, Task, Crew
from agents import researcher,writer


task1 = Task(
    description="""Research and find 3 promising investment properties in {country}. 
                   Include the name of the property, city, country, location for each property.""",
    expected_output="""A detailed list of five properties with the following format:
    
    Property 1:
    name : [property name]
    City: [City Name]
    Country: Australia
    Location: [Location Details]

    ... and so on for 3 properties.""",
    agent=researcher
)


task2 = Task(
    description="Summarize the property information into a bullet point list for each property in comprehensive.",
    expected_output="""A summarized list of each property in comprehensive including :
    
    name : [property name]
    City: [City Name]
    Country: Australia
    Location: [Location Details]
    
    and so on...""",
    agent=writer,
    output_file="Report.txt",
)
from crewai import Agent, Task, Crew
from agents import researcher,writer


task1 = Task(
    description="""Research and find 5 promising investment properties in {country}. 
                   Include the name of the city, country, location, measurement, and profit or loss ratio for each property.""",
    expected_output="""A detailed list of five properties with the following format:
    
    Property 1:
    City: [City Name]
    Country: Australia
    Location: [Location Details]
    Measurement: [Measurement Details]
    Profit or Loss Ratio: [Ratio]
    ... and so on for 5 properties.""",
    agent=researcher
)


task2 = Task(
    description="Summarize the property information into a bullet point list for each property in comprehensive.",
    expected_output="""A summarized list of each property in comprehensive including :
    
    Property 1:
    City: [City Name]
    Country: Australia
    Location: [Location Details]
    Measurement: [Measurement Details]
    Profit or Loss Ratio: [Ratio]
    
    and so on...""",
    agent=writer,
    output_file="Report.txt",
)
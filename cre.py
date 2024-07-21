from crewai import Agent, Task, Crew
from agents import researcher,writer
from tasks import task1,task2

crew = Crew(agents=[researcher, writer], tasks=[task1, task2], verbose=2)
task_output = crew.kickoff(inputs={'country': 'Australia'})
print(task_output)
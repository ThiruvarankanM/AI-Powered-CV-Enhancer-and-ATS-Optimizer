from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
import sys
sys.path.append(os.path.dirname(__file__))
from tools.custom_tool import CVParseTool

@CrewBase
class CvEnhancer():
    """CV Enhancement Crew"""

    @agent
    def cv_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_analyst'],
            verbose=True
        )

    @agent  
    def cv_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_writer'],
            verbose=True
        )

    @task
    def analyze_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_task']
        )

    @task
    def enhance_task(self) -> Task:
        return Task(
            config=self.tasks_config['enhance_task']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CvEnhancer():
    """CvEnhancer crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # Professional multi-agent setup for CV enhancement
    # Analyzer Agent: Evaluates CV strengths/weaknesses
    @agent
    def analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['analyzer'],
            verbose=True
        )

    # Content Writer Agent: Rewrites and improves CV sections
    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer'],
            verbose=True
        )

    # ATS Optimizer Agent: Ensures CV is ATS-friendly
    @agent
    def ats_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['ats_optimizer'],
            verbose=True
        )

    # Industry Expert Agent: Provides sector-specific advice
    @agent
    def industry_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['industry_expert'],
            verbose=True
        )

    # Task: Analyze CV
    @task
    def analyze_cv_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_cv_task'],
        )

    # Task: Rewrite/Improve CV
    @task
    def rewrite_cv_task(self) -> Task:
        return Task(
            config=self.tasks_config['rewrite_cv_task'],
        )

    # Task: Optimize for ATS
    @task
    def ats_optimize_task(self) -> Task:
        return Task(
            config=self.tasks_config['ats_optimize_task'],
        )

    # Task: Add Industry Advice
    @task
    def industry_advice_task(self) -> Task:
        return Task(
            config=self.tasks_config['industry_advice_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CvEnhancer crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

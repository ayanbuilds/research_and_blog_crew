from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


# Define the class for our Crew (Compiling the Crew)
@CrewBase
class ResearchAndBlogCrew:
    
    agents: list[BaseAgent] #jo bhi agents honge unka ye basically varible hai jisme list hogi humare agents ki
    tasks: list[Task] # same as agents

    #Define the paths of config file (Means kahan se load karne hn agents and tasks)
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # Compiling Agents (Order does not matter here)

    @agent
    def report_generator(self) -> Agent:  # same function name as agent name
        return Agent(
            config=self.agents_config['report_generator']
        )
    
    @agent
    def blog_writer(self) -> Agent:  # same function name as agent name
        return Agent(
            config=self.agents_config['blog_writer']
        )
    

    # Compiling tasks (Order matters)

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_task']
        )
    
    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_writing_task'],
            output_file= "blogs/blog.md"
        )
    
    #  Defining Crew

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

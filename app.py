from crewai import Crew
from agents import TripPlannerAgents
from tasks import TripTasks

date_range = 'June-Sep 24'
origin = 'Vellore'
interests = 'Studying and good food'
cities = 'Vellore,  Chennai'

agents = TripPlannerAgents()
city_selector_agent = agents.city_selection_agent()
local_expert_agent = agents.local_expert()
travel_concierge_agent = agents.travel_concierge()


tasks = TripTasks()
identify_task = tasks.identify_task(city_selector_agent, origin, cities, interests, date_range)
gather_task = tasks.gather_task(city_selector_agent, origin, interests, date_range)
plan_task = tasks.plan_task(city_selector_agent, origin, interests, date_range)


# Create a crew and kickoff the planning process
crew = Crew(
  agents=[city_selector_agent, local_expert_agent, travel_concierge_agent],
  tasks=[identify_task, gather_task, plan_task]
)

result = crew.kickoff()
print(result)
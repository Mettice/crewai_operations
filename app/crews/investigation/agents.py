from crewai import Agent
from app.config import settings
from app.crews.investigation.tools import get_customer,get_subscription,get_payment,get_ticket_history



def create_investigator_agent()->Agent:
    return Agent(
        role='Ticket Investigation Agent',
        goal='Accurately investigate support tickets based on their content and context.',
        backstory="""You are an expert in IT support and customer service. You have years of experience 
        investigating and resolving support tickets. You are able to quickly understand the 
        content and context of a support ticket and accurately investigate and resolve it.
        """,
        verbose=True,
        allow_delegation=False,
        llm=settings.model_name,
        tools=[
            get_customer,
            get_subscription,
            get_payment,
            get_ticket_history,
        ]
    )

       
        
    

from crewai.flow.flow import Flow, listen, start
from app.crews.triage.crew import run_triage_crew
from app.models.ticket import SupportTicket
from app.crews.investigation.crew import run_investigation_crew

class SupportFlow(Flow):
    @start()
    def triage_ticket(self):
        ticket = SupportTicket(
            ticket_id=self.state['ticket_id'],
            customer_id=self.state['customer_id'],
            subject=self.state['subject'],
            description=self.state['description']
        )

        result = run_triage_crew(ticket)
        self.state['ticket'] = ticket
        self.state['triage_result'] = result

        return self.state['triage_result']

    @listen(triage_ticket)
    def investigate_ticket(self, triage_result):
        result = run_investigation_crew(
            ticket=self.state['ticket'],
            triage_result=triage_result
        )
        self.state['investigation_result'] = result

        return self.state['investigation_result']
    

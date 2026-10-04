from fastapi import APIRouter
from app.models.ticket import SupportTicket
from app.flows.support_flow import SupportFlow

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/")
def triage_ticket_flow(ticket:SupportTicket):
    flow = SupportFlow()
    result = flow.kickoff(
        inputs={
            'ticket_id': ticket.ticket_id,
            'customer_id': ticket.customer_id,
            'subject': ticket.subject,
            'description': ticket.description
        }
    )
    
    return {
        "ticket_id": ticket.ticket_id,
        "triage_result": flow.state.get("triage_result"),
        "investigation_result": flow.state.get("investigation_result"),
    }
    
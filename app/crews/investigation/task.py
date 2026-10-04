from crewai import Task

from app.models.ticket import SupportTicket
from app.schemas.triage import TriageResult
from app.schemas.investigation import InvestigationResult


def create_investigation_task(
    agent,
    ticket:SupportTicket,
    triage_result:TriageResult
) -> Task:
    return Task(
        description=f"""You are investigating a customer support ticket. The ticket details are as follows:
        Ticket ID: {ticket.ticket_id}
        Customer ID: {ticket.customer_id}
        Subject: {ticket.subject}
        Description: {ticket.description}
        
        Based on the following triage result:
        Category: {triage_result.category}
        Priority: {triage_result.priority}
        Risk Level: {triage_result.risk_level}
        Confidence: {triage_result.confidence}
        Reasoning: {triage_result.reasoning}
        
        Investigate the ticket and determine the following:
        1. Whether the customer is verified
        2. The customer's name
        3. The customer's subscription status
        4. The customer's subscription plan
        5. Whether there is a payment issue
        6. Whether there is a duplicate payment
        7. The amount of the duplicate payment (if any)
        8. The number of open tickets for the customer
        9. The evidence supporting the investigation
        10. A summary of the investigation


        Important rules

        Do not invent customer name
        do not refund,
        do not cancel,
        don't make any changes to the customer record


        """,
        expected_output="A structured InvestigationResult containing customer_verified, customer_name, subscription_status, subscription_plan, payment_issue_detected, duplicate_payment, duplicate_amount, open_tickets_count, evidence, and investigation_summary",
        output_pydantic=InvestigationResult,
        agent=agent
    )


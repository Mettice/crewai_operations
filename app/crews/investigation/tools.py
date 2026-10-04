from typing import Any
from crewai.tools import tool


CUSTOMER = {
    "CUST-001": {
    "id":"CUST-001",
    "name":"John Doe",
    "email":"johndoe@gmail.com"
    },
    "CUST-002": {
        "id":"CUST-002",
        "name":"Jane Doe",
        "email":"janedoe@gmail.com"
    }
}

SUBSCRIPTION = {
    "CUST-001":{
    "plan":"premium",
    "status":"active",
    "amount":49.99
    },
    "CUST-002":{
        "plan":"basic",
        "status":"active",
        "amount":29.99
    }
}

PAYMENT= {
    "CUST-001":[
    {"id":"TX-001",
    "amount":49.99,
    "status":"completed"
    },
    {"id":"TX-002",
    "amount":49.99,
    "status":"completed"  
    },
    {"id":"TX-003",
    "amount":49.99,
    "status":"failed"
    }
    ],
    "CUST-002":{
        "plan":"basic",
        "status":"active",
        "amount":29.99
    }
}

TICKET_HISTORY = {
    "CUST-001": [],
    "CUST-002":[
        {
            "id":"TKT-002",
            "subject":"Billing issue",
            "description":"I was charged twice for my subscription",
            "status":"resolved",
        }
    ],

}

@tool("get_customer")
def get_customer(customer_id:str)->dict:
    """Retrieve Customers data based on cutomer id"""
    customer = CUSTOMER.get(customer_id)

    if not customer:
        return{
            "found": False,
            "customer_id": customer_id,
        }
    return {
        "found":True,
        "customer":customer
    }


@tool("get_subscription")
def get_subscription(customer_id:str)->dict:
    """Retrieve Subscription data based on cutomer id"""
    subscription = SUBSCRIPTION.get(customer_id)
    if not subscription:
        return{
            "found":False,
            "customer_id": customer_id,
        }
    return {
        "found":True,
        "subscription":subscription
    }
    

@tool("get_payment")
def get_payment(customer_id:str)->dict:
    """Retrieve Payment data based on cutomer id"""
    payment = PAYMENT.get(customer_id)
    if not payment:
        return{
            "found":False,
            "customer_id": customer_id,
        }
    return {
        "found":True,
        "payment":payment
    }
    

@tool("get_ticket_history")
def get_ticket_history(customer_id:str)->dict:
    """Retrieve Ticket History data based on cutomer id"""
    ticket_history = TICKET_HISTORY.get(customer_id)
    if not ticket_history:
        return{
            "found":False,
            "customer_id": customer_id,
        }
    return {
        "found":True,
        "ticket_history":ticket_history
    }




    
    
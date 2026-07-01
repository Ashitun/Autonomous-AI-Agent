from fastapi import APIRouter
from models.request_model import AgentRequest
from services.agent_service import process_agent_request
router = APIRouter(
    prefix="/agent",
    tags=["agent"] 
    )

@router.post("/")
async def run_agent(agent_request : AgentRequest):
    response = process_agent_request(agent_request.request)
    return response
from agent.planner import create_plan
from agent.executor import execute_plan
from tools.document_tool import generate_document
from agent.reflector import reflect

def process_agent_request(user_request: str):
    plan = create_plan(user_request)

    results = execute_plan(
    user_request,
    plan
    )

    review = reflect(results)

    document_path = generate_document(
    plan["goal"],
    results
    )

    return {
    "goal": plan["goal"],
    "tasks": plan["tasks"],
    "review": review,
    "document": document_path
    }
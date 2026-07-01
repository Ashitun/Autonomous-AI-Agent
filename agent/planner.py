from agent.llm import ask_gemini
import json


def create_plan(user_request : str) :
    prompt = f"""
Create ONLY 5 high-level tasks.

Do not create unnecessary subtasks.

The tasks should be sufficient to generate a complete professional business document.

Return only valid JSON.

    Example:

    {{
        "goal":"Create AI Project Proposal",
        "tasks":[
            "Write Executive Summary",
            "Write Project Scope",
            "Write Timeline",
            "Write Budget",
            "Write Conclusion"
        ]
    }}

    User Request:

    {user_request}
    """
    response = ask_gemini(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try :
        plan = json.loads(response)
        return plan 
    except json.JSONDecodeError:
        return {
            "goal" : "planning Failed",
            "tasks" : [] ,
            "error" : "Invalid JSON received from Gemini"

        }



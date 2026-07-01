from agent.llm import ask_gemini

def execute_plan(user_request : str , plan : dict) :
    results = []

    for task in plan["tasks"]:
        prompt = f""" You are an experienced Business Analyst and Technical Writer.
        Original user request :
        {user_request}
        Overall Goal:
        {plan["goal"]}
        current_task :
        {task}
Write detailed, professional, well-structured content for ONLY this section.

Use formal business language.

If information is missing, make realistic assumptions and explicitly mention them.

Do not repeat information from other sections.

The output will be added to a Microsoft Word business document.
"""
        output = ask_gemini(prompt)
        results.append(
            {
                "task" : task,
                "content" : output
            }
        )
        return results


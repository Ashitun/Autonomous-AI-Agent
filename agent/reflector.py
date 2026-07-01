from agent.llm import ask_gemini


def reflect(results: list):

    prompt = f"""
You are an AI reviewer.

Review the generated content below.

Check whether every planned task has meaningful content.

If every task has been completed successfully, return ONLY:

PASS

Otherwise return ONLY:

FAIL

Generated Content:

{results}
"""

    response = ask_gemini(prompt)

    response = response.strip().upper()

    if "PASS" in response:
        return "PASS"

    return "FAIL"
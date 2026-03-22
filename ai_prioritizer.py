from openai import OpenAI

client = OpenAI()


def prioritize_tasks_with_ai(tasks):
    prompt = f"""
You are an AI academic advisor.

Tasks:
{tasks}

Rank tasks from highest to lowest priority.

Consider:
- deadline urgency
- estimated hours needed
- difficulty
- academic importance/weight

Return STRICTLY in this format:

1. Task Name - Reason
2. Task Name - Reason
3. Task Name - Reason

Recommended first task: Task Name
Summary: Explain in 1-2 sentences how you prioritized tasks.
Keep answers short and clear.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
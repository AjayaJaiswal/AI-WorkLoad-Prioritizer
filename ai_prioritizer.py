import os
from openai import OpenAI

# Create client only if API key exists
client = OpenAI() if os.getenv("OPENAI_API_KEY") else None


def prioritize_tasks_with_ai(tasks):
    # Fallback if no API key is available
    if client is None:
        sorted_tasks = sorted(tasks, key=lambda task: task["score"], reverse=True)

        lines = []
        for i, task in enumerate(sorted_tasks, start=1):
            lines.append(
                f"{i}. {task['name']} - Priority score {task['score']} based on deadline, workload, difficulty, and importance."
            )

        if sorted_tasks:
            lines.append(f"Recommended first task: {sorted_tasks[0]['name']}")
            lines.append(
                "Summary: Tasks were ranked using the internal scoring system because no OpenAI API key was found."
            )

        return "\n".join(lines)

    # Clean task formatting for better AI output
    formatted_tasks = "\n".join([
        f"- {task['name']} (deadline: {task['deadline']} days, hours: {task['time']}, difficulty: {task['difficulty']}, importance: {task['weight']}, score: {task['score']})"
        for task in tasks
    ])

    prompt = f"""
You are an AI academic advisor.

Tasks:
{formatted_tasks}

Rank tasks from highest to lowest priority.

Consider:
- deadline urgency
- estimated hours needed
- difficulty
- academic importance/weight
- existing score

Return STRICTLY in this format:

1. Task Name - Reason
2. Task Name - Reason
3. Task Name - Reason

Recommended first task: Task Name
Summary: Explain in 1-2 sentences how you prioritized tasks.
Keep answers short and clear.
"""

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
        return response.output_text

    except Exception:
        # Backup fallback if API request fails
        sorted_tasks = sorted(tasks, key=lambda task: task["score"], reverse=True)

        lines = []
        for i, task in enumerate(sorted_tasks, start=1):
            lines.append(
                f"{i}. {task['name']} - Priority score {task['score']} based on deadline, workload, difficulty, and importance."
            )

        if sorted_tasks:
            lines.append(f"Recommended first task: {sorted_tasks[0]['name']}")
            lines.append(
                "Summary: AI request failed, so tasks were ranked using the internal scoring system instead."
            )

        return "\n".join(lines)
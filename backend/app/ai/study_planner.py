from app.ai.tutor import client

async def generate_study_plan(goal: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Create a concise 7-day study plan.

        Rules:
        - Day 1 to Day 7 only
        - Maximum 2 tasks per day
        - Keep each day under 2 lines
        - No explanations
        - Return only the plan

        Goal:
        {goal}
        """
    )

    return response.text
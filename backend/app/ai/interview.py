from app.ai.tutor import client

async def generate_mock_interview(domain):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Generate 10 interview questions for {domain}.

        Rules:
        - Questions only
        - No answers
        - Number the questions
        - Suitable for interview preparation
        """
    )

    return response.text
from app.ai.tutor import client

async def generate_quiz(notes: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Generate 5 multiple choice questions.

        Format:

        Q1:
        A)
        B)
        C)
        D)

        Answer:

        Notes:
        {notes}
        """
    )

    return response.text
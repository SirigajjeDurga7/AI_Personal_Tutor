from app.ai.tutor import client

async def generate_flashcards(notes: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Create 5 flashcards from these notes.

        Return format:

        Q: Question
        A: Answer

        Notes:
        {notes}
        """
    )

    return response.text
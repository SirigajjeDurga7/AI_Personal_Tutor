from app.ai.tutor import client

async def summarize_notes(notes: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Summarize the following notes in 5-8 bullet points.
        Keep it simple and student friendly.

        Notes:
        {notes}
        """
    )

    return response.text
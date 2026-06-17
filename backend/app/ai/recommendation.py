from app.ai.tutor import client

async def generate_recommendations(weak_topics):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Weak Topics:
        {weak_topics}

        Suggest:
        - Topics to revise
        - Practice areas
        - Learning recommendations

        Keep the response concise.
        """
    )

    return response.text
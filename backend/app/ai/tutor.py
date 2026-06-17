from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

async def ask_ai(question: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        You are an AI tutor.

        Answer in 3-5 concise sentences.
        Be student-friendly.
        Avoid long explanations unless explicitly requested.

        Question: {question}
        """
    )

    return response.text
from google import genai

client = genai.Client(api_key="AIzaSyCMZhpUvfskbZa5JUs1u-gmJDnUQxLbzM8")

def ask_gemini(prompt):
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )
    return response.text
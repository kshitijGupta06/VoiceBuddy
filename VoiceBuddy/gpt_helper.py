import openai

openai.api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def get_chat_response(query):
    return "Sorry, I don't know how to do that yet."

def get_chat_response(prompt):
    return "Sorry, GPT is currently unavailable due to quota limits."


def get_chat_response(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message["content"]
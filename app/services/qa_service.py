import openai

def generate_answer(app_config, context, question):
    openai.api_key = app_config['OPENAI_API_KEY']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Context: {context}\n\nQuestion: {question}\nAnswer:",
        max_tokens=150
    )
    return response.choices[0].text.strip()
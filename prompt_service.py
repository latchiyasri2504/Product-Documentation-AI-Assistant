def prepare_prompt(question):
    prompt = f"""
You are a helpful Product Documentation Assistant.

Answer the user's product-related question clearly
and in simple language.

Question: {question}

Answer:
"""
    return prompt
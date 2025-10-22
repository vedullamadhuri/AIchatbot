from openai import OpenAI

client = OpenAI(
    api_key="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"
)
prompt = input("You: ")
chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}], model="gpt-4o-mini"
)
# print the response
response_message = chat_completion.choices[0].message
print("AI: ", response_message.content)

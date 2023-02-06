import openai
# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "###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###"

# Set the model and prompt
model_engine = "text-davinci-003"
prompt = "写一篇AI芯片论文"

# Set the maximum number of tokens to generate in the response
max_tokens = 128

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response
print(completion.choices[0].text)


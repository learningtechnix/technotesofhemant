# Author: Hemant Gangwar
# Contact: learningtechnix@gmail.com
# Purpose: Accessing chatgpt chatbot from python

import openai

# Configure already captured api key
openai.api_key = "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"

# Listing details of models
#models = openai.Model.list()
#print(models)

#for model in models['data']:
#    print(model['id'])

# Generate text with GPT-3 model
# A dynamic prompt
prompt_ask = input("What do you want me to answer: ")

response = openai.Completion.create(
    engine="davinci", prompt=prompt_ask, max_tokens=100, temperature=0.2
)

# Displaying the output gathered from the query
print(response.choices[0].text)

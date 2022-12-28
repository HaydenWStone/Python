def askgpt(question):
    import openai

    # Set your API key
    openai.api_key = "api key here"

    # Create a Completion object using the GPT-3 model
    completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt=question,
    temperature = 1,
    max_tokens=1024,
    n=1,
)

    output = completion.choices[0].text

    return(str(output))
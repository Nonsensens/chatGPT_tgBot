import openai


def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature =0.6,
        max_tokens = 1500,
    )
    return response.choices[0].text


def main():
    while True:
        print('GPT: Ask me a question\n')
        myQn = input()
        askGPT(myQn)
        print('\n')



from openai import OpenAI


client = OpenAI()

response = client.responses.create(
    model = "gpt-5-nano",
    input="Bana kısa bir komik fıkra yaz?"
)

print(response.output_text)

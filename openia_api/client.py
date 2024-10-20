from app.settings import API_IA_KEY
from openai import OpenAI

client = OpenAI(api_key=API_IA_KEY)


def get_car_bio(model, brand, year):
    prompt = f"Monte uma descrição de venda do carro {model} {brand} {year} em apenas 250 caracteres."

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}]
    )

    return response

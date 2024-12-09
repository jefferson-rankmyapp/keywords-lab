from openai import OpenAI
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(prompt):

    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Você é um especialista em análise ASO e está analisando a descrição de aplicativos."},
                      {"role": "user", "content": prompt}]
        )
        #  print(response.choices[0].message)
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao chamar a API da OpenAI: {e}"

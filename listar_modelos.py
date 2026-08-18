import os
from dotenv import load_dotenv
from google import genai

# Carrega a sua chave do arquivo .env
load_dotenv()

# Inicializa o cliente com a biblioteca nova e oficial
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Consultando a API do Google... \n")
print("Modelos disponíveis para a sua chave:")
print("-" * 40)

# Faz um loop na lista de modelos e imprime o nome de cada um
try:
    for model in client.models.list():
        print(model.name)
except Exception as e:
    print(f"Erro ao consultar modelos: {e}")
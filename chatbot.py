import openai
#COLOQUE A CHAVE DA API QUE VOCE PEGOU NO OPENAI.COM
chave_api = "SUA CHAVE API"
#SE DER ERRO NA HORA DE RODAR POSSIVELMENTE VOCE ESTA SEM CREDITOS NO SITE

openai.api_key = chave_api

def enviarmensagem(mensagem, lista_mensagens = []):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = lista_mensagens,
        
    )

    return resposta["choices"][0]["message"]["content"]

while True:
    texto = input("escreva aqui sua mensagem:")

    if texto == "sair":
        break
    else:
        resposta = enviarmensagem(texto)
        print("chatbot:", resposta["content"])


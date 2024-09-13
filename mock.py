import random
mock_chat_responses = [
    "Claro que a Terra é plana, senão as pessoas do outro lado cairiam, né?",
    "Se você não vê algo, então não existe. Simples assim!",
    "Por que estudar matemática? Eu nunca vou precisar de um triângulo na minha vida!",
    "Clima global? É só abrir a janela e checar. Tá frio ou calor, pronto!",
    "Café é só uma sopa de feijão, não entendo o hype.",
    "Internet é só uma moda passageira, logo a gente volta a usar cartas.",
    "Pra que vacina? Só comer mais laranja que resolve tudo!",
    "Computadores nunca vão ser mais rápidos que um humano. Eu já vi o Usain Bolt!",
    "Leis da física? Eu já quebrei várias delas jogando videogame.",
    "Se você quiser evitar vírus no computador, é só nunca usar a internet!"
]

mock_audio_responses = [
    "output.mp3",
    "output2.mp3",
    "output3.mp3",
]

def chat_with_gpt(prompt):
    # Simula um pequeno atraso para parecer mais realista
    import time
    time.sleep(0.5)
    
    # Retorna uma resposta aleatória da lista de respostas mockadas
    return random.choice(mock_chat_responses)

def generate_audio(TEXT_TO_SPEAK):
    return random.choice(mock_audio_responses)
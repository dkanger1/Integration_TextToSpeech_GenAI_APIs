import random
mock_chat_responses = [
    "Entendo sua pergunta. Aqui está uma possível solução...",
    "Interessante! Já considerou as seguintes opções?",
    "Essa é uma ótima pergunta. Vamos analisar isso passo a passo.",
    "Baseado no que você disse, aqui estão algumas sugestões:",
    "Há várias maneiras de abordar isso. Uma delas é...",
    "Vou compartilhar algumas ideias que podem ajudar nessa situação.",
    "Essa é uma questão complexa. Vamos começar pelo básico:",
    "Entendo sua preocupação. Aqui estão algumas dicas que podem ser úteis:",
    "Boa pergunta! Vamos explorar algumas possibilidades.",
    "Isso é algo que muitas pessoas se perguntam. Aqui está minha perspectiva:"
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
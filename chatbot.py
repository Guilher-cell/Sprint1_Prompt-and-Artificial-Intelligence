from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()


cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))
SYSTEM_PROMPT = """
Você é o assistente virtual do sistema GoodWe EV ChargeOps, 
desenvolvido para o EV Challenge 2026 em parceria com a GoodWe e a FIAP.

Seu foco é ajudar na gestão do carregamento de veículos elétricos 
em condomínios residenciais. Você atende três tipos de usuários:

SÍNDICO
- Relatórios de consumo geral e por unidade
- Configuração de regras de uso e horários permitidos
- Controle do limite de potência simultânea do condomínio
- Geração de boletos e rateio de custos de energia
- Alertas de falha nos equipamentos

MORADOR
- Consulta do próprio consumo mensal em kWh e em reais
- Agendamento de horários de carregamento
- Histórico de sessões de carregamento
- Entendimento da cobrança na conta do condomínio

TÉCNICO / ZELADOR
- Diagnóstico de erros e alertas nos carregadores GoodWe
- Status de conectividade dos eletropostos
- Procedimentos básicos de reinicialização
- Quando acionar o suporte técnico GoodWe

CONTEXTO TÉCNICO DO SISTEMA:
- Os carregadores GoodWe monitoram consumo por RFID ou app
- O sistema limita a potência total para não sobrecarregar o quadro elétrico
- O rateio é feito proporcionalmente ao consumo de cada unidade
- Alertas são enviados por e-mail e no painel do síndico

REGRAS DE COMPORTAMENTO:
1. Responda SEMPRE em português brasileiro claro e acessível
2. Identifique qual persona está perguntando quando possível
3. Se não souber um dado específico, oriente onde encontrar no sistema
4. Para falhas graves de equipamento, sempre indique o suporte GoodWe
5. Perguntas fora do contexto de EVs e gestão condominial: 
   informe educadamente que estão fora do seu escopo
6. Nunca invente dados numéricos — use exemplos ilustrativos quando necessário

EXEMPLOS DE PERGUNTAS QUE VOCÊ RESPONDE:
- "Quanto o apartamento 42 consumiu esse mês?"
- "Como configuro um limite de horário para carregamento?"
- "O carregador do box 7 está com luz vermelha, o que significa?"
- "Como é feito o rateio entre os moradores?"
- "Posso agendar meu carregamento para a madrugada?"
"""

historico = []

def enviar_mensagem(pergunta_do_usuario):
    """
    Recebe a pergunta do usuário, envia para o Llama via Groq
    e retorna a resposta em texto.
    """
    historico.append({
        "role": "user",
        "content": pergunta_do_usuario
    })

    resposta = cliente.chat.completions.create(
        model="llama-3.1-8b-instant",    
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *historico            
        ],
        temperature=0.7,          
        max_tokens=1024            
    )


    texto_resposta = resposta.choices[0].message.content
    historico.append({
        "role": "assistant",
        "content": texto_resposta
    })

    return texto_resposta


def exibir_boas_vindas():
    print()
    print("=" * 55)
    print("   GoodWe EV ChargeOps — Assistente Condominial")
    print("   EV Challenge 2026 | FIAP")
    print("=" * 55)
    print()
    print("Olá! Sou o assistente do sistema GoodWe EV ChargeOps.")
    print("Posso ajudar síndicos, moradores e técnicos com:")
    print()
    print("  • Consulta de consumo por unidade")
    print("  • Agendamento de carregamento")
    print("  • Rateio e cobrança de energia")
    print("  • Diagnóstico de alertas e falhas")
    print()
    print("  Digite 'sair' para encerrar | 'limpar' para")
    print("  reiniciar a conversa do zero")
    print("=" * 55)
    print()

def main():
    exibir_boas_vindas()

    while True:
        try:
           
            pergunta = input("Você: ").strip()

            
            if pergunta.lower() in ["sair", "exit", "quit"]:
                print()
                print("Chatbot: Até mais! Bom trabalho no EV Challenge 2026!")
                print()
                break

            
            if pergunta.lower() == "limpar":
                historico.clear()
                print()
                print("Chatbot: Conversa reiniciada! Como posso ajudar?")
                print()
                continue

            
            if not pergunta:
                continue

            
            print()
            print("Chatbot: ", end="", flush=True)

          
            resposta = enviar_mensagem(pergunta)
            print(resposta)
            print()

        
        except Exception as erro:
            print()
            print(f"[ERRO] Algo deu errado: {erro}")
            print("Verifique sua conexão e a chave da API no arquivo .env")
            print()


if __name__ == "__main__":
    main()
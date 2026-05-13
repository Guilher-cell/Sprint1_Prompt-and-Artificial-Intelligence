from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Você é o assistente virtual do sistema GoodWe EV ChargeOps, 
desenvolvido para o EV Challenge 2026 em parceria com a GoodWe e a FIAP.
Foco: gestão de carregamento de veículos elétricos em condomínios residenciais.
Responda sempre em português brasileiro claro e objetivo.
"""

TESTES = [
    {
        "numero": 1,
        "persona": "Morador",
        "pergunta": "Quanto meu apartamento consumiu de energia no carregamento este mês?",
        "resposta_esperada": (
            "Deve informar que o consumo individual fica disponível no painel do morador, "
            "mostrar como acessar (app ou portal), e explicar que o valor é calculado "
            "em kWh multiplicado pela tarifa do condomínio."
        )
    },
    {
        "numero": 2,
        "persona": "Morador",
        "pergunta": "Como faço para agendar o carregamento do meu carro para a madrugada?",
        "resposta_esperada": (
            "Deve explicar o passo a passo de agendamento pelo app ou portal GoodWe, "
            "mencionar que o horário da madrugada pode ter tarifa mais baixa, "
            "e informar como cancelar ou alterar o agendamento."
        )
    },
    {
        "numero": 3,
        "persona": "Técnico / Zelador",
        "pergunta": "O carregador do box 7 está com a luz vermelha piscando. O que significa?",
        "resposta_esperada": (
            "Deve descrever que luz vermelha piscando indica erro de comunicação ou falha elétrica, "
            "orientar a reinicialização básica do equipamento, "
            "e indicar quando acionar o suporte técnico GoodWe."
        )
    },
    {
        "numero": 4,
        "persona": "Síndico",
        "pergunta": "Como é feito o rateio do custo de energia entre os moradores que usaram o carregador?",
        "resposta_esperada": (
            "Deve explicar que o rateio é proporcional ao consumo em kWh de cada unidade, "
            "que o sistema gera relatório mensal automático, "
            "e que o síndico pode configurar a tarifa base no painel administrativo."
        )
    },
    {
        "numero": 5,
        "persona": "Síndico",
        "pergunta": "Posso limitar quantos carros carregam ao mesmo tempo para não sobrecarregar a rede elétrica?",
        "resposta_esperada": (
            "Deve explicar o conceito de orquestração de carga (load balancing), "
            "como configurar o limite de potência simultânea no painel do síndico, "
            "e que o sistema redistribui automaticamente a potência disponível entre os carregadores ativos."
        )
    },
]

def rodar_teste(teste):
    print(f"\n{'='*55}")
    print(f"TESTE {teste['numero']} — Persona: {teste['persona']}")
    print(f"{'='*55}")
    print(f"Pergunta : {teste['pergunta']}")
    print(f"\nResposta esperada (critério):")
    print(f"  {teste['resposta_esperada']}")
    resposta = cliente.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": teste["pergunta"]}
        ],
        temperature=0.6,
        max_tokens=512
    )
    texto = resposta.choices[0].message.content
    print(f"\nResposta do chatbot:")
    print(f"  {texto}")
    print(f"\n[Avalie manualmente se a resposta atende ao critério acima]")

def main():
    print()
    print("=" * 55)
    print("  Modelo de Testes — GoodWe EV ChargeOps")
    print("  Sprint 1 | EV Challenge 2026 | FIAP")
    print("=" * 55)

    for teste in TESTES:
        rodar_teste(teste)
        input("\n  Pressione Enter para o próximo teste...")

    print()
    print("=" * 55)
    print("  Todos os testes concluídos!")
    print("=" * 55)
    print()


if __name__ == "__main__":
    main()

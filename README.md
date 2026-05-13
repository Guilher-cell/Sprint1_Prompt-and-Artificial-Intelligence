# Sprint1_Prompt-and-Artificial-Intelligence
Esse foi um trabalho educacional com o foco do entendimento de um chatbot, realizado pelo grupo:

André Fujinaga - RM569158 ||
Arthur Machado - RM569919 ||
Conrado Gracie - RM569157 ||
Guilherme Belo - RM570079 ||
Renato Sandreschi - RM569156 ||

faculdade de informática e administração paulista (FIAP).

Para executar esse projeto execute em seu terminal pip install groq python-dotenv.

Configure seu ambiente .env 

GROQ_API_KEY=gsk_coloque_sua_chave_aqui.

python chatbot.py

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

O Problema:
O crescimento acelerado dos veículos elétricos no Brasil trouxe um desafio concreto para condomínios residenciais: como gerenciar o carregamento compartilhado de forma justa, segura e automatizada?

Na ausência de uma solução integrada, os condomínios enfrentam diariamente os seguintes problemas:

Sobrecarga elétrica: vários moradores carregando simultaneamente podem ultrapassar o limite do quadro elétrico geral, causando quedas de energia.
Falta de rastreabilidade: sem registro individual de consumo, é impossível saber quem usou quanto de energia.
Rateio manual: o síndico precisa calcular manualmente a divisão do custo de energia entre os moradores que utilizaram os carregadores.
Ausência de agendamento: sem controle de horários, o uso é caótico e desequilibrado — quem chega primeiro carrega, independentemente da necessidade.
Falhas sem notificação: equipamentos com defeito ficam fora de serviço por longos períodos por falta de monitoramento.

Nossa Solução
Desenvolvemos um chatbot com Inteligência Artificial integrado ao contexto do sistema GoodWe EV ChargeOps, capaz de atender de forma autônoma e contextualizada as principais demandas operacionais do dia a dia condominial.
O assistente atua como interface inteligente entre os usuários (síndico, morador, técnico) e o sistema de gerenciamento dos eletropostos, respondendo perguntas, orientando procedimentos e auxiliando na tomada de decisão — tudo em linguagem natural, sem necessidade de treinamento técnico.

O que o chatbot resolve na prática:

O chatbot ajuda em diferentes situações relacionadas ao uso e gerenciamento do sistema de recarga de veículos elétricos no condomínio. Quando o síndico não sabe quanto cada morador consumiu, o chatbot orienta como acessar e interpretar relatórios de consumo por unidade. Caso o morador não saiba como agendar o carregamento, o sistema explica o passo a passo do agendamento pelo app ou portal. Se o zelador não entende o código de erro apresentado no equipamento, o chatbot descreve o significado dos alertas e orienta a reinicialização. Quando o síndico não sabe como configurar o limite de potência, o chatbot explica o conceito de orquestração de carga e como realizar a configuração. Além disso, quando o morador não entende a cobrança na conta do condomínio, o sistema detalha o cálculo de rateio proporcional ao consumo individual.

Personas Atendidas
O chatbot foi projetado para atender três personas distintas dentro do ambiente condominial:
Síndico — Gestão e Controle
Responsável pela administração geral do condomínio. Precisa de visão macro: relatórios consolidados, configuração de regras de uso, controle de custos e garantia de que a rede elétrica não será sobrecarregada.
Perguntas típicas:

"Como vejo o consumo total de energia dos carregadores este mês?"
"Como configuro o horário permitido para carregamento?"
"Como gero o relatório para cobrar cada apartamento?"
"Posso limitar quantos carros carregam ao mesmo tempo?"


Morador — Uso Pessoal
Usuário final do carregador. Quer informações sobre seu próprio consumo, agendamentos e entendimento da cobrança. Não possui conhecimento técnico e precisa de respostas simples e diretas.
Perguntas típicas:

"Quanto meu apartamento consumiu esse mês?"
"Como agendar o carregamento para a madrugada?"
"Como vejo o histórico das minhas sessões de carregamento?"
"Por que esse valor apareceu na minha conta?"


Técnico / Zelador — Manutenção
Responsável pela operação física dos equipamentos. Precisa de diagnósticos rápidos, procedimentos de reinicialização e orientações claras sobre quando acionar o suporte técnico especializado.
Perguntas típicas:

"O carregador do box 7 está com luz vermelha piscando. O que significa?"
"Como reinicio o equipamento corretamente?"
"O carregador não está reconhecendo o cartão RFID. O que faço?"
"Quando devo acionar o suporte técnico da GoodWe?"

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tecnologias Escolhidas e Justificativa:
Modelo de IA: Meta Llama 3 (via Groq)
O que é o Llama?
O Llama (Large Language Model Meta AI) é uma família de modelos de linguagem de grande escala desenvolvida pela Meta (Facebook). Diferentemente de modelos como o ChatGPT (OpenAI) ou Gemini (Google), o Llama é open source — seu código e pesos são disponibilizados publicamente, permitindo uso gratuito, customização e integração em projetos acadêmicos e comerciais sem custos de licença.

Por que escolhemos o Llama?

O modelo Llama 3 foi escolhido para o projeto devido a diferentes fatores que atendem às necessidades do desenvolvimento do sistema. Um dos principais critérios é o fato de ser gratuito, já que, por ser open source, não há custo de licença relacionado ao modelo em si. Além disso, o Llama 3 apresenta alta qualidade, competindo diretamente com modelos proprietários em benchmarks de linguagem natural.

Outro ponto importante é o contexto do projeto e sua flexibilidade é um diferencial, já que pode ser executado localmente ou utilizado via API, facilitando futuras evoluções e integrações do sistema.

Plataforma de Inferência: Groq
O que é o Groq?
O Groq é uma empresa americana que desenvolveu um chip de processamento dedicado exclusivamente para inferência de modelos de linguagem, chamado LPU (Language Processing Unit). Diferente de GPUs convencionais, o LPU foi projetado do zero para processar texto gerado por LLMs com velocidade e eficiência máximas.

O Groq oferece uma API gratuita (GroqCloud) que permite rodar modelos open source — incluindo o Llama — sem precisar de hardware próprio.

Por que escolhemos o Groq?

O Groq foi escolhido como plataforma de execução do modelo devido às suas vantagens em desempenho e facilidade de utilização. Um dos principais critérios é a velocidade, já que o Groq pode ser até 10 vezes mais rápido que GPUs convencionais para inferência de modelos de linguagem. Além disso, o serviço oferece um plano gratuito, sendo suficiente para desenvolvimento e testes durante o projeto.

Bibliotecas Utilizadas
  No desenvolvimento do projeto, foram utilizadas bibliotecas específicas para facilitar a integração e aumentar a segurança da aplicação. A biblioteca groq foi utilizada como cliente oficial da API Groq, permitindo uma comunicação direta e simplificada com o modelo Llama. Já a biblioteca python-dotenv foi utilizada para o gerenciamento de variáveis de ambiente, protegendo a chave da API ao mantê-la armazenada no arquivo .env, evitando que informações sensíveis sejam enviadas para o GitHub.

Fluxo de Funcionamento
O diagrama abaixo representa o ciclo completo de uma interação com o chatbot:

<img width="452" height="750" alt="image" src="https://github.com/user-attachments/assets/ce3b76c2-bdf8-43a6-a318-2ee63178b533" />



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
System Prompt Base
O system prompt é o texto enviado ao modelo antes de qualquer pergunta do usuário. Ele define a personalidade, o escopo, as regras de comportamento e o contexto técnico do chatbot. É o elemento mais importante do projeto quanto mais preciso, melhor a qualidade das respostas.

"Você é o assistente virtual do sistema GoodWe EV ChargeOps, 
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
6. Nunca invente dados numéricos — use exemplos ilustrativos quando necessário"
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Modelo de Testes
O modelo de testes define as 5 perguntas esperadas e o critério de avaliação da resposta ideal para cada uma. Este modelo será a base da avaliação na Sprint 2.

Teste 1 — Consulta de consumo (Persona: Morador)
Pergunta:

"Quanto meu apartamento consumiu de energia no carregamento este mês?"

Critério de resposta ideal:
A resposta deve informar que o consumo individual fica disponível no painel do morador (app ou portal GoodWe), explicar que o valor é medido em kWh e convertido para reais com base na tarifa configurada pelo síndico, e orientar como acessar esse relatório.
O que avalia:
Capacidade do chatbot de orientar o morador sem inventar dados numéricos específicos, direcionando para a fonte correta de informação.

Teste 2 — Agendamento de carregamento (Persona: Morador)
Pergunta:

"Como faço para agendar o carregamento do meu carro para a madrugada?"

Critério de resposta ideal:
A resposta deve explicar o passo a passo de agendamento pelo app ou portal GoodWe, mencionar que horários de menor demanda (como madrugada) podem ter prioridade ou tarifa reduzida, e informar como cancelar ou alterar um agendamento existente.
O que avalia:
Capacidade de guiar o morador em um processo operacional com instruções claras e sequenciais.

Teste 3 — Diagnóstico de falha (Persona: Técnico / Zelador)
Pergunta:

"O carregador do box 7 está com a luz vermelha piscando. O que significa?"

Critério de resposta ideal:
A resposta deve descrever que luz vermelha piscando indica erro de comunicação ou falha elétrica no equipamento GoodWe, orientar o procedimento básico de reinicialização (desligar e religar o disjuntor específico), e indicar claramente quando o suporte técnico GoodWe deve ser acionado.
O que avalia:
Capacidade do chatbot de fornecer diagnóstico técnico útil sem inventar informações e sem substituir o suporte especializado.

Teste 4 — Rateio de custos (Persona: Síndico)
Pergunta:

"Como é feito o rateio do custo de energia entre os moradores que usaram o carregador?"

Critério de resposta ideal:
A resposta deve explicar que o rateio é proporcional ao consumo registrado em kWh por cada unidade, que o sistema GoodWe EV ChargeOps gera relatório mensal automático com o consumo individual, e que o síndico pode configurar a tarifa base (R$/kWh) no painel administrativo para que o valor em reais seja calculado automaticamente.
O que avalia:
Capacidade do chatbot de explicar um conceito financeiro-operacional de forma clara para o síndico, sem simplificar demais nem usar termos excessivamente técnicos.

Teste 5 — Orquestração de carga (Persona: Síndico)
Pergunta:

"Posso limitar quantos carros carregam ao mesmo tempo para não sobrecarregar a rede elétrica?"

Critério de resposta ideal:
A resposta deve explicar o conceito de orquestração de carga (load balancing), informar que o sistema GoodWe permite configurar um limite de potência simultânea no painel administrativo do síndico, e descrever que o sistema redistribui automaticamente a potência disponível entre os carregadores ativos, priorizando conforme regras pré-definidas.
O que avalia:
Capacidade do chatbot de explicar um conceito técnico avançado (orquestração de potência) de forma acessível para um síndico sem formação técnica.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Conclusão:

A Sprint 1 estabeleceu as bases sólidas do GoodWe EV ChargeOps Chatbot, demonstrando que a combinação entre um system prompt bem estruturado, um modelo de linguagem de alta performance (Llama 3 via Groq) e um escopo condominial bem definido é suficiente para construir uma ferramenta operacional real — não apenas uma demonstração genérica de IA.
O maior aprendizado desta etapa foi entender que a qualidade do chatbot não depende apenas do modelo escolhido, mas principalmente do contexto que é fornecido a ele. Um system prompt preciso, com personas bem definidas, regras claras de comportamento e contexto técnico relevante, transforma um modelo genérico em um assistente especializado e confiável.
Com o modelo de testes definido e o código funcional, o grupo está preparado para a Sprint 2, onde as respostas serão avaliadas com métricas objetivas e a solução evoluirá para uma interface mais acessível ao usuário final.

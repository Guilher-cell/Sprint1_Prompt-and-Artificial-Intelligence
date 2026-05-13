# Sprint1_Prompt-and-Artificial-Intelligence
Esse foi um trabalho educacional com o foco do entendimento de um chatbot, realizado pelo grupo:

André Fujinaga - RM569158
Arthur Machado - RM569919
Conrado Gracie - RM569157
Guilherme Belo - RM570079
Renato Sandreschi - RM569156

faculdade de informática e administração paulista (FIAP).

Para executar esse projeto execute em seu terminal pip install groq dotenv.

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


Tecnologias Escolhidas e Justificativa:
Modelo de IA: Meta Llama 3 (via Groq)
O que é o Llama?
O Llama (Large Language Model Meta AI) é uma família de modelos de linguagem de grande escala desenvolvida pela Meta (Facebook). Diferentemente de modelos como o ChatGPT (OpenAI) ou Gemini (Google), o Llama é open source — seu código e pesos são disponibilizados publicamente, permitindo uso gratuito, customização e integração em projetos acadêmicos e comerciais sem custos de licença.

Por que escolhemos o Llama?

O modelo Llama 3 foi escolhido para o projeto devido a diferentes fatores que atendem às necessidades do desenvolvimento do sistema. Um dos principais critérios é o fato de ser gratuito, já que, por ser open source, não há custo de licença relacionado ao modelo em si. Além disso, o Llama 3 apresenta alta qualidade, competindo diretamente com modelos proprietários em benchmarks de linguagem natural.

Outro ponto importante é o contexto do projeto e sua flexibilidade é um diferencial, já que pode ser executado localmente ou utilizado via API, facilitando futuras evoluções e integrações do sistema.

⚡ Plataforma de Inferência: Groq
O que é o Groq?
O Groq é uma empresa americana que desenvolveu um chip de processamento dedicado exclusivamente para inferência de modelos de linguagem, chamado LPU (Language Processing Unit). Diferente de GPUs convencionais, o LPU foi projetado do zero para processar texto gerado por LLMs com velocidade e eficiência máximas.

O Groq oferece uma API gratuita (GroqCloud) que permite rodar modelos open source — incluindo o Llama — sem precisar de hardware próprio.

Por que escolhemos o Groq?

O Groq foi escolhido como plataforma de execução do modelo devido às suas vantagens em desempenho e facilidade de utilização. Um dos principais critérios é a velocidade, já que o Groq pode ser até 10 vezes mais rápido que GPUs convencionais para inferência de modelos de linguagem. Além disso, o serviço oferece um plano gratuito, sendo suficiente para desenvolvimento e testes durante o projeto.


📦 Bibliotecas Utilizadas
  No desenvolvimento do projeto, foram utilizadas bibliotecas específicas para facilitar a integração e aumentar a segurança da aplicação. A biblioteca groq foi utilizada como cliente oficial da API Groq, permitindo uma comunicação direta e simplificada com o modelo Llama. Já a biblioteca python-dotenv foi utilizada para o gerenciamento de variáveis de ambiente, protegendo a chave da API ao mantê-la armazenada no arquivo .env, evitando que informações sensíveis sejam enviadas para o GitHub.

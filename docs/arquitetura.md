# Arquitetura do Bac Bo Bot

## Objetivo
Criar um sistema modular para:
- armazenar histórico de resultados
- calcular estatísticas de sequências
- aplicar estratégias
- gerar sinais com pontuação
- gerenciar risco

## Estrutura de Módulos
- core/estado.py → mantém o estado do bot
- core/dados.py → valida entrada de resultados
- core/estatisticas.py → calcula frequências e padrões
- core/estrategias.py → aplica regras de leitura de padrões
- core/decisao.py → motor de pontuação
- core/risco.py → gerencia limite de perdas e lucros

## Fluxo do Sistema
1. Receber resultado
2. Atualizar estado
3. Calcular estatísticas
4. Rodar estratégias
5. Gerar score
6. Validar risco
7. Registrar logs

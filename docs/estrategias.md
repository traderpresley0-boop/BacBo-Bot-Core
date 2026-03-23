# Estratégias de Análise do Bac Bo

Este documento descreve os padrões iniciais que o bot deve identificar. Cada estratégia recebe um nome e uma descrição clara, permitindo fácil implementação e pontuação futura.

---

## 1. Rachas
Sequências consecutivas de resultados iguais.

### 1.1 Racha Curta
- Sequência de 2 resultados iguais.  
- Exemplo: P P ou B B

### 1.2 Racha Média
- Sequência de 3 resultados iguais.  
- Exemplo: P P P ou B B B

### 1.3 Racha Longa
- Sequência de 4 ou mais resultados iguais.  
- Exemplo: P P P P ou B B B B

---

## 2. Alternâncias
Padrões de resultados que se alternam.

### 2.1 Alternância Simples
- Padrão de 2 alternâncias (ex: P B ou B P)

### 2.2 Alternância Dupla
- Padrão de 4 alternâncias (ex: P B P B ou B P B P)

### 2.3 Alternância Tripla
- Padrão de 6 alternâncias (ex: P B P B P B)

---

## 3. Padrões de Sequência
Mais complexos, combinando rachas e alternâncias.

### 3.1 Racha + Alternância
- Um racha seguido de alternância.  
- Exemplo: P P B P B

### 3.2 Alternância + Racha
- Alternância seguida de um racha.  
- Exemplo: P B P B B B

### 3.3 Zig-Zag
- Pequenas sequências que mudam constantemente.  
- Exemplo: P B B P P B

---

## 4. Estratégias de Frequência
Análise de probabilidades e tendência histórica.

### 4.1 Predomínio de Player/Banker
- Detecta se um lado está aparecendo mais que o outro em N rodadas.  
- Exemplo: Player apareceu 60% nas últimas 20 rodadas

### 4.2 Concentração de Sequências
- Identifica quando rachas ou alternâncias ocorrem com frequência acima da média histórica.

---

## 5. Observações
- Cada estratégia deve ser **medida e validada com dados históricos** antes de ser usada para gerar sinais.  
- No futuro, cada padrão terá **peso na pontuação final** para decisão do bot.

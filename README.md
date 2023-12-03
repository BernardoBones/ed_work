**ABORDAGEM UTILIZADA**
- Consiste de um fluxo principal que fica em loop até o usuário desejar sair
- Escolhe se o input se dará por uma expressão/variável informada pelo usuário no terminal ou se será a partir de um arquivo de texto
  
**- Caso seja pelo terminal:**
     - Será identificado 3 possibilidades na função bot_expressao:
       - Atribuição de variável
       - Printar o valor da variável (auto-explicativo)
       - Expressão
**- Caso seja por arquivo:**
     - Será chamada a função bot-arquivo para leitura do arquivo
     - Para cada linha lida, será chamada a função bot_expressao, identificando as mesmas 3 possibilidades:

**TOKENIZAÇÃO DA EXPRESSÃO**
  - Recebe uma string (expressão)
  - Valida se há caracteres inválidos, caso não tenha, mapeia os caracteres da string em um vetor
  - Substitui possíveis variáveis (dict de variáveis global) pelos seus respectivos valores
  - Adiciona parenteses na expressão de acordo com as precedências das subexpressões, para serem interpretados como prioridade posteriormente

ATRIBUIÇÃO DE VARIÁVEL
  - Caso variável seja apenas um valor, salva key(variável) e value(valor) no dicionário global **variaveis**
  - Caso seja uma expressão, monta a árvore da expressão e salva o resultado da expressão como o valor da variável

EXPRESSÃO
  - Tokeniza a expressão
  - Cria árvore recursivamente a partir dos tokens
    - Valor do nodo é um operador, e os filhos os números ou subexpressões
  - Avalia a árvore, retornando o resultado
    - Percorre a árvore recursivamente, calculando as subarvores caso existam e retornando o resultado final
  - Printa o resultado
  - Caso a função não esteja sendo executado a partir da leitura de um arquivo texto e nem da interface, pergunta a o usuário se o mesmo deseja visualizar a árvore da expressão
      - Caso sim, printa a árvore, percorrendo-a recursivamente e printando o valor do nodo e seus filhos

EXECUÇÃO COM INTERFACE GRÁFICA
  - Executa apenas expressões, não lê/armazena variáveis, nem trabalha com arquivos
  - Input se dá pelo usuário informar a expressão
  - Exibe a resposta na interface

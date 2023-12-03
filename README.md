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


**DESAFIOS ENCONTRADOS**
- Primeiro ponto foi como tratar a string a fim de separar seus elementos de forma que a árvore pudesse ser montada corretamente
  - Tentamos "fazer no braço" essa tratativa, porém percebemos que estávamos evoluindo para algo muito complexo em que cada caso de teste, o algorítmo só aumentava de tamanho, então buscamos como alternativa, o RegEx
    - Filtrando os elementos da string a partir de um padrão, e ao mesmo tempo validando o os caracteres formadores da expressão
- Segundo ponto de dificuldade foi de que forma montaríamos a árvore, já visando que teríamos que percorre-la para realizar os cálculos, ou seja, a criação teria que ser até mais eficiente que a pesquisa
  - Sofremos no começo até entender de que forma trabalharíamos com os operadores como valores principais dos nodos, criação e realocação de nodos...
    - Também vale ressaltar que demoramos a entender como tratar a precedência dos () e operadores da melhor forma, optamos por criar algo de certa forma padronizado, que é feito já ao filtrar os elementos da string, abstraindo esse algortimo da criaçãpo da árvore
      - A ideia foi que a Classe árvore apenas criasse e avaliasse a árvore, sem a necessidade de realizar algum tratamento dos dados recebidos - tokenização largando mastigado para o resto do código
- Discutimos também como trabalharíamos com as variáveis, optamos por um dicionário "global", em que a inserção e atualização de valores pudesse se dar da forma mais dinâmica possível
- Outra dificuldade perceptível foi a interface, 'apanhamos' da biblioteca bastante, decidimos deixar apenas para expressões simples, informadas pelo usuário e sem uso de variáveis, para que funcionasse 100% o que a interface apresenta ao usuário, sem risco de bugs e exceções inesperadas ao executar
- Por fim, ponto que foi de bastante aprendizado é a organização do código. Mexemos, apagamos e criamos vários arquivos e funções, visando modularizar as partes do projeto, para que o mesmo fosse mais fácil de trabalhar e também mais fácil de ser entendido.

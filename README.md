# Gerador de Relatório em PDF com Pandas e ReportLab

Este projeto tem como objetivo criar um relatório automatizado em formato PDF utilizando os dados de um arquivo tabular processado com a biblioteca **Pandas** e gerando a saída visual com a biblioteca **ReportLab**. 

### **Objetivos Principais:**
1. **Leitura de Dados:**
   - Carregar um arquivo CSV contendo informações de alunos, como nome, curso e notas em diferentes disciplinas.
2. **Processamento de Dados:**
   - Manipular os dados para realizar filtragens ou cálculos, como médias de notas ou ordenação por critérios específicos.
3. **Geração de Relatório PDF:**
   - Gerar um documento PDF estilizado que apresenta as informações do DataFrame em formato de tabela, adicionando títulos, margens e organização visual.

### **Funcionalidades:**
- **Leitura de Arquivo CSV:** O projeto permite a importação de arquivos CSV com delimitadores específicos (ex.: ponto e vírgula).
- **Iteração com Pandas:** Utiliza o método `iterrows()` para iterar sobre as linhas do DataFrame e organizar as informações de cada aluno.
- **Personalização de Relatório:** O layout do PDF pode ser adaptado, com títulos, margens ajustadas e espaçamento entre os elementos.
- **Exportação Automática:** O arquivo gerado é salvo automaticamente na mesma pasta do projeto, com o nome especificado pelo usuário.

### **Ferramentas Utilizadas:**
1. **Pandas:** Para a manipulação e análise dos dados do arquivo CSV.
2. **ReportLab:** Para a criação e estilização do documento PDF.
3. **Python:** Como linguagem de programação principal para integrar as funcionalidades.

### **Exemplo de Aplicação:**
Imagine um sistema de gestão acadêmica que precisa gerar boletins de alunos ou relatórios consolidados de desempenho. Este projeto serve como base para automatizar essa tarefa, transformando dados brutos em um documento formatado e pronto para impressão ou envio.

### **Estrutura do Código:**
1. Importação das bibliotecas e leitura do arquivo CSV.
2. Manipulação dos dados no DataFrame (opcional: filtros, cálculos, etc.).
3. Configuração do layout do PDF com margens, títulos e organização.
4. Iteração pelos dados e escrita de informações no documento.
5. Exportação do PDF final para o diretório do projeto.

Este projeto pode ser expandido para incluir gráficos, tabelas formatadas ou integração com interfaces gráficas para facilitar o uso por usuários não técnicos.
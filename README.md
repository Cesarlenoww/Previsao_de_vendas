Previsão de Vendas com Regressão Linear
Este projeto utiliza machine learning para prever vendas mensais com base no orçamento de marketing e no mês do ano. Utilizamos regressão linear para criar o modelo, e o conjunto de dados fictício simula o comportamento de vendas ao longo de 12 meses.

Tecnologias Utilizadas
Python: Linguagem de programação usada para implementar o projeto.
Pandas: Biblioteca para manipulação e análise de dados.
Numpy: Biblioteca para computação numérica.
Matplotlib: Utilizada para visualização gráfica dos resultados.
Scikit-learn: Biblioteca de machine learning usada para criar o modelo de regressão linear.
Funcionalidades
Treinamento de Modelo: O modelo de regressão linear é treinado com base em um conjunto de dados contendo o mês e o orçamento de marketing.
Previsão de Vendas: Após o treinamento, o modelo realiza previsões com base nos dados de teste.
Visualização Gráfica: Os resultados das previsões são visualizados em um gráfico que compara os valores reais com as previsões.
Como Executar o Projeto
Clone este repositório:
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git

Instale as dependências necessárias:
Copiar código
pip install pandas numpy matplotlib scikit-learn

Execute o script Python:
Copiar código
python previsao_vendas.py
Explicação do Código
Carregamento e Preprocessamento de Dados:

Os dados de vendas e orçamento de marketing são carregados em um DataFrame do Pandas.
As variáveis Mês e Orçamento de Marketing são usadas como variáveis preditoras, e Vendas como a variável alvo.
Treinamento do Modelo:

Utilizamos a função train_test_split para dividir o conjunto de dados em treino e teste.
O modelo de regressão linear é treinado com os dados de treino.
Previsões e Visualização:

O modelo faz previsões sobre os dados de teste.
Um gráfico de dispersão é gerado para visualizar as previsões comparadas com os dados reais.
Resultados
O gráfico gerado mostra a precisão do modelo, com os pontos reais e as previsões plotados para uma fácil interpretação.
Melhorias Futuras
Incluir mais variáveis para melhorar a precisão do modelo.
Explorar outros algoritmos de machine learning para comparação de desempenho.
Utilizar um conjunto de dados real de vendas.

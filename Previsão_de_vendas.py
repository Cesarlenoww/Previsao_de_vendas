import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carregar os Dados
# Para o exemplo, você pode usar um conjunto de dados fictício. Em um caso real, você carregaria dados históricos de vendas.
# Exemplo de um DataFrame fictício:
data = {
    'Mês': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'Vendas': [200, 220, 250, 275, 300, 320, 350, 370, 400, 420, 450, 480],
    'Orçamento de Marketing': [50, 55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
}
df = pd.DataFrame(data)

# 2. Preprocessamento dos Dados
# Adicionar variáveis de tempo, como mês e ano, se necessário
df['Mês'] = df['Mês'].dt.month
X = df[['Mês', 'Orçamento de Marketing']]
y = df['Vendas']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 3. Treinamento do Modelo
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Previsões
y_pred = model.predict(X_test)

# Ordenar os dados de teste para que a linha de previsão seja exibida corretamente
X_test_sorted = X_test.sort_values(by='Mês')
y_pred_sorted = model.predict(X_test_sorted)

# Visualizando os resultados com um gráfico
plt.figure(figsize=(10, 6))
plt.scatter(X_test['Mês'], y_test, color='black', label='Dados Reais')  # Pontos reais
plt.scatter(X_test['Mês'], y_pred, color='red', label='Previsões')  # Previsões do modelo
plt.plot(X_test_sorted['Mês'], y_pred_sorted, color='red', label='Linha de Previsão')  # Linha de previsão
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Previsão de Vendas com Regressão Linear')
plt.legend()
plt.show()

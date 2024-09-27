import pandas as pd  # Para manipulação de dados
import matplotlib.pyplot as plt  # Para visualização de dados
from scipy.stats import linregress  # Para regressão linear

def draw_plot():
    # Carrega os dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')
    
    # Cria um gráfico de dispersão
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Calcula a linha de melhor ajuste para todo o conjunto de dados
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series([i for i in range(1880, 2050)])  # Gera uma série de anos de 1880 a 2050
    plt.plot(years, intercept + slope * years, label='Fit line: 1880-2050', color='blue')

    # Calcula a linha de melhor ajuste para os dados de 2000 até o ano mais recente
    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    recent_years = pd.Series([i for i in range(2000, 2050)])
    plt.plot(recent_years, intercept_recent + slope_recent * recent_years, label='Fit line: 2000-2050', color='green')

    # Adiciona rótulos e título ao gráfico
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Salva o gráfico como uma imagem PNG
    plt.savefig('sea_level_plot.png')
    
    return plt.gca()  # Retorna o objeto do eixo atual

# Chama a função para gerar o gráfico
draw_plot()

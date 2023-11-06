import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Leitura dos dados
df = pd.read_csv("googleplaystore.csv")

# Limpeza dos dados
df.drop_duplicates(subset="App", inplace=True)
df = df[df["Installs"] != "Free"]
df = df[df['Installs'] != "Paid"]
df = df[df["Android Ver"] != "NaN"]
df = df.dropna()

# Retirando + e , dos números de instalação
df["Installs"] = df["Installs"].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)
df["Installs"] = df["Installs"].apply(lambda x: x.replace(',', '') if ',' in str(x) else x)
df["Installs"] = df["Installs"].apply(lambda x: int(x))

# Convertendo todos os tamanhos para Mb
df["Size"] = df["Size"].apply(lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
df["Size"] = df["Size"].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
df["Size"] = df["Size"].apply(lambda x: str(x).replace('', '') if 'Free' in str(x) else x)
df["Size"] = df["Size"].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)
df["Size"] = df["Size"].apply(lambda x: float(x))

a = int(input())

if a == 1:
# Gráfico de pizza com as categorias mais frequentes
    categorias = df["Category"].value_counts().sort_values(ascending=False)
    categorias_limite = 10
    legendas = ["Família", "Jogos", "Ferramentas", "Corporativo", "Medicina", "Personalização", "Produtividade", "Estilo de vida","Finanças", "Esportes"]
    categorias = categorias.head(categorias_limite)
    plt.pie(categorias, labels=legendas, autopct='%1.1f%%', startangle=90)
    plt.title("As 10 categorias mais populares")
    plt.show()

# Gráfico de barras com as avaliações dos usuários e sua média
elif a == 2:
    bins_sturges = 1 + int(np.log2(len(df["Rating"])))
    plt.hist(df["Rating"], range=[1,5], bins=bins_sturges)
    plt.title("Avaliações gerais\nMediana de: {}".format(np.nanmedian(df["Rating"])))
    plt.show()

# Gráfico de barras por categoria com as avaliações dos usuários e sua média
elif a == 3:
    print(df["Category"].value_counts())
    especifico = input()
    df_specifc = df[df["Category"] == especifico]
    bins_sturges = 1 + int(np.log2(len(df_specifc["Rating"])))
    plt.hist(df_specifc["Rating"], range=[1,5], bins=bins_sturges)
    plt.title("Avaliações de {}\nMediana de: {}".format(especifico, np.nanmedian(df_specifc["Rating"])))
    plt.show()

# Mapa de calor das correlações
elif a == 4:
    colunas_numericas = ["Rating", "Reviews", "Size", "Installs"]
    df_numericas = df[colunas_numericas]
    correlacoes = df_numericas.corr()
    sns.heatmap(correlacoes, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Mapa de Calor das Correlações")
    plt.show()

# Gráfico de dispersão de reviews e número de downloads
elif a == 5:
    df_copy = df.copy()
    # Filtrar valores de "Reviews" maiores que 10 e "Installs" maiores que 0
    df_copy["Reviews"] = df_copy["Reviews"].astype(float)
    df_copy = df_copy[df_copy["Reviews"] > 10]
    df_copy = df_copy[df_copy["Installs"] > 0]

    # Aplicar escala logarítmica aos valores de "Reviews" e "Installs"
    df_copy["Reviews"] = np.log10(df_copy["Reviews"])
    df_copy["Installs"] = np.log10(df_copy["Installs"])

    plt.scatter(df_copy["Reviews"], df_copy["Installs"], alpha=0.5)
    plt.xlabel("Reviews(log)")
    plt.ylabel("Downloads(log))")
    plt.title("Relação entre Quantidade de Reviews e Quantidade de Downloads")

    # Calcular a linha de regressão linear
    m, b = np.polyfit(df_copy["Reviews"], df_copy["Installs"], 1)
    plt.plot(df_copy["Reviews"], m * df_copy['Reviews'] + b, color='darkblue')
    plt.show()

# Gráfico de pizza com a porcentagem de aplicativos pagos e gratuitos
elif a == 6:
    contagem_pagos = df["Type"].value_counts()
    plt.pie(contagem_pagos, labels=["Gratuitos", "Pagos"], autopct='%1.1f%%', startangle=90)
    plt.title("Porcentagem de aplicativos pagos vs. aplicativos gratuitos")
    plt.show()

# Gráfico de barras do número de downloads etre aplicativos pagos e gratuitos
elif a == 7:
    downloads_por_tipo = df.groupby("Type")["Installs"].sum()
    downloads_por_tipo.plot(kind='bar', color=["blue", "green"])
    plt.xticks(rotation=0)
    plt.xlabel("Tipo de Aplicativo")
    plt.ylabel("Quantidade de Downloads(log)")
    plt.yscale("log")
    plt.title("Número de downloads entre aplicativos pagos vs. aplicativos gratuitos")
    plt.show()

# Gráfico de dispersão entre preço do aplicativo e número de downloads
elif a == 8:
    # Convertendo os preços para float e filtrando os acima de 200
    df = df[df["Type"] != "Free"]
    df["Price"] = df["Price"].str.replace('$', '').astype(float)
    mascara = df["Price"] > 200
    df_filtrado = df[~mascara]

    plt.scatter(df_filtrado["Price"], df_filtrado["Installs"], alpha=0.4)
    plt.xlabel("Preço do Aplicativo")
    plt.ylabel("Número de Downloads")
    plt.title("Relação entre Preço do Aplicativo e Número de Downloads")
    plt.yscale("log")
    plt.show()

# Gráfico de dispersão entre classificação do aplicativo e quantidade de downloads
elif a == 9:
    plt.scatter(df["Rating"], df["Installs"], alpha=0.5)
    plt.xlabel("Classificação")
    plt.ylabel("Quantidade de Downloads")
    plt.title("Relação entre Classificação e Quantidade de Downloads")
    plt.yscale("log")
    plt.show()

# Gráfico de dispersão entre preço do aplicativo e classificação
elif a == 10:
    # Convertendo os preços para float e filtrando os acima de 200
    df = df[df["Type"] != "Free"]
    df["Price"] = df["Price"].str.replace('$', '').astype(float)
    mascara = df["Price"] > 200
    df_filtrado = df[~mascara]


    plt.scatter(df_filtrado["Price"], df_filtrado["Rating"], alpha=0.4)
    plt.xlabel("Preço do Aplicativo")
    plt.ylabel("Classificação")
    plt.title("Relação entre Preço de Aplicativo e Classificação")
    plt.show()

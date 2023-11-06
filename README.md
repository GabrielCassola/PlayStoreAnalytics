# PlayStoreAnalytics (Em desenvolvimento)
**Descrição:** Este projeto de análise de dados tem como objetivo explorar e compreender o vasto conjunto de informações disponíveis na Google Play Store, uma das maiores plataformas de distribuição de aplicativos para dispositivos móveis, abrigando milhares de aplicativos de diversas categorias, tornando-se um campo fértil para investigações sobre o mercado mobile.

**Objetivos:**
   - Exploração de Dados: Coletar, limpar e explorar os dados disponíveis, incluindo informações sobre aplicativos, classificações, downloads, categorias e preços.
   - Análise de Tendências: Identificar tendências e padrões no mercado de aplicativos, como categorias mais populares, preços médios, classificações mais comuns e distribuição de downloads.
   - Relação entre Preço e Popularidade: Investigar como o preço dos aplicativos afeta sua popularidade, medindo a relação entre o preço e o número de downloads ou classificações.
   - Avaliação de Desenvolvedores: Analisar o desempenho de diferentes desenvolvedores e estúdios com base em suas classificações médias e números de downloads.
   - Impacto das Atualizações e Versões do Android: Avaliar o impacto das atualizações de aplicativos e das versões do Android na satisfação do usuário e no número de downloads.

**Métodos:**
- Neste projeto, utilizaremos técnicas de análise de dados, visualização de dados e estatísticas descritivas para extrair insights valiosos. Faremos uso de bibliotecas Python, como Pandas e Matplotlib, para manipular os dados e criar visualizações informativas.

**Resultados Esperados:**
- Espero obter uma compreensão aprofundada do mercado de aplicativos móveis por meio da análise de dados da Google Play Store. Isso inclui insights sobre quais categorias de aplicativos são mais populares, como o preço afeta a popularidade dos aplicativos e como as classificações impactam a satisfação do usuário. Essas informações podem ser valiosas para desenvolvedores, empresas e pesquisadores interessados no mercado de aplicativos móveis.
- As considerações detalhadas sobre as análises e outros resultados estarão disponíveis em um PDF anexado no repositório deste projeto.


## Requisitos

- Python 3
- Bibliotecas Python: pandas, matplotlib, numpy, seaborn
  
## Uso

1. Faça o download do arquivo `googleplaystore.csv` com os dados e coloque-o na mesma pasta que este código.

2. Execute o código Python `analise_google_play_store.py`.

3. Escolha uma das opções disponíveis:
   - Para visualizar as 10 categorias mais populares, digite `1`.
   - Para visualizar um histograma das avaliações gerais, digite `2`.
   - Para visualizar um histograma de avaliações por categoria, digite `3` e insira a categoria desejada.
   - Para visualizar um mapa de calor das correlações, digite `4`.
   - Para visualizar um gráfico de dispersão entre reviews e downloads, digite `5`.
   - Para visualizar a porcentagem de aplicativos pagos vs. gratuitos, digite `6`.
   - Para visualizar um gráfico de barras do número de downloads entre aplicativos pagos vs. gratuitos, digite `7`.
   - Para visualizar um gráfico de dispersão entre preço e downloads, digite `8`.
   - Para visualizar um gráfico de dispersão entre classificação e downloads, digite `9`.
   - Para visualizar um gráfico de dispersão entre preço e classificação, digite `10`.
  
## Atualizações Futuras
Estou planejando várias atualizações e melhorias para este projeto no futuro. Algumas das áreas em que estou trabalhando incluem:

   ### Interface Gráfica (GUI)

   Estou explorando a possibilidade de adicionar uma interface gráfica de usuário (GUI) para tornar este projeto mais acessível e fácil de usar.
   
   ### Mais Análises
   
   Planejo expandir as análises disponíveis neste projeto para fornecer insights ainda mais abrangentes sobre o mercado de aplicativos móveis. Isso pode incluir análises adicionais de dados, gráficos e visualizações.
   
   ### Análise de Sentimentos de Reviews
   
   Estou aprimorando a análise de sentimentos de reviews de aplicativos com as bibliotecas WordCloud e NLTK. Isso permitirá uma análise mais detalhada das opiniões e feedback dos usuários, gerando visualizações de nuvem de palavras e métricas de sentimentos.

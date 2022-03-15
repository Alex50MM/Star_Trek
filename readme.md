# Análise de Dados dos episódios de Star Trek: The Next Generation.

## O dataset foi extraído do seguinte repositório no github
https://github.com/RMHogervorst/TNG
https://github.com/RMHogervorst/TNG/tree/master/raw-data

## Importação da Biblioteca Pandas.
`import pandas as pd`

## Importação da base de dados que se encontra na pasta data com o arquivo TNG.csv .
`startrek = pd.read_csv ("data\TNG.csv")`

### No meu caso, utilizei a primeira vez o editor ATOM (https://atom.io), precisei incluir também o encoding na Importação, pois estava dando erro de codificação.
`startrek = pd.read_csv ("data\TNG.csv", encoding = 'latin-1')`

## Usando o comando .info(), comecei minha análise para verificar se haviam informações que precisavam ser corrigidas.
`startrek.info()`

## Neste momento identifiquei que a Serie (Coluna) Released (que se refere a data que foi lançada os episódios), estava como tipo objeto e fiz a alteração para tipo data.
`startrek['Released'] = pd.to_datetime (startrek['Released'])`

#### Também queria realizar o ajuste das Séries Episode e Season que estava como Float e alterar para Int.
`startrek[['Episode', 'Season']].astype(int)`

#### Porém não era possível pois retornou uma mensagem de erro, pois havia células vazias, de um total de 110.176 linhas no total, a Serie Episode e a Serie Season havia 10.899 células vazias. Para corrigir o tipo destas células eu deveria realizar o seguinte comando, para preencher as células vazias com um valor zero e só então realizar o comando anterior para então poder converter as colunas de Float para Int.
`startrek = startrek.fillna(0)`

#### Resolvi analisar em relação as avaliações dadas a cada episódio e também por temporada. Iniciando com um describe() para começar a entender os gráficos que serão gerados a seguir.
`startrek.imdbRating.describe()`

## Deletei algumas Colunas (ou Series) que não tinha interesse em manter em meu dataframe:
### Caso você queira excluir somente uma coluna (ou Serie), utilizar o comando a seguir:
`startrek.drop('Unnamed: 0', axis= 1)`

### Neste caso eu quis excluir algumas Colunas (ou Series) que continha alguns textos que eu não achei interessante no momento, então para excluir múltiplas Colunas (ou Series), é preciso definir que vai excluir (drop) colunas e então colocar os nomes das Colunas entre Colchetes
`startrek.drop(columns = ['Unnamed: 0', 'productionnumber', 'type', 'text', 'speechdescription', 'imdbID'])`

#### Criando um gráfico do tipo scatter (gráfico de dispersão)
`startrek.plot.scatter(x = 'imdbRating', y = 'Season')`

#### Por fim, salvei o meu dataframe em um arquivo Excel contendo somente as informações que julguei relevantes
`startrek.to_excel ('data\startrek.xlsx', sheet_name = 'Next Generation', index = False)`

# import pandas as pd
import polars as pl
from datetime import datetime
# pip instal fast parquet


ENDERECO_DADOS = './../BOLSA FAMILIA/'

try:
    inicio = datetime.now()

    # LENDO PARQUET LEITURA DIRETA
    # Pandas Tempo de execução: 0:00:37.595855
    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # Polars Tempo de execução: 0:00:11.796894
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    print(df_bolsa_familia.head(10))
    final = datetime.now()
    print(f'Tempo de execução: {final - inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo Parquet: {e}')


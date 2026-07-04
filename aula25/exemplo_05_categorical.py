# import pandas as pd
import polars as pl
from datetime import datetime

# pip instal fast parquet


ENDERECO_DADOS = './../BOLSA FAMILIA/'

try:
    inicio = datetime.now()

    # Uso do Categorical para melhorar a performance da RAM
    # Uso do Categorical para comprar os munícipios repetidos
    df_scan = (pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet').select(['NOME MUNICÍPIO', 'VALOR PARCELA']).with_columns([pl.col('NOME MUNICÍPIO').cast(pl.Categorical)]).group_by('NOME MUNICÍPIO').agg(pl.col('VALOR PARCELA').sum()).sort('VALOR PARCELA', descending=True))

    df_bolsa_familia = df_scan.collect()
    print(df_bolsa_familia.head(10))

    final = datetime.now()
    print(f'Tempo de execução: {final - inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo Parquet: {e}')

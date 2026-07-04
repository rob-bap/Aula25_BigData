# import pandas as pd
import polars as pl
from datetime import datetime

# pip instal fast parquet


ENDERECO_DADOS = './../BOLSA FAMILIA/'

try:
    inicio = datetime.now()

    # LENDO PARQUET LEITURA *PREGUIÇOSA SCAN_PARQUET

    # Polars Tempo de execução: 0:00:14.178371
    # scan_parquet gera um plano de execução, não traz os dados.
    df_scan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    # print(df_scan) printa o plano de execução

    # pré-processamento

    # Collect executao o plano, carregando os dados para a memóra
    df_bolsa_familia = df_scan.collect()
    print(df_bolsa_familia.head(10))

    final = datetime.now()
    print(f'Tempo de execução: {final - inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo Parquet: {e}')


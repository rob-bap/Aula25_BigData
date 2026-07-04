# import pandas as pd
import polars as pl
from datetime import datetime  # trabalhar com o tempo
import os

ENDERECO_DADOS = './../BOLSA FAMILIA/'

# pd = 0:01:47.381650
# pl = 0:00:32.057238

try:
    inicio = datetime.now()
    print('Carregando dados...')

    df_bolsa_familia = None
    lista_arquivos = []

    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
    # print(lista_dir_arquivos)

    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)
    # print(lista_arquivos)
            
    for nome in lista_arquivos:
        print(f'Processando arquivo {nome}')
        # df = pd.read_csv(ENDERECO_DADOS + nome, sep=';', encoding='iso-8859-1')
        df = pl.read_csv(ENDERECO_DADOS + nome, separator=';', encoding='iso-8859-1')

        if df_bolsa_familia is None:
            df_bolsa_familia = df

        else:
            # pd.concat([df_bolsa_familia, df])
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        del df

        print(f'Aquivo {nome} processado com sucesso!')
        # print(df_bolsa_familia.shape)

    # converter a serie 'valor parcela'
    df_bolsa_familia = df_bolsa_familia.with_columns(pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64))

    print('Iniciando a gravação do arquivo parquet...')
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    print('\nGravação do arquivo parquet concluida com sucesso!')
        
    final = datetime.now()
    print(f'Tempo de execução: {final - inicio}')

    print(df_bolsa_familia.head(10))
    print(df_bolsa_familia.columns)
    print(df_bolsa_familia.shape)

except Exception as e:
    print(f"Erro ao obter dados : {e}")
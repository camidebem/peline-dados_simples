from extract import extract_data
from transform import transform_data
from load import load_to_db, load_to_csv

def run_etl():
    # Passo 1: Extrair dados
    filepath = '/home/camily/pipeline-dados/data/daily_food_nutrition_dataset.csv'
    df = extract_data(filepath)
    print("Dados extraídos com sucesso!")

    # Passo 2: Transformar dados
    df_transformed = transform_data(df)
    print("Dados transformados com sucesso!")

    # Passo 3: Carregar dados - escolha entre banco de dados ou CSV
    db_url = 'postgresql://camily_de_bem:123@localhost:5432/bancodeteste'  
    table_name = 'dados_nutricionais'  # Nome da tabela no banco de dados

    # Carregar para banco de dados
    load_to_db(df_transformed, db_url, table_name)

    # Ou, se preferir carregar para CSV, descomente a linha abaixo:
    # load_to_csv(df_transformed, 'data/dados_transformados.csv')

if __name__ == '__main__':
    run_etl()

from sqlalchemy import create_engine

def load_to_db(df, db_url, table_name):
    """Carrega os dados para um banco PostgreSQL"""
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, index=False, if_exists='replace')
    print(f"Dados carregados na tabela {table_name} com sucesso!")

def load_to_csv(df, filepath):
    """Carrega os dados em um arquivo CSV"""
    df.to_csv(filepath, index=False)
    print(f"Dados salvos em {filepath}")

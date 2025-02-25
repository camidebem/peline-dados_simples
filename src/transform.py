import pandas as pd


def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def create_new_columns(df):
    
    # Calcular a soma total de calorias por usuário e por dia
    df['data'] = pd.to_datetime(df['Date'])  # Caso a coluna 'Date' não seja datetime, converta
    df['total_calorias_por_dia'] = df.groupby(['User_ID', df['data'].dt.date])['Calories (kcal)'].transform('sum')

    # Calcular a média de calorias consumidas por dia por usuário
    df['media_calorias_diaria_usuario'] = df.groupby('User_ID')['total_calorias_por_dia'].transform('mean')

    # Calcular a soma total de calorias por refeição e usuário
    df['calorias_totais_refeicao'] = df.groupby(['User_ID', 'Meal_Type'])['Calories (kcal)'].transform('sum')

    # Calcular a média de calorias consumidas por refeição
    df['media_calorias_refeicao_usuario'] = df.groupby(['User_ID', 'Meal_Type'])['calorias_totais_refeicao'].transform('mean')

    # Encontrar a refeição com maior quantidade de sódio por usuário
    df['maior_consumo_sodio_usuario'] = df.groupby('User_ID')['Sodium (mg)'].transform('max')

    # Calcular a ingestão total de água por usuário e por dia
    df['total_agua_por_dia'] = df.groupby(['User_ID', df['data'].dt.date])['Water_Intake (ml)'].transform('sum')

    # Contar o número de refeições por dia por usuário
    df['num_refeicoes_por_dia_usuario'] = df.groupby(['User_ID', df['data'].dt.date])['Meal_Type'].transform('count')

    return df

def transform_data(df):
    """Função principal de transformação"""
    df = clean_data(df)
    df = create_new_columns(df)
    return df
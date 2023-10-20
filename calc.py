import datetime

# Defina a data inicial do seu portfolio
data_inicial = datetime.datetime(2023, 7, 10)

# Obtenha a data atual
data_atual = datetime.datetime.now(2023, 7, 10)

# Calcule a diferença entre as datas
diferenca = data_atual - data_inicial

# Calcule o número de anos passados
anos_passados = diferenca.days // 365

# Atualize a data inicial com base nos anos passados
data_atualizada = data_inicial + datetime.timedelta(days=anos_passados*365)

# Imprima a data atualizada
print("Data atualizada:", data_atualizada.strftime("%d/%m/%Y"))

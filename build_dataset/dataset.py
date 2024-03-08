import os
import csv
from collections import defaultdict
import sys

diretorio = os.path.dirname(sys.modules['__main__'].__file__)

dfs = []

registros = {}

campos = {
    'Average annual working hours per worker': '0',
    'GDP per capita': '0',
    'MtCO2e': '0',
    'IDH': '0',
    'Inequality in income': '0',
    'Life Expectancy': '0',
    'Material footprint per capita': '0',
    'Poverty Index': '0',
    'Population Total': '0',
    'GDP': '0',
    'business': '0'
}

for arquivo in os.listdir(diretorio):
    caminho_arquivo = os.path.join(diretorio, arquivo)
    if caminho_arquivo.endswith('.csv'):
        with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            for linha in leitor_csv:
                key = linha['Entity'] + ',' + linha['Code'] + ',' + linha['Year']
                registros[key] = campos

annual = []
gdp = []
idh = []
ini = []
life = []
material = []
mtc = []
poor = []
pop = []
gdp_t = []
time_business = []
all_keys = []
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.csv'):
        with open(arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                key = linha['Entity'] + ',' + linha['Code'] + ',' + linha['Year']
                all_keys.append(key)

                if arquivo == 'annual-working-hours-per-worker.csv':
                    valor = linha['Average annual working hours per worker']
                    annual.append([key, [valor, 0,0,0,0,0,0,0,0,0,0]])
                    
                if arquivo == 'gdp-per-capita-penn-world-table.csv':
                    valor = linha['GDP per capita']
                    gdp.append([key, [0, valor, 0,0,0,0,0,0,0,0,0]])

                if arquivo == 'MTC.csv':
                    valor = linha['MtCO2e']
                    mtc.append([key, [0, 0, valor,0,0,0,0,0,0,0,0]])
                
                if arquivo == 'idh.csv':
                    valor = linha['IDH']
                    idh.append([key, [0, 0, 0, valor,0,0,0,0,0,0,0]])
                
                if arquivo == 'INI.csv':
                    valor = linha['Inequality in income']
                    ini.append([key, [0, 0, 0,0,valor,0,0,0,0,0,0]])

                if arquivo == 'LIFE.csv':
                    valor = linha['Life Expectancy']
                    life.append([key, [0, 0, 0,0,0,valor,0,0,0,0,0]])

                if arquivo == 'material.csv':
                    valor = linha['Material footprint per capita']
                    material.append([key, [0, 0, 0,0,0,0,valor,0,0,0,0]])

                if arquivo == 'poor.csv':
                    valor = linha['Poverty Index']
                    poor.append([key, [0, 0, 0,0,0,0,0,valor,0,0,0]])

                if arquivo == 'pop.csv':
                    valor = linha['Population Total']
                    pop.append([key, [0, 0, 0,0,0,0,0,0,valor,0,0]])
                
                if arquivo == 'national-gdp-wb.csv':
                    valor = linha['GDP']
                    gdp_t.append([key, [0, 0, 0,0,0,0,0,0,0,valor,0]])

                if arquivo == 'time-required-to-start-business.csv':
                    valor = linha['business']
                    time_business.append([key, [0, 0, 0,0,0,0,0,0,0,0,valor]])

reg = annual + gdp + idh + ini + life + material + mtc + poor + pop + gdp_t + time_business
reg2 = sorted(reg, key=lambda x: x[0])

sem_repetir = []
for i in reg2:
    if i[0] not in sem_repetir:
        sem_repetir.append(i[0])

grupo = defaultdict(list)
for item in reg2:
    grupo[item[0]].append(item[1])

lista_final = []
resultado = []
for k, v in grupo.items():
    result = [next((i for i in s if i != 0), 0) for s in zip(*v)]
    resultado.append([k, result])

for a in resultado: 
    x = a[0].split(',') + a[1]

    if x[3] == '': 
        _3 = 0.0
    else:
        _3 = float(x[3])

    if x[4] == '': 
        _4 = 0.0
    else:
        _4 = float(x[4])

    if x[5] == '': 
        _5 = 0.0
    else:
        _5 = float(x[5])

    if x[6] == '': 
        _6 = 0.0
    else:
        _6 = float(x[6])

    if x[7] == '': 
        _7 = 0.0
    else:
        _7 = float(x[7])

    if x[8] == '': 
        _8 = 0.0
    else:
        _8 = float(x[8])

    if x[9] == '': 
        _9 = 0.0
    else:
        _9 = float(x[9])

    if x[10] == '': 
        _10 = 0.0
    else:
        _10 = float(x[10])
    
    if x[11] == '': 
        _11 = 0.0
    else:
        _11 = float(x[11])

    if x[12] == '': 
        _12 = 0.0
    else:
        _12 = float(x[12])

    if x[13] == '': 
        _13 = 0.0
    else:
        _13 = float(x[13])

    s = [x[0], x[1], int(x[2]), _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13]

    lista_final.append(s)

caminho_arquivo = './dataset.csv.txt'

coluns = [
    'Entity',
    'Code',
    'Year',
    'Average annual working hours per worker',
    'GDP per capita',
    'MtCO2e',
    'IDH',
    'Inequality in income',
    'Life Expectancy',
    'Material footprint per capita',
    'Poverty Index',
    'Population Total',
    'GDP',
    'business']

with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(coluns)
    escritor_csv.writerows(lista_final)
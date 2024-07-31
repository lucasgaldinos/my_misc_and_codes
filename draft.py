import pandas as pd

cities = ['PERDOES,MG',
          'CASTRO,PR',
          'REALEZA,PR',
          'ALTO PARNAIBA,MA',
          'FEIRA DE SANTANA,BA',
          'TRES PASSOS,RS',
          'RIO DO SUL,SC',
          'URUACU,GO',
          'CHAPADINHA,MA',
          'LAGUNA CARAPA,MS',
          'BELO ORIENTE,MG',
          'FREDERICO WESTPHALEN,RS',
          'IBIRUBA,RS',
          'PONTA PORA,MS',
          'IRATI,PR',
          'SAO JOAQUIM,SC',
          'DRACENA,SP',
          'QUERENCIA DO NORTE,PR',
          'GUANHAES,MG',
          'BELA VISTA,MS',
          'CURVELO,MG',
          'LAGES,SC',
          'TUBARAO,SC',
          'CONCORDIA,SC',
          'FRAIBURGO,SC',
          'AMAMBAI,MS',
          'SANTA BARBARA,MG',
          'POMPEU,MG',
          'JUIZ DE FORA,MG',
          'ELDORADO,MS',
          'SANTA BARBARA,SP',]

ahh = list(map(lambda x: x.split(','), cities))

print(ahh)

lista = [0 for _ in range(len(ahh))]
df = pd.DataFrame([[ahh], lista], ['city', 'region', 'nulos1'])

print(df)

print(df)

from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astroquery.simbad import Simbad
import csv

# procurar estrelas Gaia no Hipparcos

csv_file_path = 'designation.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    designation = []
    for row in csv_reader:
        designation.append(row[0])
print("Tamanho da lista designation {}".format(len(designation)))
#print(designation)

hipparcos = []
quantidade_de_estrelas_com_hip = 0
for id in designation:
    tab = Simbad.query_objectids(id)
    if (len([id for id in tab['ID'] if id.startswith('HIP')]) == 0):
        hipparcos.append(None)
    else:
        quantidade_de_estrelas_com_hip += 1
        hipparcos.append([id for id in tab['ID'] if id.startswith('HIP')][0][4:])


print("Tamanho da lista hipparcos {}".format(len(hipparcos)))
soma = 0
for row in hipparcos:
    if row is None:
        continue
    #print(int(row))
    soma += 1
print("Quantidade de estrelas Gaia com HIP: {}".format(soma))


csv_file_path = 'HIP_designation.csv'
#print(hipparcos)
with open(csv_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file, dialect='unix')
    for row1, row2 in zip(hipparcos, designation):
        if row1 is None:
            csv_writer.writerow(["", row2])
        else:
            csv_writer.writerow([row1, row2])


print("Quantidade de estrelas Gaia com HIP: {}".format(quantidade_de_estrelas_com_hip))
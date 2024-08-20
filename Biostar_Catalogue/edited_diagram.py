from astroquery.simbad import Simbad
import mysql.connector
import matplotlib.pyplot as plt
import decimal

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

# Criar o diagrama Hipparcos_minus_Gaia_MV_versus_B_minus_V_edited.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.HD, "
               "Hipparcos.Plx, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.Bt_minus_VT, "
               "Hipparcos_product.MV, "
               "Hipparcos_product.MVt "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.HIP not in ( "
               "select Gaia.HIP from Gaia where Gaia.HIP is not NULL) and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
HD_list = []
Plx_list = []
x_axis = []
BT_minus_VT_list = []
y_axis = []
MVt_list = []

for (HIP_value, HD_value, Plx_value, B_minus_V_value, BT_minus_VT_value, MV_value, MVt_value) in value:
    HIP_list.append(HIP_value)
    HD_list.append(HD_value)
    Plx_list.append(Plx_value)
    x_axis.append(B_minus_V_value)
    BT_minus_VT_list.append(BT_minus_VT_value)
    y_axis.append(MV_value)
    MVt_list.append(MVt_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
#plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))

plt.title("Hipparcos - Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")

# Colorindo as AFG
AFG = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y <= decimal.Decimal('4.82'):
        blue = plt.scatter([x], [y], s=size, marker=".", edgecolors='blue', alpha=transparency)
        AFG += (str(HIP),)

# Colorindo as anãs brancas
anas_brancas = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y >= decimal.Decimal(5.91)*decimal.Decimal(x) + decimal.Decimal(9.27):
        dodgerblue = plt.scatter([x], [y], s=size, marker=".", edgecolors='dodgerblue', alpha=transparency)
        anas_brancas += (str(HIP),)

# Colorindo as estrelas sem classificação
sem_classificacao = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y <= decimal.Decimal(5.91)*decimal.Decimal(x) + decimal.Decimal(9.27) and y >= decimal.Decimal(5.68)*decimal.Decimal(x) + decimal.Decimal(3.9):
        black = plt.scatter([x], [y], s=size, marker=".", edgecolors='black', alpha=transparency)
        sem_classificacao += (str(HIP),)

# Colorindo as GK
GK = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y <= decimal.Decimal(5.68)*decimal.Decimal(x) + decimal.Decimal(3.9) and y >= 4.82 and y <= decimal.Decimal(-5.26)*decimal.Decimal(x) + decimal.Decimal(14.842):
        coral = plt.scatter([x], [y], s=size, marker=".", edgecolors='coral', alpha=transparency)
        GK += (str(HIP),)

# Colorindo as anãs vermelhas
anas_vermelhas = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y <= decimal.Decimal(5.68)*decimal.Decimal(x) + decimal.Decimal(3.9) and y >= 4.82 and y >= decimal.Decimal(-5.26)*decimal.Decimal(x) + decimal.Decimal(14.842):
        red = plt.scatter([x], [y], s=size, marker=".", edgecolors='red', alpha=transparency)
        anas_vermelhas += (str(HIP),)

# equação da reta que passa pelo Sol
# y = 4.82
plt.axhline(y = 4.82, color = 'gray', linestyle=':', linewidth=1)

# equação da reta que isola as anãs brancas
# y = 5.91*x + 9.27
plt.plot([-0.4, 1], [6.9, 5.91*(1) + 9.27], color='gray', linestyle=':', linewidth=1)

# equação da reta que isola as estrelas não classificadas
# y = 5.68*x + 3.9
plt.plot([0.17, 1.9], [5.68*(0.17) + 3.9, 14.7], color='gray', linestyle=':', linewidth=1)

# equação da reta que isola as anãs vermelhas
# y = -5.26*x + 14.842
plt.plot([1, 1.9], [-5.26*(1) + 14.842, -5.26*(1.9) + 14.842], color='gray', linestyle=':', linewidth=1)

# Marcando o Sol
yellow = plt.scatter([0.65], [4.82], s=30, marker="o", color='yellow', edgecolors='gold', alpha=1)

# Legenda
plt.legend((yellow, blue, coral, red, dodgerblue, black),
           ('Sol', 'AFG ({} estrelas)'.format(len(AFG)), 'GK ({} estrelas)'.format(len(GK)), 'anãs vermelhas ({} estrelas)'.format(len(anas_vermelhas)), 'anãs brancas ({} estrelas)'.format(len(anas_brancas)), 'sem classificação ({} estrelas)'.format(len(sem_classificacao))),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=6)

plt.savefig('/home/lh/Desktop/Biostar_Catalogue/static/img/Hipparcos_minus_Gaia_MV_versus_B_minus_V_edited.png')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Hipparcos_minus_Gaia_MV_versus_B_minus_V_showing_gaia.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.Plx, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.HIP not in ( "
               "select Gaia.HIP from Gaia where Gaia.HIP is not NULL) and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis_temp = []
y_axis_temp = []

for (HIP_value, Plx_value, B_minus_V_value, MV_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis_temp.append(B_minus_V_value)
    y_axis_temp.append(MV_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
plt.xlim(min(x_axis_temp) - decimal.Decimal(0.2), max(x_axis_temp) + decimal.Decimal(0.2))
plt.ylim(max(y_axis_temp) + decimal.Decimal(0.5), min(y_axis_temp) - decimal.Decimal(0.5))

# Separar os dados das estrelas que têm designação mas não estão no catálogo 1
x_axis_gaia = []
y_axis_gaia = []
pop_axis = []

for i in range(len(HIP_list)):
    tab = Simbad.query_objectids("HIP " + str(HIP_list[i]))
    if (len([id for id in tab['ID'] if id.startswith('Gaia')]) != 0):
        # se esse if é True, entao a estrela com identificador HIP_list[i] tem designation, ela está no Gaia com distancia maior do que 23pc
        print(HIP_list[i])
        x_axis_gaia.append(x_axis_temp[i])
        y_axis_gaia.append(y_axis_temp[i])
        pop_axis.append(i)
x_axis = []
y_axis = []
for i in range(len(x_axis_temp)):
    if i not in pop_axis:
        x_axis.append(x_axis_temp[i])
        y_axis.append(y_axis_temp[i])

black = plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
lightcoral = plt.scatter(x_axis_gaia, y_axis_gaia, s = size, marker = ".", edgecolors = 'lightcoral', alpha = transparency)
plt.title("Hipparcos - Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")
plt.legend((lightcoral, black),
           ('Estrelas com designação Gaia ({} estrelas)'.format(len(x_axis_gaia)), 'Estrelas sem designação Gaia ({} estrelas)'.format(len(x_axis))),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=6)

plt.savefig('/home/lh/Desktop/Biostar_Catalogue/static/img/Hipparcos_minus_Gaia_MV_versus_B_minus_V_showing_gaia.png')

# close matplotlib.pyplot as plt object
plt.close()

# Make sure data is committed to the database
connection.commit()

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_white_dwarfs.csv
anas_brancas = ",".join(anas_brancas)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_white_dwarfs_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % anas_brancas)
# sql = "insert into cust_table(name)values(names)where cust_id IN('{ids}')"
#sql = "SELECT * FROM table WHERE column = ANY(%(parameter_array)s)"
#cur.execute(sql,{"parameter_array": [1, 2, 3]})

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_unknown.csv
sem_classificacao = ",".join(sem_classificacao)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_unknown_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % sem_classificacao)

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_AFG.csv
AFG = ",".join(AFG)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_AFG_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % AFG)

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_GK.csv
GK = ",".join(GK)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_GK_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % GK)

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_red_dwarfs.csv
anas_vermelhas = ",".join(anas_vermelhas)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_red_dwarfs_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % anas_vermelhas)

cursor.close()
connection.close()
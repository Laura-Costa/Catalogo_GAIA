import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

'''
 Criando um arquivo do tipo CSV para cada tabela 
'''

# Criando o arquivo CAT1.csv

cursor.execute('''select CAT1.designation, '''
               '''CAT1.HIP, '''
               '''CAT1.HD, '''
               '''TRIM(CAT1.ra)+0, '''
               '''TRIM(CAT1.declination)+0, '''
               '''TRIM(CAT1.parallax)+0, '''
               '''TRIM(CAT1.parallax_error)+0, '''
               '''TRIM(CAT1.pm)+0, '''
               '''TRIM(CAT1.pmra)+0, '''
               '''TRIM(CAT1.pmdec)+0, '''
               '''TRIM(CAT1.ruwe)+0, '''
               '''TRIM(CAT1.phot_g_mean_mag)+0, '''
               '''TRIM(CAT1.phot_bp_mean_mag)+0, '''
               '''TRIM(CAT1.phot_rp_mean_mag)+0, '''
               '''TRIM(CAT1.teff_gspphot)+0, '''
               '''TRIM(CAT1.teff_gspphot_lower)+0, '''
               '''TRIM(CAT1.teff_gspphot_upper)+0, '''
               '''TRIM(CAT1.logg_gspphot)+0, '''
               '''TRIM(CAT1.logg_gspphot_lower)+0, '''
               '''TRIM(CAT1.logg_gspphot_upper)+0, '''
               '''TRIM(CAT1.mh_gspphot)+0, '''
               '''TRIM(CAT1.mh_gspphot_lower)+0, '''
               '''TRIM(CAT1.mh_gspphot_upper)+0, '''
               '''TRIM(CAT1.distance_gspphot)+0, '''
               '''TRIM(CAT1.distance_gspphot_lower)+0, '''
               '''TRIM(CAT1.distance_gspphot_upper)+0, '''
               '''TRIM(CAT1_product.Mg)+0, '''
               '''TRIM(CAT1_product.Mg_error)+0, '''
               '''TRIM(CAT1_product.MRp)+0, '''
               '''TRIM(CAT1_product.MRp_error)+0, '''
               '''TRIM(CAT1_product.Bp_minus_Rp)+0 '''
               '''from CAT1, CAT1_product '''
               '''where CAT1.designation = CAT1_product.designation '''
               '''order by CAT1.parallax asc '''
               '''into outfile '/var/lib/mysql-files/CAT1.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["designation", "HIP", "HD", "ra", "declination", "parallax", "parallax_error", "pm", "pmra",
               "pmdec", "ruwe", "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag", "teff_gspphot",
               "teff_gspphot_lower", "teff_gspphot_upper", "logg_gspphot", "logg_gspphot_lower",
               "logg_gspphot_upper", "mh_gspphot", "mh_gspphot_lower", "mh_gspphot_upper", "distance_gspphot",
               "distance_gspphot_lower", "distance_gspphot_upper", "Mg", "Mg_error", "MRp", "MRp_error", "Bp_minus_Rp"]

file = pd.read_csv("/var/lib/mysql-files/CAT1.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1/csv/CAT1.csv", header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT1.csv")

# Criando o arquivo CAT2_MV_versus_B_minus_V_plotted.csv

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''IF (CAT2.HIP in ( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL), '''
               '''(select CAT1.designation from CAT1 where CAT1.HIP = CAT2.HIP), NULL) AS designation, '''
               '''TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, '''
               '''CAT2.DEdms, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, '''
               '''TRIM(CAT2.pmDE)+0, '''
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MV is not NULL and '''
               '''CAT2_product.B_minus_V is not NULL '''
               '''order by CAT2.Plx ASC '''
               '''into outfile '/var/lib/mysql-files/CAT2_MV_versus_B_minus_V_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["HIP", "HD", "designation", "Vmag", "RAdeg", "DEdeg", "RAhms", "DEdms", "Plx", "e_Plx", "distance_Plx",
               "pmRA", "pmDE", "BTmag", "VTmag", "MV", "MV_error", "MVt", "MVt_error", "B_minus_V", "BT_minus_VT"]

file = pd.read_csv("/var/lib/mysql-files/CAT2_MV_versus_B_minus_V_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/csv/CAT2_MV_versus_B_minus_V_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_MV_versus_B_minus_V_plotted.csv")

# Criando o arquivo CAT2_MVt_versus_BT_minus_VT_plotted.csv

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''IF (CAT2.HIP in ( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL), '''
               '''(select CAT1.designation from CAT1 where CAT1.HIP = CAT2.HIP), NULL) AS designation, '''
               '''TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, '''
               '''CAT2.DEdms, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, '''
               '''TRIM(CAT2.pmDE)+0, '''
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MVt is not NULL and '''
               '''CAT2_product.BT_minus_VT is not NULL '''
               '''order by CAT2.Plx ASC '''
               '''into outfile '/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["HIP", "HD", "designation", "Vmag", "RAdeg", "DEdeg", "RAhms", "DEdms", "Plx", "e_Plx", "distance_Plx",
               "pmRA", "pmDE", "BTmag", "VTmag", "MV", "MV_error", "MVt", "MVt_error", "B_minus_V", "BT_minus_VT"]

file = pd.read_csv("/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/csv/CAT2_MVt_versus_BT_minus_VT_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_plotted.csv")

# Criando o arquivo CAT2_MVt_versus_BT_minus_VT_not_plotted.csv

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''IF (CAT2.HIP in ( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL), '''
               '''(select CAT1.designation from CAT1 where CAT1.HIP = CAT2.HIP), NULL) AS designation, '''
               '''TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, '''
               '''CAT2.DEdms, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, '''
               '''TRIM(CAT2.pmDE)+0, '''
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP = CAT2_product.HIP and '''
               '''(CAT2_product.MVt is NULL or '''
               '''CAT2_product.BT_minus_VT is NULL) '''
               '''order by CAT2.Plx ASC '''
               '''into outfile '/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_not_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["HIP", "HD", "designation", "Vmag", "RAdeg", "DEdeg", "RAhms", "DEdms", "Plx", "e_Plx", "distance_Plx",
               "pmRA", "pmDE", "BTmag", "VTmag", "MV", "MV_error", "MVt", "MVt_error", "B_minus_V", "BT_minus_VT"]

file = pd.read_csv("/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_not_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/csv/CAT2_MVt_versus_BT_minus_VT_not_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_not_plotted.csv")

# Criando o arquivo CAT1_intersection_CAT2_Mg_versus_Bp_minus_Rp.csv

cursor.execute('''select CAT1.designation, ''' 
               '''CAT1.HIP, ''' 
               '''CAT1.HD, ''' 
               '''TRIM(CAT1.ra)+0, ''' 
               '''TRIM(CAT1.declination)+0, ''' 
               '''TRIM(CAT1.parallax)+0, ''' 
               '''TRIM(CAT1.parallax_error)+0, '''
               '''TRIM(CAT1.pm)+0, ''' 
               '''TRIM(CAT1.pmra)+0, '''
               '''TRIM(CAT1.pmdec)+0, '''
               '''TRIM(CAT1.ruwe)+0, '''
               '''TRIM(CAT1.phot_g_mean_mag)+0, ''' 
               '''TRIM(CAT1.phot_bp_mean_mag)+0, ''' 
               '''TRIM(CAT1.phot_rp_mean_mag)+0, '''
               '''TRIM(CAT1.teff_gspphot)+0, ''' 
               '''TRIM(CAT1.teff_gspphot_lower)+0, ''' 
               '''TRIM(CAT1.teff_gspphot_upper)+0, ''' 
               '''TRIM(CAT1.logg_gspphot)+0, ''' 
               '''TRIM(CAT1.logg_gspphot_lower)+0, ''' 
               '''TRIM(CAT1.logg_gspphot_upper)+0, ''' 
               '''TRIM(CAT1.mh_gspphot)+0, '''
               '''TRIM(CAT1.mh_gspphot_lower)+0, ''' 
               '''TRIM(CAT1.mh_gspphot_upper)+0, ''' 
               '''TRIM(CAT1.distance_gspphot)+0, '''
               '''TRIM(CAT1.distance_gspphot_lower)+0, '''
               '''TRIM(CAT1.distance_gspphot_upper)+0, '''
               '''TRIM(CAT1_product.Mg)+0, ''' 
               '''TRIM(CAT1_product.Mg_error)+0, '''
               '''TRIM(CAT1_product.MRp)+0, '''
               '''TRIM(CAT1_product.MRp_error)+0, '''
               '''TRIM(CAT1_product.Bp_minus_Rp)+0, '''
               '''TRIM(CAT2.Vmag)+0, ''' 
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, ''' 
               '''CAT2.DEdms, ''' 
               '''TRIM(CAT2.Plx)+0, ''' 
               '''TRIM(CAT2.e_Plx)+0, ''' 
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, ''' 
               '''TRIM(CAT2.pmDE)+0, ''' 
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, ''' 
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 ''' 
               '''from CAT1, CAT1_product, CAT2, CAT2_product '''
               '''where CAT1.designation = CAT1_product.designation and '''
               '''CAT1.HIP = CAT2.HIP and CAT2.HIP = CAT2_product.HIP and '''
               '''CAT1_product.Mg is not null and '''
               '''CAT1_product.Bp_minus_Rp is not null '''
               '''order by CAT1.parallax ASC '''
               '''into outfile '/var/lib/mysql-files/CAT1_intersection_CAT2_Mg_versus_Bp_minus_Rp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["designation", "HIP", "HD", "ra", "declination", "parallax", "parallax_error", "pm", "pmra", "pmdec", "ruwe",
               "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag", "teff_gspphot", "teff_gspphot_lower", "teff_gspphot_upper",
               "logg_gspphot", "logg_gspphot_lower", "logg_gspphot_upper", "mh_gspphot", "mh_gspphot_lower", "mh_gspphot_upper",
               "distance_gspphot", "distance_gspphot_lower", "distance_gspphot_upper", "Mg", "Mg_error", "MRp", "MRp_error",
               "Bp_minus_Rp", "Vmag", "RAdeg", "DEdeg", "RAhms", "DEdms", "Plx", "e_Plx", "distance_Plx", "pmRA", "pmDE", "BTmag",
               "VTmag", "MV", "MV_error", "MVt", "MVt_error", "B_minus_V", "BT_minus_VT"]

file = pd.read_csv("/var/lib/mysql-files/CAT1_intersection_CAT2_Mg_versus_Bp_minus_Rp.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/csv/CAT1_intersection_CAT2_Mg_versus_Bp_minus_Rp.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT1_intersection_CAT2_Mg_versus_Bp_minus_Rp.csv")

# Criando o arquivo CAT1_intersection_CAT2_MRp_versus_Bp_minus_Rp.csv

cursor.execute('''select CAT1.designation, ''' 
               '''CAT1.HIP, ''' 
               '''CAT1.HD, ''' 
               '''TRIM(CAT1.ra)+0, ''' 
               '''TRIM(CAT1.declination)+0, ''' 
               '''TRIM(CAT1.parallax)+0, ''' 
               '''TRIM(CAT1.parallax_error)+0, '''
               '''TRIM(CAT1.pm)+0, ''' 
               '''TRIM(CAT1.pmra)+0, '''
               '''TRIM(CAT1.pmdec)+0, '''
               '''TRIM(CAT1.ruwe)+0, '''
               '''TRIM(CAT1.phot_g_mean_mag)+0, ''' 
               '''TRIM(CAT1.phot_bp_mean_mag)+0, ''' 
               '''TRIM(CAT1.phot_rp_mean_mag)+0, '''
               '''TRIM(CAT1.teff_gspphot)+0, ''' 
               '''TRIM(CAT1.teff_gspphot_lower)+0, ''' 
               '''TRIM(CAT1.teff_gspphot_upper)+0, ''' 
               '''TRIM(CAT1.logg_gspphot)+0, ''' 
               '''TRIM(CAT1.logg_gspphot_lower)+0, ''' 
               '''TRIM(CAT1.logg_gspphot_upper)+0, ''' 
               '''TRIM(CAT1.mh_gspphot)+0, '''
               '''TRIM(CAT1.mh_gspphot_lower)+0, ''' 
               '''TRIM(CAT1.mh_gspphot_upper)+0, ''' 
               '''TRIM(CAT1.distance_gspphot)+0, '''
               '''TRIM(CAT1.distance_gspphot_lower)+0, '''
               '''TRIM(CAT1.distance_gspphot_upper)+0, '''
               '''TRIM(CAT1_product.Mg)+0, ''' 
               '''TRIM(CAT1_product.Mg_error)+0, '''
               '''TRIM(CAT1_product.MRp)+0, '''
               '''TRIM(CAT1_product.MRp_error)+0, '''
               '''TRIM(CAT1_product.Bp_minus_Rp)+0, '''
               '''TRIM(CAT2.Vmag)+0, ''' 
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, ''' 
               '''CAT2.DEdms, ''' 
               '''TRIM(CAT2.Plx)+0, ''' 
               '''TRIM(CAT2.e_Plx)+0, ''' 
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, ''' 
               '''TRIM(CAT2.pmDE)+0, ''' 
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, ''' 
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 ''' 
               '''from CAT1, CAT1_product, CAT2, CAT2_product '''
               '''where CAT1.designation = CAT1_product.designation and '''
               '''CAT1.HIP = CAT2.HIP and CAT2.HIP = CAT2_product.HIP and '''
               '''CAT1_product.MRp is not null and '''
               '''CAT1_product.Bp_minus_Rp is not null '''
               '''order by CAT1.parallax ASC '''
               '''into outfile '/var/lib/mysql-files/CAT1_intersection_CAT2_MRp_versus_Bp_minus_Rp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["designation", "HIP", "HD", "ra", "declination", "parallax", "parallax_error", "pm", "pmra", "pmdec", "ruwe",
               "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag", "teff_gspphot", "teff_gspphot_lower", "teff_gspphot_upper",
               "logg_gspphot", "logg_gspphot_lower", "logg_gspphot_upper", "mh_gspphot", "mh_gspphot_lower", "mh_gspphot_upper",
               "distance_gspphot", "distance_gspphot_lower", "distance_gspphot_upper", "Mg", "Mg_error", "MRp", "MRp_error",
               "Bp_minus_Rp", "Vmag", "RAdeg", "DEdeg", "RAhms", "DEdms", "Plx", "e_Plx", "distance_Plx", "pmRA", "pmDE", "BTmag",
               "VTmag", "MV", "MV_error", "MVt", "MVt_error", "B_minus_V", "BT_minus_VT"]

file = pd.read_csv("/var/lib/mysql-files/CAT1_intersection_CAT2_MRp_versus_Bp_minus_Rp.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/csv/CAT1_intersection_CAT2_MRp_versus_Bp_minus_Rp.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT1_intersection_CAT2_MRp_versus_Bp_minus_Rp.csv")

# Criando o arquivo CAT1_intersection_CAT2_MV_versus_B_minus_V.csv

cursor.execute('''select CAT1.designation, '''
               '''CAT1.HIP, '''
               '''CAT1.HD, '''
               '''TRIM(CAT1.ra)+0, '''
               '''TRIM(CAT1.declination)+0, '''
               '''TRIM(CAT1.parallax)+0, '''
               '''TRIM(CAT1.parallax_error)+0, '''
               '''TRIM(CAT1.pm)+0, '''
               '''TRIM(CAT1.pmra)+0, '''
               '''TRIM(CAT1.pmdec)+0, '''
               '''TRIM(CAT1.ruwe)+0, '''
               '''TRIM(CAT1.phot_g_mean_mag)+0, '''
               '''TRIM(CAT1.phot_bp_mean_mag)+0, '''
               '''TRIM(CAT1.phot_rp_mean_mag)+0, '''
               '''TRIM(CAT1.teff_gspphot)+0, '''
               '''TRIM(CAT1.teff_gspphot_lower)+0, '''
               '''TRIM(CAT1.teff_gspphot_upper)+0, '''
               '''TRIM(CAT1.logg_gspphot)+0, '''
               '''TRIM(CAT1.logg_gspphot_lower)+0, '''
               '''TRIM(CAT1.logg_gspphot_upper)+0, '''
               '''TRIM(CAT1.mh_gspphot)+0, '''
               '''TRIM(CAT1.mh_gspphot_lower)+0, '''
               '''TRIM(CAT1.mh_gspphot_upper)+0, '''
               '''TRIM(CAT1.distance_gspphot)+0, '''
               '''TRIM(CAT1.distance_gspphot_lower)+0, '''
               '''TRIM(CAT1.distance_gspphot_upper)+0, '''
               '''TRIM(CAT1_product.Mg)+0, '''
               '''TRIM(CAT1_product.Mg_error)+0, '''
               '''TRIM(CAT1_product.MRp)+0, '''
               '''TRIM(CAT1_product.MRp_error)+0, '''
               '''TRIM(CAT1_product.Bp_minus_Rp)+0, '''
               '''TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, '''
               '''CAT2.DEdms, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, '''
               '''TRIM(CAT2.pmDE)+0, '''
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 '''
               '''from CAT1, CAT1_product, CAT2, CAT2_product '''
               '''where CAT1.designation = CAT1_product.designation and '''
               '''CAT1.HIP = CAT2.HIP and CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MV is not NULL and '''
               '''CAT2_product.B_minus_V is not NULL '''
               '''order by CAT1.parallax ASC '''
               '''into outfile '/var/lib/mysql-files/CAT1_intersection_CAT2_MV_versus_B_minus_V_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["designation", "HIP", "HD", "ra", "declination", "parallax", "parallax_error", "pm", "pmra", "pmdec", "ruwe",
               "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag", "teff_gspphot", "teff_gspphot_lower", "teff_gspphot_upper",
               "logg_gspphot", "logg_gspphot_lower", "logg_gspphot_upper", "mh_gspphot", "mh_gspphot_lower", "mh_gspphot_upper",
               "distance_gspphot", "distance_gspphot_lower", "distance_gspphot_upper", "Mg", "Mg_error", "MRp", "MRp_error",
               "Bp_minus_Rp", "Vmag", "RAdeg", "DEdeg", "RAhms", "DEdms", "Plx", "e_Plx", "distance_Plx", "pmRA", "pmDE", "BTmag",
               "VTmag", "MV", "MV_error", "MVt", "MVt_error", "B_minus_V", "BT_minus_VT"]
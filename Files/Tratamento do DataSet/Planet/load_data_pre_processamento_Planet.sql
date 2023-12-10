load data local infile '/home/h/Área de trabalho/Catalogo_GAIA/Files/Tratamento do DataSet/Planet/exoplanet.eu_catalog.csv'
    into table Planet
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\r\n'
    ignore 1 rows
    (@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8, @col9, @col10, @col11, @col12, @col13, @col14, @col15, @col16, @col17, @col18, @col19, @col20, @col21, @col22, @col23, @col24, @col25, @col26, @col27, @col28, @col29, @col30, @col31, @col32, @col33, @col34, @col35, @col36, @col37, @col38, @col39, @col40, @col41, @col42, @col43, @col44, @col45, @col46, @col47, @col48, @col49, @col50, @col51, @col52, @col53, @col54, @col55, @col56, @col57, @col58, @col59, @col60, @col61, @col62, @col63, @col64, @col65, @col66, @col67, @col68, @col69, @col70, @col71, @col72, @col73, @col74, @col75, @col76, @col77, @col78, @col79, @col80, @col81, @col82, @col83, @col84, @col85, @col86, @col87, @col88, @col89, @col90, @col91, @col92, @col93, @col94, @col95, @col96, @col97, @col98) 
	set 
	name=@col1,
	mass=@col3,
	star_name=@col69,
	orbital_period=@col12,
	semi_major_axis=@col15,
	discovered=@col25,
	right_ascension=@col70,
	declination=@col71
;

load data local infile '/home/h/Área de trabalho/Catalogo_GAIA/Files/Tratamento do DataSet/Star/HIP_MAIN.DAT'
    into table Star_Hipparcos
    fields terminated by '|'
    enclosed by '"'
    escaped by '"'
    lines terminated by '\r\r'
    (@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8, @col9, @col10, @col11, @col12, @col13, @col14, @col15, @col16, @col17, @col18, @col19, @col20, @col21, @col22, @col23, @col24, @col25, @col26, @col27, @col28, @col29, @col30, @col31, @col32, @col33, @col34, @col35, @col36, @col37, @col38, @col39, @col40, @col41, @col42, @col43, @col44, @col45, @col46, @col47, @col48, @col49, @col50, @col51, @col52, @col53, @col54, @col55, @col56, @col57, @col58, @col59, @col60, @col61, @col62, @col63, @col64, @col65, @col66, @col67, @col68, @col69, @col70, @col71, @col72, @col73, @col74, @col75, @col76, @col77, @col78) set HIP=@col2, Vmag=@col6, RAdeg=@col9, DEdeg=@col10, Plx=@col12, pmRA=@col13, pmDE=@col14, e_Plx=@cpl17, BTmag=@col33, e_BTmag=@col34, VTmag=@col35, e_VTmag=@col36, B_V=@col38, e_B_V=@col39;





load data local infile '/home/h/Área de trabalho/Catalogo_GAIA/Files/Tratamento do DataSet/Star/1701635903850O-result.csv'
    into table Star_Gaia
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 rows
    (@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8, @col9, @col10, @col11, @col12, @col13, @col14, @col15, @col16, @col17, @col18, @col19, @col20, @col21) 
	set 
	designation=@col1,
	ra=@col2,
	declination=@col3,
	parallax=@col4,
	parallax_error=@col5,
	ruwe=@col6,
	phot_g_mean_mag=@col7,
	phot_bp_mean_mag=@col8,
	phot_rp_mean_mag=@col9,
	teff_gspphot=@col10,
	teff_gspphot_lower=@col11,
	teff_gspphot_upper=@col12,
	logg_gspphot=@col13,
	logg_gspphot_lower=@col14, 
	logg_gspphot_upper=@col15,
	mh_gspphot=@col16,
	mh_gspphot_lower=@col17,
	mh_gspphot_upper=@col18,
	distance_gspphot=@col19,
	distance_gspphot_lower=@col20,
	distance_gspphot_upper=@col21
;
	
	
	

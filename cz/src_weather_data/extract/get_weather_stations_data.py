from weather_data_downloader import downloader

base_url = 'https://www.chmi.cz/files/portal/docs/meteo/ok/open_data/RDATA'
dest_path = '../stations_raw_data'
metric_file_path = '../metrics.txt'
region_file_path = '../regions.txt'
station_file_path = '../weather_station_list_cz.txt'
sleep_time = 1  #in seconds

#get the list of metrics from the file
with open(metric_file_path) as metric_file:
    metrics = [metric.rstrip() for metric in metric_file]

#get the list of regions from the file
with open(region_file_path) as region_file:
    regions = [region.rstrip() for region in region_file]

#get the list of weather stations from the file
with open(station_file_path) as station_file:
    stations = [station.rstrip() for station in station_file]

#call the download function
for metric in metrics:
    for region in regions:
        for station in stations:
            downloader(base_url,metric,region,station,dest_path,sleep_time)


#
#
# ## prumerna teplota
# https://www.chmi.cz/files/portal/docs/meteo/ok/open_data/RDATA/T/Pardubicky/H2ZAMB01_T_N.csv.zip
#
# ## maximalni teplota
# https://www.chmi.cz/files/portal/docs/meteo/ok/open_data/RDATA/TMA/Jihocesky/C1BLAT01_TMA_N.csv.zip
#
# ## minimalni teplota
# https://www.chmi.cz/files/portal/docs/meteo/ok/open_data/RDATA/TMI/Praha/P1PKLE01_TMI_N.csv.zip
#
# ## denni uhrn srazek
# https://www.chmi.cz/files/portal/docs/meteo/ok/open_data/RDATA/SRA/Praha/P1PCHO01_SRA_N.csv.zip
#
# ## vyska nove napadleho snehu
# https://www.chmi.cz/files/portal/docs/meteo/ok/open_data/RDATA/SNO/Karlovarsky/L2TSEK01_SNO_N.csv.zip
#
# ## celkova vyska snehove pokryvky
# https://www.chmi.cz/files/portal/docs/meteo/ok/open_data/RDATA/SCE/Vysocina/B2BRTN01_SCE_N.csv.zip

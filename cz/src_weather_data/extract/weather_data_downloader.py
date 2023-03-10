import requests
import time

def downloader(url_base,metric,region,station,dest_path,sleep_time):
    #url_base - first path of the URL which is common for all requests
    #metric - type of the weather metric needed for the URL and file name
        #T - temperature (average)
        #TMA - temperature (max)
        #TMI - temperature (min)
        #SRA - precipitation
        #SNO - new snow height
        #SCE - total snow cover height
    #region - needed for the URL
    #station - weather station ID
    #dest_pat - path where the file will be saved
    url = url_base + '/' + metric + '/' + region +'/' + station + '_' + metric + '_N.csv.zip'
    r = requests.get(url, allow_redirects=True)

    # check the status_code - if 200 requested file exists and will be written to the specified path
    if r.status_code == 200:
        open(dest_path + '/' + station + '_' + metric + '_N.csv.zip', 'wb').write(r.content)
        print(dest_path + '/' + station + '_' + metric + '_N.csv.zip downloaded')
    time.sleep(sleep_time)

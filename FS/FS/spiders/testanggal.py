from datetime import datetime, timedelta

tanggal_yang_diambil = datetime.strftime(datetime.now() - timedelta(2), '%Y/%m/%d')
j = "6"
kode = "DPS"

api = '/v2/api-next/flight-tracker/dep/'+kode+'/'+tanggal_yang_diambil+'/'+j+'?carrierCode=&numHours=6'

print(api)
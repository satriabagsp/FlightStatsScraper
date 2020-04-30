# -*- coding: utf-8 -*-
import scrapy
import mysql.connector
import http.client
import mimetypes
import json
import time
from FS.items import Info
import socket
from datetime import datetime, timedelta

socket.getaddrinfo('localhost', 8080)
class FlightstatusdepSpider(scrapy.Spider):
    name = 'flightstatusdep'

    #Ambil Link
    tanggal_yang_diambil = datetime.strftime(datetime.now() - timedelta(1), '%Y/%m/%d')
    jam = {'0','6','12','18'}
    kodeBandara = ('CGK','KNO','SUB','UPG','DPS','JOG','BPN','HLP','BTH','PLM','SRG','BDO','PNK','LOP','PKU')
    start_urls = []
    for kode in kodeBandara:
        for j in jam:
            conn = http.client.HTTPSConnection("www.flightstats.com")
            payload = ''
            headers = {}
            api = '/v2/api-next/flight-tracker/dep/'+kode+'/'+tanggal_yang_diambil+'/'+j+'?carrierCode=&numHours=6'
            conn.request("GET", api, payload, headers)
            res = conn.getresponse()
            data = res.read()
            jsonnya = data.decode("utf-8") #ini dalam bentuk string
            jsonJadi = (json.loads(jsonnya)) #ini jsonnya jadinya bos
            data = jsonJadi['data']['flights']

            for url in data:
                link = 'https://www.flightstats.com/v2'+url['url']
                start_urls.append(link)

            def parse(self, response):
                #konek db
                mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "",
                    database = "flightstatus"
                )
                mycursor = mydb.cursor()
                tanggal = datetime.date(datetime.now())
                test = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[1]/text()').get()
                if test is not None:
                    link_url = response.request.url
                    id_penerbangan = link_url[-10:]
                    id_pesawat = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[1]/text()').get()
                    nama_pesawat = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/text()').get()
                    asal_bandara = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/text()').get()
                    asal_negara = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/text()').get()
                    tujuan_bandara = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/text()').get()
                    tujuan_negara = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/text()').get()
                    tanggal_keberangkatan = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/text()').get()
                    jam_keberangkatan = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/text()').get()
                    tanggal_kedatangan = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/text()').get()
                    jam_kedatangan = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/text()').get()
                    status = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/text()').get()
                    status2 = response.xpath('/html/body/div[1]/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[2]/text()').get()
                elif test is None:
                    link_url = response.request.url
                    id_penerbangan = link_url[-10:]
                    id_pesawat = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[1]/text()').get()
                    nama_pesawat = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/text()').get()
                    asal_bandara = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/text()').get()
                    asal_negara = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/text()').get()
                    tujuan_bandara = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/text()').get()
                    tujuan_negara = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/text()').get()
                    tanggal_keberangkatan = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/text()').get()
                    jam_keberangkatan = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/text()').get()
                    tanggal_kedatangan = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/text()').get()
                    jam_kedatangan = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/text()').get()
                    status = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/text()').get()
                    status2 = response.xpath('/html/body/div[1]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[2]/text()').get()
                
                #Masukin ke DB
                sql = "INSERT departure VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE status=%s, status_add=%s, keberangkatan_tanggal=%s, keberangkatan_jam=%s, kedatangan_tanggal=%s, kedatangan_jam=%s, waktu_extract=%s"
                baris = (
                    id_penerbangan,
                    id_pesawat, 
                    nama_pesawat, 
                    asal_bandara,
                    asal_negara,
                    tujuan_bandara,
                    tujuan_negara,
                    status, 
                    status2,
                    tanggal_keberangkatan,
                    jam_keberangkatan,
                    tanggal_kedatangan,
                    jam_kedatangan,
                    datetime.date(datetime.now()),
                    status, 
                    status2,
                    tanggal_keberangkatan,
                    jam_keberangkatan,
                    tanggal_kedatangan,
                    jam_kedatangan,
                    datetime.date(datetime.now())
                )

                mycursor.execute(sql, baris)
                mydb.commit()


                # return Info(id_penerbangan=id_penerbangan,
                #     id_pesawat=id_pesawat, 
                #     nama_pesawat=nama_pesawat, 
                #     asal_bandara=asal_bandara,
                #     asal_negara=asal_negara,
                #     tujuan_bandara=tujuan_bandara,
                #     tujuan_negara=tujuan_negara,
                #     tanggal_keberangkatan=tanggal_keberangkatan,
                #     jam_keberangkatan=jam_keberangkatan,
                #     tanggal_kedatangan=tanggal_kedatangan,
                #     jam_kedatangan=jam_kedatangan,
                #     status=status, 
                #     status2=status2,
                #     waktu_scrape=datetime.date(datetime.now()))






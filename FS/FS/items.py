# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class FsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Info(scrapy.Item):
    # define the fields for your item here like:
    id_penerbangan = Field()
    id_pesawat = Field()
    nama_pesawat = Field()
    asal_bandara = Field()
    asal_negara = Field()
    tujuan_bandara = Field()
    tujuan_negara = Field()
    tanggal_keberangkatan = Field()
    jam_keberangkatan = Field()
    tanggal_kedatangan = Field()
    jam_kedatangan = Field()
    status = Field()
    status2 = Field()
    waktu_scrape = Field()
    pass
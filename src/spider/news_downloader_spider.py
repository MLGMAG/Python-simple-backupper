import scrapy
import os

# scrapy crawl news_downloader

RESOURCES_DIR = './resources'

class NewsSpider(scrapy.Spider):
    name = "news_downloader"
    start_urls = [
        'https://lb.ua/news/2024/02/16/598712_ministerka_zakordonnih_sprav.html',
        'https://lb.ua/news/2024/02/16/598718_italiya_skliche_pershiy_tsogorich_samit.html',
        'https://lb.ua/news/2024/02/16/598721_informator_fbr_obbrehav_sina.html',
        'https://lb.ua/news/2024/02/16/598724_oon_provede_zasidannya_genasamblei.html',
        'https://lb.ua/news/2024/02/16/598725_uryad_rishi_sunaka_dopustiv_retsesiyu.html',
        'https://lb.ua/news/2024/02/16/598730_predstavnik_derzhdepu_zaproshuvati.html',
        'https://lb.ua/news/2024/02/16/598732_palata_predstavnikiv_ssha_pishla.html',
        'https://lb.ua/news/2024/02/16/598736_prezident_i_premier_polshchi_berezni.html',
        'https://lb.ua/news/2024/02/16/598738_senat_kanadi_nabliziv_ratifikatsiyu.html',
        'https://lb.ua/news/2024/02/16/598741_provalna_repetitsiya_sunaka.html',
        'https://lb.ua/news/2024/02/16/598825_chlenstvo_nato_iedina_nadiyna.html',
        'https://lb.ua/news/2024/02/16/598831_kabmin_pogodiv_priznachennya_sergiya.html',
        'https://lb.ua/news/2024/02/16/598839_ochevidno_vin_ubitiy_putinim-.html',
        'https://lb.ua/news/2024/02/16/598846_mzs_nazvalo_nepriynyatnimi.html',
        'https://lb.ua/news/2024/02/16/598852_zelenskiy_i_prezident_nimechchini.html',
        'https://lb.ua/news/2024/02/16/598867_zelenskiy_pribuv_parizha.html',
        'https://lb.ua/news/2024/02/16/598878_ukraina_pidpisala_dvostoronnyu_ugodu.html'
    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = f'{RESOURCES_DIR}/{page}'

        if not os.path.exists(RESOURCES_DIR):
            os.mkdir(RESOURCES_DIR)

        with open(filename, 'wb') as f:
            f.write(response.body)


import time

import scrapy as scrapy
from scrapy_splash import SplashRequest
from DOU_HTML.model import dou_licitacao
from DOU_HTML.service import dou_service


class DOUSpider(scrapy.Spider):
    name = "DOU"

    def start_requests(self):
        urls = [
            'http://www.in.gov.br/leiturajornal?secao=dou3&data=15-08-2019&ato=Aviso%20de%20Licita%C3%A7%C3%A3o'
        ]
        for url in urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5})

    def parse(self, response):
        new_urls = response.css("ul.ul-materias li a::attr(href)").getall()
        for new_url in new_urls:
            yield SplashRequest("http://www.in.gov.br" + new_url,
                                self.carrega_obj,
                                endpoint='render.html',
                                args={'wait': 0.5})
            time.sleep(3)

    @staticmethod
    def carrega_obj(response):
        header = response.css("div.detalhes-dou p span::text").getall()
        titulos = (response.css("div.texto-dou p.identifica::text").getall())
        corpo = (response.css("div.texto-dou p.dou-paragraph::text").getall())
        publicador = (response.css("div.texto-dou p.assina::text").getall())
        publicador.append(response.css("div.texto-dou p.cargo::text").get())
        objeto = dou_licitacao.DouLicitacao(header, titulos, corpo, publicador)
        print(objeto.to_json())
        dou_service.salva_obj(objeto, "licitacoes")

import time

import scrapy as scrapy
from DOU_HTML.model import dou_licitacao
from DOU_HTML.service import dou_service
from scrapy_splash import SplashRequest


class DOUSpider(scrapy.Spider):
    # Definicao do nome da Spider, utilizado durante a chamada do Framework via linha de comando
    name = "DOU"

    # Metodo basico da ckasse scrapy.Spider, invocado durante a coleta
    def start_requests(self):
        # Definicao das URLs a serem navegadas pela Spider
        urls = [
            'http://www.in.gov.br/leiturajornal?secao=dou3&data=01-08-2019&ato=Aviso%20de%20Licita%C3%A7%C3%A3o'
        ]
        for url in urls:
            # Cada uma das URLs acaba sendo enviada para uma requisicao Splash
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5})

    def parse(self, response):
        # O seletor abaixo retorna a lista das licitacoes disponiveis na primeira pagina
        new_urls = response.css("ul.ul-materias li a::attr(href)").getall()
        # Para cada uma das licitacoes, uma nova requisicao Splash incia
        for new_url in new_urls:
            yield SplashRequest("http://www.in.gov.br" + new_url,
                                self.carrega_obj,
                                endpoint='render.html',
                                args={'wait': 0.5})
            time.sleep(3)

    @staticmethod
    def carrega_obj(response):
        # Seletor que busca as inforacoes de header da pagina
        header = response.css("div.detalhes-dou p span::text").getall()
        # Seletor que busca titulo e subtitulo da pagina
        titulos = (response.css("div.texto-dou p.identifica::text").getall())
        # Seletor para buscar o texto corpo da pagina, onde constam as informacoes das licitacoes
        corpo = (response.css("div.texto-dou p.dou-paragraph::text").getall())
        # Seletores que busca informacoes do nome do publicador
        publicador = (response.css("div.texto-dou p.assina::text").getall())
        publicador.append(response.css("div.texto-dou p.cargo::text").get())
        # Criacao do objeto que
        objeto = dou_licitacao.DouLicitacao(header, titulos, corpo, publicador)
        # Funcao que salva o objeto no banco NoSQL
        dou_service.salva_obj(objeto, "licitacoes")

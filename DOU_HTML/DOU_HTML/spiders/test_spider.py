import scrapy as scrapy
from scrapy_splash import SplashRequest


class TestSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = [
            'http://www.in.gov.br/leiturajornal?secao=dou3&data=30-08-2019&ato=Aviso%20de%20Licita%C3%A7%C3%A3o'
        ]
        for url in urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5})

    def parse(self, response):
        botoes = response.css("span.pagination-button").getall()
        botao = botoes[-1]
        botao.click()

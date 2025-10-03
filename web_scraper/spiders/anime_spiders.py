import scrapy
from datetime import datetime
from ..items import CamisetaItem 
from scrapy_playwright.page import PageMethod 
import logging

# Configuração para reduzir o ruído de logs e focar em erros críticos
logging.getLogger("scrapy_playwright").setLevel(logging.WARNING)
logging.getLogger("scrapy").setLevel(logging.INFO)

class AnimeSpiderSpider(scrapy.Spider):
    name = "anime_spider"
    allowed_domains = ["chicorei.com"]
    
    # 1. MÉTODO PARA INICIAR AS REQUISIÇÕES (Ativa o Playwright)
    def start_requests(self):
        url = "https://chicorei.com/camiseta/masculino/anime/"
        
        yield scrapy.Request(
            url,
            meta={
                "playwright": True, 
                "playwright_include_page": True,
                "playwright_page_coroutines": [
                    # Espera que o preço apareça para garantir que a página esteja renderizada
                    PageMethod("wait_for_selector", "span[itemprop='price']", timeout=10000)
                ]
            },
            callback=self.parse_listing
        )

    # 2. MÉTODO PARA RASPAGEM DA LISTA DE PRODUTOS
    async def parse_listing(self, response):
        # O seletor para o contêiner de produto
        produtos = response.css('.product-list-item') 
        
        if not produtos:
            self.logger.warning("Nenhum item encontrado. Verifique o seletor ou bloqueio.")
            return

        for produto in produtos:
            item = CamisetaItem()
            
            # Extrai o link (href) e garante que ele seja completo
            link_a = produto.css('a::attr(href)').get()
            item['link_produto'] = response.urljoin(link_a) if link_a else None
            
            # Extrai o nome/título e limpa espaços
            nome_raw = produto.css('.product-list-item-title::text').get()
            item['nome_produto'] = nome_raw.strip() if nome_raw else None
            
            # Extrai o preço (direto do atributo content, limpo)
            item['preco_atual'] = produto.css('span[itemprop="price"]::attr(content)').get()
            
            # Marca a data da raspagem
            item['data_raspagem'] = datetime.now()

            # Envia para o parse_detail para pegar as cores e imagens
            if item.get('link_produto'):
                yield scrapy.Request(
                    url=item['link_produto'],
                    # Ativa o Playwright novamente, caso a página de detalhe seja dinâmica
                    meta={"playwright": True, "item": item}, 
                    callback=self.parse_detail
                )

    # 3. MÉTODO PARA RASPAGEM DA PÁGINA DE DETALHES (Cores e Imagem)
    async def parse_detail(self, response):
            item = response.meta['item']
            
            # Mapeamento de RGB para Nome de Cor
            # NOTA: O código HTML fornece 'rgb(r, g, b)', então o mapeamento deve ser formatado
            rgb_to_nome = {
                "rgb(0, 0, 0)": "Preto Noir",
                "rgb(255, 255, 255)": "Branco Cannoli",
                "rgb(69, 84, 145)": "Azul Surf",
                "rgb(179, 181, 183)": "Mescla Gaivota",
                "rgb(234, 185, 57)": "Amarelo Manga",
                "rgb(103, 71, 63)": "Marrom Sucupira",
                "rgb(244, 243, 210)": "Bege Baunilha",
                "rgb(177, 70, 78)": "Vermelho Goiaba",
                "rgb(121, 166, 117)": "Verde Sálvia",
                "rgb(190, 138, 54)": "Amarelo Âmbar"
            }
            
            # 1. LINK DA IMAGEM: Seletor validado
            item['link_imagem'] = response.css('div.image-zoom-placeholder img::attr(src)').get()
            
            # 2. CORES: Extração do RGB via atributo STYLE
            cores_raw_style = response.css('div.product-color-option::attr(style)').getall()
            cores_encontradas = []

            for style_string in cores_raw_style:
                # 1. Isola a string RGB: procura "rgb(x, y, z)"
                if 'background-color:' in style_string:
                    # Extrai o código RGB (Ex: "rgb(0, 0, 0)")
                    rgb_code = style_string.split('background-color:')[1].split(';')[0].strip()
                    
                    # 2. Converte o RGB para o nome da cor (usando o mapeamento)
                    # Se a cor estiver no dicionário, usa o nome. Caso contrário, usa o código RGB original.
                    nome_da_cor = rgb_to_nome.get(rgb_code, f"RGB:{rgb_code}") 
                    cores_encontradas.append(nome_da_cor)
            
            item['cor_disponivel'] = cores_encontradas
            
            # Retorna o item COMPLETO para o Pipeline
            yield item
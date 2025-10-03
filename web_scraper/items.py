# Define here the models for your scraped items
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose 
import re

# Função auxiliar para extrair e converter o preço
# Função para garantir que o preço seja float (ponto decimal)
def parse_price(value):
    str_value = str(value) 
    
    # 1. Se houver vírgula, troca por ponto (ex: '39,90' -> '39.90')
    str_value = str_value.replace(',', '.') 
    
    # 2. Tenta converter para float.
    try:
        # Arredonda para 2 casas decimais para evitar problemas de float.
        return round(float(str_value), 2)
    except ValueError:
        return None 

class CamisetaItem(scrapy.Item):
    # ... outros campos ...
    
    preco_atual = scrapy.Field(
        # Aplica a função parse_price para garantir a conversão para float
        input_processor=MapCompose(parse_price),
        output_processor=TakeFirst()
    )


class CamisetaItem(scrapy.Item):
    """
    Define os campos para um item de camiseta raspado.
    """
    # Campos simples com TakeFirst (retorna o primeiro valor de uma lista)
    nome_produto = scrapy.Field(
        output_processor=TakeFirst()
    )
    link_produto = scrapy.Field(
        output_processor=TakeFirst()
    )
    link_imagem = scrapy.Field(
        output_processor=TakeFirst()
    )
    data_raspagem = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    # Campo que é uma lista (não usa TakeFirst)
    cor_disponivel = scrapy.Field()
    
    # Campo com MapCompose e TakeFirst para processamento de preço
    preco_atual = scrapy.Field(
        # Aplica a função parse_price a cada valor,
        # esperando que a extração do atributo 'content' já tenha sido feita
        input_processor=MapCompose(parse_price),
        # Pega o primeiro valor processado (que deve ser um float ou None)
        output_processor=TakeFirst()
    )
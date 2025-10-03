# Define here the models for your scraped items
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose 
import re

# Função auxiliar para extrair e converter o preço
def parse_price(value):
    """
    Extrai o valor numérico de uma string de preço (geralmente de um atributo content)
    e o converte para float.
    Exemplo: 'R$ 1.234,56' -> 1234.56
    """
    if isinstance(value, str):
        # Encontra o padrão de preço (pode conter R$, cifras, espaços, pontos, vírgulas)
        # e remove tudo que não for dígito ou separador decimal (vírgula/ponto)
        # A expressão regular simplificada foca em números e separadores
        cleaned_value = re.sub(r'[^\d,.]', '', value)

        # Trata o formato brasileiro (vírgula como separador decimal)
        if ',' in cleaned_value and '.' in cleaned_value:
            # Caso raro onde pode ter ambos, assume-se o ponto como separador de milhar
            # e a vírgula como separador decimal (padrão brasileiro).
            cleaned_value = cleaned_value.replace('.', '')
            cleaned_value = cleaned_value.replace(',', '.')
        elif ',' in cleaned_value:
            # Apenas vírgula, assume-se separador decimal
            cleaned_value = cleaned_value.replace(',', '.')
        try:
            return float(cleaned_value)
        except ValueError:
            return None
    return value


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
import csv
from datetime import datetime

class CsvExportPipeline:

    def __init__(self):
        # Abre o arquivo CSV para escrita. Usamos 'a' para adicionar no final.
        # newline='' evita linhas em branco.
        self.file = open('chicorei_anime.csv', 'a', newline='', encoding='utf-8')
        # Cria o objeto que vai escrever no CSV
        self.writer = csv.writer(self.file)
        # Controla se o cabeçalho já foi escrito
        self.headers_written = False

    def process_item(self, item, spider):
        # Converte o item para um dicionário
        data = dict(item)
        
        # Escreve o cabeçalho (nomes das colunas) apenas uma vez
        if not self.headers_written:
            self.writer.writerow(data.keys())
            self.headers_written = True
        
        # Escreve os valores do item (a linha de dados)
        # O Playwright pode retornar strings vazias ou None, precisamos tratar:
        row = [str(v) if v is not None else "" for v in data.values()]
        self.writer.writerow(row)
        
        return item

    def close_spider(self, spider):
        # Fecha o arquivo quando o spider termina
        self.file.close()
# Scrapy settings for web_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# =================================================================
# CONFIGURAÇÕES DO PLAYWRIGHT (PARA LIDAR COM JAVASCRIPT)
# =================================================================

# 1. Habilita o Playwright como o novo manipulador de downloads
# Ele intercepta as requisições HTTP e HTTPS.
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# 2. Roda o navegador em modo "headless"
PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": True}

# 3. (Ajuste de performance) Reduza as requisições simultâneas
CONCURRENT_REQUESTS = 4

# Define o nome do bot e seus módulos
BOT_NAME = "web_scraper" 

SPIDER_MODULES = ["web_scraper.spiders"]
NEWSPIDER_MODULE = "web_scraper.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "web_scraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "web_scraper.middlewares.WebScraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "web_scraper.middlewares.WebScraperDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# Ativação do Pipeline de Exportação para CSV
ITEM_PIPELINES = {
    'web_scraper.pipelines.CsvExportPipeline': 300, 
    # O número 300 indica a ordem de execução (menor número roda primeiro)
}
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
# Adicione esta linha: Define o ponto e vírgula como separador de colunas padrão
FEED_EXPORT_FIELDS = ['nome_produto', 'link_produto', 'preco_atual', 'link_imagem', 'cor_disponivel', 'data_raspagem']
FEED_EXPORT_ITEM_FIELDS = FEED_EXPORT_FIELDS
FEED_EXPORT_SEPARATOR = ';'

#New code
# --- Configurações de Cortesia e Identificação ---

# 1. Respeitar o robots.txt
ROBOTSTXT_OBEY = True

# 2. Atraso de 1 segundo entre requisições (Download Delay)
# Isso faz com que o Scrapy espere 1 segundo antes de fazer a próxima requisição.
DOWNLOAD_DELAY = 1

# 3. Desativar o uso de cookies
# Isso evita que o robô mantenha sessões persistentes no servidor de destino.
COOKIES_ENABLED = False

# 4. USER_AGENT que simule um navegador Chrome moderno
# Substitua o valor pelo USER_AGENT atualizado de um navegador Chrome.
# O valor abaixo é um exemplo que simula um Chrome em um sistema Windows.
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

# --- Configurações de Concorrência (Relacionado ao Atraso) ---

# Limita o número de requisições simultâneas para o mesmo domínio
# Recomendado em conjunto com DOWNLOAD_DELAY
CONCURRENT_REQUESTS_PER_DOMAIN = 8
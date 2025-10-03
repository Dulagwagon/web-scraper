# 👕 [Web Scraper] Monitoramento de E-commerce: Chico Rei (Anime)

Este projeto é um **Web Scraper** escalável construído com o framework **Scrapy** em Python. O objetivo principal é extrair dados de produtos (preços, links, cores) do e-commerce Chico Rei, superando desafios de carregamento de conteúdo dinâmico (JavaScript).

## 🚀 Soluções Técnicas e Tecnologias

Este projeto demonstra domínio das seguintes habilidades:

* **Web Scraping Avançado:** Utilização do framework **Scrapy** para estruturação do *crawler*.
* **Renderização de JavaScript:** Integração com **Scrapy-Playwright** para renderizar o conteúdo dinâmico (componentes de produto e variações de cor), garantindo a coleta de dados que não estão no HTML estático.
* **Persistência de Dados:** Implementação de um **Pipeline** customizado para salvar os dados em um banco de dados **SQLite** (`chicorei_data.db`), em vez de apenas arquivos CSV.
* **Tratamento e Mapeamento de Dados:** Engenharia de código para extrair e mapear códigos **RGB** para nomes de cores legíveis (ex: `rgb(0, 0, 0)` -> `Preto Noir`).

## 🛠️ Como Rodar o Projeto Localmente

1.  **Clone o Repositório:**
    ```bash
    git clone [https://docs.github.com/pt/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github](https://docs.github.com/pt/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
    cd web_scraper
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate # Use '.\venv\Scripts\Activate' no Windows
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install scrapy scrapy-playwright
    playwright install
    ```

4.  **Execute o Crawler (O Scraper):**
    ```bash
    python -m scrapy crawl anime_spider
    ```
    Após a execução, o banco de dados `chicorei_data.db` será criado/atualizado com os dados coletados.

## ✨ Próximas Melhorias (Escalabilidade Futura)

Para futuras iterações e demonstração de valor, o projeto pode ser expandido com:

1.  **Análise de Dados:** Adicionar um script Python (usando Pandas) para gerar gráficos de popularidade de cor e histórico de preços.
2.  **Automação:** Configurar agendamento diário via **Scrapyd** ou **AP Scheduler** para monitoramento contínuo de preços.
3.  **API:** Criar uma API simples (usando Flask ou FastAPI) para expor os dados do SQLite.
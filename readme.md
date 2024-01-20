# Music Organizer 🎶

Um aplicativo Django para organizar e gerenciar informações sobre artistas, músicas e playlists.

[![Build Status](https://travis-ci.com/seu-usuario/nome-do-repositorio.svg?branch=main)](https://travis-ci.com/seu-usuario/nome-do-repositorio)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Visão Geral

O projeto Music Organizer é uma aplicação Django que oferece funcionalidades essenciais para organizar e gerenciar informações relacionadas à música. Ele inclui modelos para artistas, músicas e playlists, juntamente com endpoints de API para listar e criar esses recursos.

## Funcionalidades

- Listagem e criação de artistas.
- Listagem e criação de músicas associadas a artistas.
- Listagem e criação de playlists contendo músicas.

## Pré-requisitos

- Python 3.x
- Ambiente virtual (opcional, mas recomendado)
- [Docker](https://www.docker.com/) (para execução em contêiner)

## Instalação

### Usando Docker

1. **Construa a imagem:**

   ```bash
   docker build -t music-organizer .
   ```

2. **Execute o contêiner:**

   ```bash
   docker run -p 8000:8000 music-organizer
   ```

### Clonando o Repositório

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/thaleson/MusicOrganizer.git
    cd MusicOrganizer
    ```

2. **Configurar um ambiente virtual (opcional):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # no Windows, use venv\Scripts\activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

## Uso

1. **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

2. **Acesse o aplicativo no seu navegador:**

    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Testes

Este projeto foi testado nos seguintes sistemas operacionais:

- Windows
- macOS
- Linux

Para executar os testes, utilize o seguinte comando:

```bash
python manage.py test
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de recebimento.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
# Descer Laudo

Este projeto automatiza o tratamento de solicitações de avaliação recebidas por
email. O script lê arquivos `.eml` da pasta `Downloads` do sistema, extrai
informações importantes e cria uma estrutura de pastas para cada solicitação.
PDFs anexados são convertidos em imagens PNG e uma planilha do Google é
preenchida automaticamente com todos os dados extraídos.

## Requisitos

- Python 3.8+
- Os pacotes listados em `requeriments.txt`
- Binários do [Poppler](https://poppler.freedesktop.org/) (já incluídos em
  `Release-24.08.0-0/poppler-24.08.0`)

## Instalação

Crie um ambiente virtual (opcional) e instale as dependências:

```bash
pip install -r requeriments.txt
```

Nenhuma configuração extra do Poppler é necessária se a estrutura do repositório
for mantida, pois o caminho utilizado pelo código já aponta para
`Release-24.08.0-0/poppler-24.08.0/Library/bin`.

## Execução

Execute o script principal com Python:

```bash
python main.py
```

O aplicativo procurará o primeiro `.eml` na pasta `Downloads`, analisará seu
conteúdo e detectará o tipo de laudo (rural, urbano ou máquinas). Uma estrutura
de pastas será criada nos caminhos de rede pré-definidos e qualquer arquivo
compactado encontrado em `Downloads` será movido e extraído. Os PDFs dentro da
pasta `DOCUMENTOS` criada serão convertidos em PNG utilizando o Poppler. Por
fim, o script abre uma planilha do Google e, por meio de automação de teclado,
preenche cada linha com os dados extraídos.

## Visão geral da automação

1. **Extração do EML** – Lê o `.eml` na pasta `Downloads` e extrai nome do
   solicitante, datas, órgão, telefones e outros campos.
2. **Criação de pastas** – Monta uma estrutura de diretórios (incluindo
   subpastas para documentos, PNGs, fotos e outros) de acordo com o tipo de
   laudo detectado.
3. **Preenchimento de planilha** – Abre um link pré-configurado do Google Sheets
   e escreve os dados coletados linha por linha por meio de entrada simulada de
   teclado.

## Licença

Este projeto é distribuído sob os termos da Licença Pública Geral GNU versão 3.
A distribuição do Poppler inclusa é licenciada sob a GPLv2 ou posterior,
compatível com este projeto.

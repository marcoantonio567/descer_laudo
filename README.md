
# Descer Laudo 🚀

Automatiza o processamento de laudos recebidos por e-mail (arquivos `.eml`), organizando anexos, convertendo PDF em imagens e alimentando planilhas no Google Sheets, além de enviar resultados para servidor de rede.

## 🔧 Pré-requisitos

* **Python 3.8 ou superior**
* Pacotes Python listados em `requeriments.txt`
* Binários do Poppler (incluídos em `Release-24.08.0-0/poppler-24.08.0/Library/bin`) ([github.com][1])

## 🛠️ Instalação

```bash
git clone https://github.com/marcoantonio567/descer_laudo.git
cd descer_laudo
python -m venv venv        # opcional, mas recomendado
source venv/bin/activate   # ou `venv\Scripts\activate` no Windows
pip install -r requeriments.txt
```

## ▶️ Uso

1. Coloque os arquivos `.eml` na pasta `Downloads` do sistema.
2. Execute:

   ```bash
   python main.py
   ```
3. O script irá:

   * Ler o primeiro `.eml` da pasta Downloads.
   * Extrair informações: tipo de laudo (rural, urbano ou máquinas), dados do solicitante (nome, datas, órgão, telefones etc.).
   * Criar uma estrutura de diretórios com subpastas para documentos, imagens, fotos etc. ([github.com][1])
   * Descompactar arquivos ZIP encontrados.
   * Converter PDFs em PNGs usando os binários do Poppler.
   * Preencher um Google Sheets via automação de teclado com os dados coletados. ([github.com][1])

## 🧩 Visão geral do fluxo

1. **Extração do `.eml`**: processa o primeiro arquivo disponível em Downloads
2. **Montagem de pastas**: organiza diretórios conforme o tipo de laudo
3. **Conversão de PDF**: gera PNGs com Poppler
4. **Planilha Google**: preenche dados via GUI automation

---

## 🧪 Testes

Para testar funcionalidades específicas, confira `testes.py`. Recomenda-se criar mockups ou simular `.eml` com anexos, verificando o comportamento da pipeline completa.

## 🧱 Estrutura do projeto

* `main.py`: orquestra todo o processo
* `coordenadas.py`: lógica de extração de campos do e-mail
* `functions/`: funções utilitárias
* `images/`: imagens usadas no projeto ou geradas pelo script
* `Release-24.08.0-0/poppler-24.08.0/`: binários Poppler para conversão PDF → PNG
* `requeriments.txt`: dependências do Python
* `testes.py`: casos de teste

## 📝 Licença

Distribuído sob a licença **GPL‑3.0**. Os binários do Poppler estão sob **GPL‑2.0 ou posterior**, compatível com este projeto ([github.com][1]).

---

## ⭐ Melhorias sugeridas

* **Parâmetros configuráveis**: definir caminhos (ex: Downloads, Sheets URL) via arquivo `.env` ou `config.yaml`
* **Autenticação na API do Sheets**: migrar da automação de teclado para uso da API do Google Sheets
* **Logs e tratamento de erros**: capturar falhas e registrar eventos importantes
* **Integração contínua (CI)**: adicionar GitHub Actions para rodar `testes.py` automaticamente

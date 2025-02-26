# 📹 Analisador de Vídeos com Resumo Automático

Este projeto permite analisar vídeos do YouTube, transcrever o áudio e gerar um resumo automático utilizando modelos de Processamento de Linguagem Natural (PLN).

## 🚀 Tecnologias Utilizadas

- Python 3.13
- `pytube` para download de vídeos
- `whisper` para transcrição
- `transformers` para sumarização
- `torch` para execução dos modelos

## 📦 Instalação

Antes de começar, certifique-se de ter o Python instalado e um ambiente virtual configurado.

```bash
# Clone o repositório
git clone https://github.com/GustavoLibano/VideoAnalise.git
cd VideoAnalise

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
```

## ⚙️ Como Usar

1. **Forneça a URL do vídeo do YouTube**.
2. **O script irá baixar e transcrever o áudio**.
3. **O resumo será gerado automaticamente**.

Execute o script principal:
```bash
python app.py "URL_DO_VIDEO"
```

Exemplo:
```bash
python app.py "https://www.youtube.com/watch?v=o8du_qjduAQ"
```

## 🛠 Solução de Problemas

### Erro: `torch.OutOfMemoryError: CUDA out of memory`
Se sua GPU não tiver VRAM suficiente, rode o modelo na CPU:
```python
resumo_pipeline = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)
```

### Reduzir o consumo de memória
- Use um modelo menor: `sshleifer/distilbart-cnn-12-6`
- Diminua o `batch_size` na inferência
- Libere memória da GPU antes de rodar:
  ```python
  import torch
  torch.cuda.empty_cache()
  ```

## 📜 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

🔗 **Autor:** [Seu Nome](https://github.com/GustavoLibano)


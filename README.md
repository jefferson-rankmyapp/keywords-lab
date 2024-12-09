# Analisador de Descrições de Aplicativos

Este projeto utiliza a API da OpenAI para analisar longas descrições de aplicativos e fornecer insights estratégicos.

## Funcionalidades
- Identificação de frases temáticas, padrões e sugestões de melhorias.
- Interface gráfica com Streamlit.
- Exportação de relatórios.

## Como Rodar
1. Clone o repositório:
   ```bash
   git clone <repo_url>
   cd <repo_dir>

2. Configure o ambiente:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
3. Instale as dependências
```bash
pip install -r requirements.txt
```
4. Adicione sua chave da OpenAI no arquivo .env.
5. Execute o aplicativo:
```bash
streamlit run app.py
```



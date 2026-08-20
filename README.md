# 🏭 AuraMotors - Agente de IA para Manufatura Inteligente

> **Nota de Transparência:** Este projeto é um *case* de estudo desenvolvido para fins educacionais. Todos os dados, documentos e informações corporativas utilizados são **fictícios** e estruturados exclusivamente para simular um ambiente de manufatura inteligente.
---
## 📋 Sobre o Projeto

Agente conversacional corporativo desenvolvido para a **AuraMotors Componentes Automotivos S.A.** O sistema centraliza a base de conhecimento da fábrica, permitindo que qualquer colaborador consulte instantaneamente informações técnicas, operacionais e de gestão através de uma interface unificada na nuvem.

---

## 🛑 O Problema Operacional

A dispersão de documentos em múltiplos formatos (PDF, Word, Excel, PowerPoint, Markdown, CSV, JSON e HTML) e locais descentralizados gerava gargalos severos no chão de fábrica e nos escritórios da AuraMotors. A busca manual por manuais de robôs, planilhas de estoque ou políticas internas aumentava o tempo de parada (*downtime*) e o risco de falhas operacionais.

---

## 💡 A Solução e Arquitetura (RAG)

Para mitigar os riscos de alucinação de modelos de linguagem e garantir respostas precisas baseadas estritamente nos dados da empresa, implementamos a arquitetura **RAG (Retrieval-Augmented Generation)**. 

* **Fluxo do Sistema:** Os documentos internos são processados, indexados e consultados em tempo real pelo modelo de IA toda vez que um colaborador faz uma pergunta na interface.
* **Múltiplos Formatos Suportados:** Ingestão de dados estruturados e não estruturados (PDFs de manutenção, planilhas de suprimentos, relatórios em JSON, etc.).

---

## 📂 Arquitetura do Código e Organização de Pastas
O projeto segue uma estrutura modular e limpa para facilitar a manutenção e a escalabilidade:

```text
agente-manutencao-auramotors/
│
├── docs/                      # Documentos corporativos em vários formatos (PDF, XLSX, JSON, etc.)
├── venv/                      # Ambiente virtual Python isolado
├── .env                       # Variáveis de ambiente sensíveis (Chave da API - Ignorado pelo Git)
├── .gitignore                 # Arquivos e pastas ignorados pelo controle de versão
├── agent.py                   # Lógica principal do agente, conexão com a IA e carregamento de documentos
├── app.py                     # Interface web interativa construída com Streamlit
├── gerar_docs.py              # Script utilitário para criação/população da base documental
├── listar_modelos.py          # Script de diagnóstico para listar modelos disponíveis na conta gratuita
└── requirements.txt           # Dependências e bibliotecas do projeto
```
---

## 💬 Exemplo de Interação com o Agente
Abaixo, há uma demonstração de um caso de uso real onde o colaborador consulta o agente sobre o SLA de um fornecedor:

> **Usuário:** "Quais são os fornecedores de fixadores e seus SLAs?"
> 
> **Agente (IA):** "Com base no cadastro de fornecedores da AuraMotors, o fornecedor da categoria de Fixadores e seu respectivo SLA é:
> * **Fornecedor:** Metalúrgica Precision (ID: FORN-01)
> * **SLA de Entrega:** 3 dias"

![Evidência do Agente Rodando na Nuvem OCI](docs_auramotors/Captura%20de%20tela%202026-08-19%20232140.png)

![Evidência do Agente Rodando na Nuvem OCI](docs_auramotors/Captura%20de%20tela%202026-08-19%20232243.png)
---

## 🛠️ Stack Tecnológica e Ferramentas

* **Linguagem:** Python 3.10+
* **Interface Web:** Streamlit
* **Inteligência Artificial:** Google GenAI SDK (Google Gemini)
* **Gerenciamento de Ambiente:** `python-dotenv` para variáveis de ambiente
* **Infraestrutura e Nuvem:** Oracle Cloud Infrastructure (OCI) - Compute Instance (Ubuntu 22.04)
* **Controle de Versão:** Git e GitHub

---

## 🚀 Como Executar o Projeto Localmente

Se você deseja clonar e rodar o agente no seu ambiente de desenvolvimento local, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/agente-manutencao-auramotors.git](https://github.com/SEU_USUARIO/agente-manutencao-auramotors.git)
   cd agente-manutencao-auramotors
   ```
---   
2. **Crie o ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate 
   ```
---   
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
---   
4. **Configure a chave da API:**
   Crie um arquivo .env na raiz do projeto e insira sua chave do Google Gemini ou a que for usar:
   ```
   GEMINI_API_KEY="sua_chave_aqui"
   ```
---
5. **Execute a aplicação:**
   ```
   streamlit run app.py
   ```
---

## ☁️ Deploy em Nuvem (Oracle Cloud - OCI)

O projeto está em produção em uma Máquina Virtual (Compute Instance) na Oracle Cloud Infrastructure (OCI), garantindo alta disponibilidade para os colaboradores da fábrica.

Endereço de Acesso Público: http://137.131.185.255:8501

---

## 🎯 Guia de Uso (Exemplos de Consultas)

O agente cobre diferentes domínios organizacionais da AuraMotors. Você pode testar perguntas como:

Manutenção (PDF/Word): "Qual é o procedimento padrão para resolver o erro E-102 no braço robótico de solda?"

Suprimentos (JSON/Excel): "Quem é o fornecedor principal de fixadores e qual é o seu SLA de entrega atual?"

Segurança (HTML/Markdown): "Quais são os EPIs obrigatórios para o setor de estamparia segundo as normas vigentes?"

---

## 🔮 Próximos Passos e Melhorias Futuras (*Roadmap*)
* **Containerização com Docker:** Empacotar a aplicação em containers para garantir portabilidade total entre ambientes de desenvolvimento e produção.
* **Persistência de Histórico:** Implementar banco de dados para salvar o histórico de interações dos usuários.
* **Orquestração Multi-Agente:** Evoluir a arquitetura para múltiplos agentes especializados por departamento.

---

## 📜 Licença
Este projeto está licenciado sob a **MIT License** - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Contato e Autoria
Desenvolvido por **Renata Aires**. Vamos nos conectar?
* 🔗 [LinkedIn](https://www.linkedin.com/in/renata-aires-saraiva/)
* ✉️ [E-mail Profissional](renataaires8332@gmail.com)
* 🐙 [Repositório no GitHub](https://github.com/RenataAires/agente-manutencao-auramotors.git)
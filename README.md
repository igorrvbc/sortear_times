# sortear_times
App simples parar sortear os jogadores para cada time do futebol(pelada)

# ⚽ Sorteador de Times de Futebol

Sistema simples para organizar e sortear **4 times de 6 jogadores** entre amigos de forma totalmente **aleatória**, com direito a definição de **capitães**, **distribuição dos jogadores** e **sorteio dos confrontos iniciais**.

---

## 🚀 Acesse o App

Você pode acessar e usar o sistema online, sem instalar nada:

👉 [Clique aqui para acessar o app no Streamlit](https://SEU-LINK.streamlit.app)

(Substitua com seu link real assim que publicar)

---

## 👾 Como funciona

1. **Informe os nomes dos 4 capitães** – um para cada time.
2. O sistema irá sortear os jogadores (números de 1 a 20) e distribuir aleatoriamente **5 jogadores para cada capitão**, formando assim os 4 times.
3. Após a formação dos times, o sistema realiza o **sorteio do primeiro confronto entre 2 times**.
4. Os dois times que **não forem sorteados** ficam automaticamente na **linha de espera** para a próxima rodada.

---

## 🎮 Regras

- Cada time possui:
  - 1 Capitão (informado manualmente)
  - 5 Jogadores (sorteados aleatoriamente dos números 1 a 20)
- Os times são identificados como:
  - Exemplo: `Time 1 - João`
- O sorteio é **completamente aleatório**, sem favoritismo nem repetições.

---

## 🧪 Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- Hospedagem via [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📥 Como rodar localmente (opcional)

Se quiser rodar o projeto localmente, siga os passos:

```bash
# Clone o repositório
git clone https://github.com/igorrvbc/sortear_times.git

# Acesse a pasta
cd sortear_times

# Instale as dependências
pip install -r requirements.txt

# Rode o app
streamlit run app.py

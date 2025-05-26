import streamlit as st
import random

# Título do app
st.title("Sorteio de Times da Pelada dos Aposentados")

# Entrar com os nomes dos capitães
st.subheader("Insira os nomes dos capitães:")

# Lista para armazenar os nomes dos capitães
capitaes = []

# Criando 4 campos de texto, um para cada capitão
for i in range(1, 5):
    capitao = st.text_input(f"Capitao do time {i}")
    if capitao:
        capitaes.append(capitao)
    
# Verifica se todos os capitães foram inseridos
if len(capitaes) == 4:
    if st.button("Sortear Times e Confrontos"):
       
    # Cria uma lista com os números de 1 a 20
        numeros_jogadores = list(range(1, 21))
    
    # Embaralha a lista de jogadores
        random.shuffle(numeros_jogadores)
    
    # Cria dicionario com os times
        times = {}
        for i in range(4):
            nome_time = f"Time {i + 1} ({capitaes[i]})"
            times[nome_time] = numeros_jogadores[i * 5: (i + 1) * 5]
        
    
    # Exibe os times
        st.subheader("Sorteio dos Jogadores:")
        for nome_time, jogadores_time in times.items():
            st.write(f" {nome_time}")
            st.write(f"Jogadores: {', '.join(str(j) for j in jogadores_time)}")
               
    # Sorteio dos confrontos    
        st.subheader("Sorteio dos Confrontos")
    
    # Pega lista com os nomes dos times
        nomes_times = list(times.keys())
    # Embaralha a ordem dos times para fazer o sorteio dos jogos
        random.shuffle(nomes_times)
    
    # Os dois primeiros times a jogar
        jogo1 = nomes_times[:2]
    
    # Os dois últimos times a jogar
        linha_fora = nomes_times[2:]
          
    # Exibe o resultado do sorteio dos confrontos
        st.write("Confrontos - Jogo 1")
        st.write(f"{jogo1[0]} x {jogo1[1]}")
        
        st.write("=== Linha Fora ===")
        st.write(f"Linha fora 1: {linha_fora[0]}")
        st.write(f"Linha fora 2: {linha_fora[1]}")
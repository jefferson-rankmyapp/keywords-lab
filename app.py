import streamlit as st
from collections import Counter
from src.analyzer import analyze_description, analyze_description_openai
from src.report_generator import generate_report

st.title("Analisador de Descrições de Aplicativos")
st.write("Cole a descrição longa do seu aplicativo abaixo para receber insights e diagnósticos.")

description = st.text_area("Descrição longa", height=300)

# # Campo para prompt personalizado
# custom_prompt = st.text_area(
#     "Prompt personalizado (opcional)",
#     placeholder="Digite aqui seu prompt personalizado. Use [INSIRA TEXTO] para incluir o texto da descrição.",
#     height=150,
# )

# Controle para definir a quantidade mínima de repetições
min_repeats = st.number_input(
    "Quantidade mínima de repetições para exibir keywords", 
    min_value=1, 
    value=2, 
    step=1
)

if st.button("Analisar"):
    if description.strip():
        st.write("Processando sua descrição...")
        
        results = analyze_description(description, min_repeats)
        
        # Exibir resultados
        for key, value in results.items():
            st.subheader(key.upper())
            st.write(value)

        st.write("Processando sua descrição...")
        results_openai = analyze_description_openai(description, None)
        st.success("Análise OpenAI concluida!")
        
        # Exibição dos resultados
        for key, result in results_openai.items():
            st.subheader(f"Resultado:\n{key.upper()}:")
            st.write(result)
            
        # # Opção de exportar
        # if st.button("Exportar Relatório"):
        #     message = generate_report(results)
        #     st.success(message)
    else:
        st.error("Por favor, cole uma descrição antes de clicar em Analisar.")

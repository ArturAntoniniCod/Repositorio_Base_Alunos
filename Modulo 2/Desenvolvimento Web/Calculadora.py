import streamlit as st

coluna= st.columns(4)

numero=st.text_input('digite um numero: ')
numero1=st.text_input('digite outro numero: ')

with coluna[0]:
    st.write('Somar')
    if st.button('enviar'):
        resultado= int(numero1)+ int(numero)
        st.text(f'o resultado é {resultado}')

with coluna[1]:
    st.write('Subtração')
    
    if st.button('enviar '):
        resultado= int(numero1)- int(numero)
        st.text(f'o resultado é {resultado}')

with coluna[2]:
    st.write('Dividir')
    
    if st.button('enviar  '):
        resultado= int(numero1)/ int(numero)
        st.text(f'o resultado é {resultado}')

with coluna[3]:
    st.write('Multiplicação')
    
    if st.button('enviar   '):
        resultado= int(numero1)* int(numero)
        st.text(f'o resultado é {resultado}')



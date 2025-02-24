# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

# ANSI
# style = 0 = sem estilo / 1=em negrito / 4=sublinhado / 7 inverte

# text= 30=branco / 31 = vermelho/ 32=verde/33=amarelo/34=azul/35=roxo/36=ciano/37=cinza

# background = 40=branco/41=vermelho/42=verde/43=amarelo/44=azul/45=roxo/46=ciano/47=cinza


print('\033[1;30;41mOlá Mundo!\033[m')

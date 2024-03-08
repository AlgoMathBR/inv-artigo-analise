from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords


# Texto para a nuvem de palavras
with open('./build_dataset/texto.txt', 'r') as file:
    # Ler o conteúdo do arquivo
    texto = file.read()

nltk.download('stopwords')

# Obter a lista de stopwords do inglês
stopwords_english = set(stopwords.words('english'))

wordcloud = WordCloud(stopwords=stopwords_english,
                      width=324, # controla o tamanho da imagem
                      height=373, # controla o tamanho da imagem
                      max_words=100,
                      background_color='black').generate(texto)

# Plotar a nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")  # Remover eixos
plt.tight_layout(pad=0)
plt.show()


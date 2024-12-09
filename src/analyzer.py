import re
from collections import Counter
from nltk.util import ngrams
from nltk.corpus import stopwords
from src.openai_client import call_openai
import nltk

# Baixar stopwords do NLTK
nltk.download('stopwords')

def analyze_description(description, min_repeats):
    # Remove caracteres desnecessários
    clean_text = re.sub(r'[^\w\s]', '', description.lower())
    words = clean_text.split()
    char_count = len(description)
    word_count = len(words)
    
    # Dividir texto em frases
    sentences = re.split(r'[.!?]', description)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)
    avg_words_per_sentence = round(word_count / sentence_count, 3) if sentence_count else 0
    
    # Contar palavras e caracteres
    word_frequencies = Counter(words)
    stop_words = set(stopwords.words('portuguese'))  # Você pode customizar esta lista
    keywords = {word: count for word, count in word_frequencies.items() if count >= min_repeats and word not in stop_words}
    
    # Bigramas
    bigrams = list(ngrams(words, 2))
    bigram_frequencies = Counter(bigrams)
    bigram_frequencies_serializable = {" ".join(bigram): freq for bigram, freq in bigram_frequencies.items() if freq >= min_repeats}
    # Trigramas
    trigrams = list(ngrams(words, 3))
    trigram_frequencies = Counter(trigrams)
    trigram_frequencies_serializable = {" ".join(trigram): freq for trigram, freq in trigram_frequencies.items() if freq >= min_repeats}
    
    # Densidade de keywords
    keyword_density_words = {k: round(v / word_count, 3) for k, v in keywords.items()}
    keyword_density_chars = {k: round(v * len(k) / char_count, 3) for k, v in keywords.items()}
    
    # Análise por posição
    first_30_percent = words[:int(len(words) * 0.3)]
    middle_40_percent = words[int(len(words) * 0.3):int(len(words) * 0.7)]
    last_30_percent = words[int(len(words) * 0.7):]
    
    positional_analysis = {
        "first_30_percent": Counter(first_30_percent),
        "middle_40_percent": Counter(middle_40_percent),
        "last_30_percent": Counter(last_30_percent),
    }
    
    # Resultado final
    result = {
        "char_count": char_count,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_words_per_sentence": avg_words_per_sentence,
        "keywords": keywords,
        "keyword_density_words": keyword_density_words,
        "keyword_density_chars": keyword_density_chars,
        "bigram_frequencies": bigram_frequencies_serializable,
        "trigram_frequencies": trigram_frequencies_serializable,
        "positional_analysis": positional_analysis,
    }
    
    return result

# Exemplo de uso
description = """
Coloque aqui a longa descrição do aplicativo.
"""
result = analyze_description(description, min_repeats=2)

# Exibição dos resultados
for key, value in result.items():
    print(f"\n{key.upper()}:")
    if isinstance(value, dict) or isinstance(value, Counter):
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:
        print(value)


def analyze_description_openai(description, custom_prompt=None):
    prompts = {
        "tematicas": "Liste frases de um texto que promovam benefícios, diferenciais ou chamadas à ação. Considere o seguinte texto: [INSIRA TEXTO].",
        "padroes": "Quais padrões ou combinações de palavras sugerem funcionalidades principais ou diferenciais de um aplicativo? Texto: [INSIRA TEXTO].",
        "melhorias": "Analise o texto fornecido e sugira ajustes para otimizar o posicionamento no Google Play Store. Texto: [INSIRA TEXTO].",
    }
    
    results = {}
    if custom_prompt:  # Caso um prompt personalizado seja fornecido
        full_prompt = custom_prompt.replace("[INSIRA TEXTO]", description)
        results["custom"] = call_openai(full_prompt)
    else:
        for key, prompt in prompts.items():
            full_prompt = prompt.replace("[INSIRA TEXTO]", description)
            results[key] = call_openai(full_prompt)
    
    return results

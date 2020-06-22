from unicodedata import normalize 
import re

"""
Script para remover acentos e caracteres especiais de um texto usando python. Caracteres com acento serão substituidos para o equivalente sem acentuação e o ç será trocado por c.

Para NÃO passar os caracteres para minusculo, basta retirar o "lower.()" do metodo.
"""

def filter_text(doc):	
    doc = normalize('NFKD', doc).lower()
    return re.sub('[^a-z0-9 \\\]', '', doc)



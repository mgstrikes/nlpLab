from nltk.stem.snowball import SnowballStemmer
import nltk
from nltk.stem.porter import PorterStemmer
p_stemmer = PorterStemmer()
words = ['run', 'ran', 'runner', 'running',
         'runs', 'easily', 'fairly', 'fairness']
for word in words:
    print(f'{word} ----> {p_stemmer.stem(word)}')


s_stemmer = SnowballStemmer(language='english')

for word in words:
    print(f'{word} ----> {s_stemmer.stem(word)}')

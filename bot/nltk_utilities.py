import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')

class NltkUtilities:
    def remove_stopwords(self, input_tokens):
        common_english_stopwords = stopwords.words('english')
        filtered_tokens = [token for token in input_tokens if token.lower() not in common_english_stopwords]
        return filtered_tokens

    #Transforms each token to its root form (E.g. "running" to "run"), except the tokens that are restaurant names that we want to preserve in the original form
    def input_tokens_stemmer(self, input_tokens):
        stemmer = PorterStemmer()
        processed_tokens = [stemmer.stem(token) for token in input_tokens]
        return processed_tokens

    def stem_word(self, word):
        stemmer = PorterStemmer()
        return stemmer.stem(word)

    #Returns the tokens completely filtered
    def filter_input_tokens(self, input_string):
        input_tokens = word_tokenize(input_string)
        stemmed_input_tokens = self.input_tokens_stemmer(input_tokens)
        filtered_input_tokens = self.remove_stopwords(stemmed_input_tokens)
        return filtered_input_tokens

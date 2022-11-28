import spacy
from math import log

class InvertedIndex:
    
    nlp = spacy.load("en_core_web_lg")    
    nlp.max_length = 3324221
    
    """
    Inverted Index class.
    """
    def __init__(self, db):
        self.index = dict()
        self.word_doc_dict={}
        self.db = db
    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.index)
        
    def index_document(self, document,file_index):
        print("index_document")
        """
        Process a given document, save it to the DB and update the index.
        """          
        
        doc = InvertedIndex.nlp(document['text'])     
        # Removing stopwords and punctuation from the doc.
        robotics_doc=[token for token in doc if not (token.is_stop or token.is_punct or token.is_space)]
 
        # Create a list of all the lemmatized tokens (words)
        for word in robotics_doc:   
            actual_word = word.text         
            if self.word_doc_dict.get(actual_word,0)==0:           
                self.word_doc_dict[actual_word]={}
                self.word_doc_dict[actual_word][file_index]=1
            else:
                self.word_doc_dict[actual_word][file_index]=self.word_doc_dict[actual_word].get(file_index,0)
                self.word_doc_dict[actual_word][file_index]+=1
                
        self.db.add(document)
        return document
    
    def lookup_query(self, query):
        print("lookup_query")
        """
        Returns the dictionary of terms with their correspondent Appearances. 
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        result_file_dict={}
               
        doc = InvertedIndex.nlp(query)     
        # Removing stopwords and punctuation from the doc.
        query_list=[token for token in doc if not (token.is_stop or token.is_punct or token.is_space)]
        
        for q in query_list:
            d = self.word_doc_dict.get(q.text,0) 
            if d!=0:
                length=len(d)
                for file_index in d:
                    result_file_dict[file_index] = result_file_dict.get(file_index,0)
                    result_file_dict[file_index]+=((1+log(d[file_index]))*(log(1/length)/log(10)))
                                                #1st term is tf # 2nd term is idf

        ##8) Sorting the dictionary based on its values            
        result_file_indices = sorted(result_file_dict.items(), key=lambda x:x[1],reverse = False)

        return result_file_indices
        
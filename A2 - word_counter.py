def count_words(text):
    '''Count words in a given text'''
    words = text.split()
    return len(words)

def count_characters(text, include_spaces=True):
    """Count characters in Text"""
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))
    
def analyze_text(text):
    '''perform basic text analysis'''
    word_count = count_words(text)
    char_count = count_characters(text)
    char_no_spaces = count_characters(text, include_spaces=False)

    return {
        'text': text,
        'words': word_count,
        'characters_with_spaces': char_count,
        'characters_without_spaces': char_no_spaces,
        'average_word_length': char_no_spaces/word_count if word_count > 0 else 0
    }

#Lets test out functions
sample_texts = [
    "python is important for NLP",
    "Natural Language Processing",
    "The quick brown fox jumps over the lazy dog"
]

for text in sample_texts:
    result = analyze_text(text)
    print( f"Text: '{result['text']} '")
    print(f'Words: {result['words']}')
    print(f'Characters: {result['characters_with_spaces']}')
    print(f'Average word length: {result['average_word_length']:.2f}')
    print("-" * 40)
    

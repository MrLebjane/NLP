import re
# text_analyzer.py
def get_basic_stats(text):
    """Calculate basic text statistics"""
    # TODO: Implement word count, character count, sentence count
    
    stats=[f'word count: {len(text.split())}',
           f'\ncharacter count:{len(text)}',
           f'\nSentence count:{len(re.split(r'[.!?]+', text))-1}'
           ]
    result=''
    for i in stats:
        result+=i
    return f'\n{result.rstrip()}'

def find_longest_shortest_words(text):
    """Find longest and shortest words"""
    # TODO: Implementation
    reps="!?.[]{/}\\,'\";:"
    for c in reps:
        text=text.replace(c,'')

    wordlist=text.split()
    wordsize=0
    lword=''
    sword=''
    swsize=100
    for word in wordlist:
        if len(word)>wordsize:
            lword=word
            wordsize=len(word)
        if len(word)<swsize:
            sword=word
            swsize=len(word)

    return f'\nLongest word: {lword} \nShortest word: {sword}'

def calculate_vowel_consonant_ratio(text):
    """Calculate ratio of vowels to consonants"""
    reps="!?.[]{/}\\,'\";:"
    for c in reps:
        text=text.replace(c,'')
    text=text.replace(' ','')
    vowels='aeiouAEIOU'   
    return f'\nvowel consonant ratio {sum(1 for c in text if c in vowels)/sum(1 for c in text if c not in vowels)}'

def clean_text(text):
    """Remove punctuation and extra spaces"""
    reps="!?.[]{/}\\,'\";:"
    for c in reps:
        text=text.replace(c,'')

    text=re.sub(' +',' ',text)
    return f'\nClean text: {text}'

def analyze_frequency(text):
    """Find most frequent characters"""
    text=text.replace(' ','')
    chardict={}
    comchar=''
    for c in text:
        if chardict.get(c)==None:
            chardict[c]=1
        else:
             chardict[c]= chardict[c]+1
    
    frecha=""
    numapp=0
    for i in range(3):
        for item in  chardict:
            if numapp<chardict[item]:
                frecha=item
                numapp=chardict[item]
       
        chardict.pop(frecha)
        if i==0:
            comchar=f'Most common char is  \'{frecha}\' with {numapp} appearances'
        elif i==1:
            comchar+=f'\nSecond most common char is \'{frecha}\' with {numapp} appearances'
        else:
            comchar+=f'\nThird most common char is  \'{frecha}\' with {numapp} appearances'
        numapp=0
    return f'\n{comchar}'

def main():
    """Main program"""
    print("=== Text Analyzer Tool ===")
    
    # Get input
    choice = input("Enter '1' for manual input or '2' to analyze sample text: ")
    
    if choice == '1':
        text = input("Enter your text: ")
    else:
        text = "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet at least once!"
    
    # Perform analysis
    print(f"\n--- Analysis Results ---")
    print(f"Original text: {text}")
    print(get_basic_stats(text))
    print(find_longest_shortest_words(text))
    print(calculate_vowel_consonant_ratio(text))
    print(clean_text(text))
    print(analyze_frequency(text))
    
    
if __name__ == "__main__":
    main()
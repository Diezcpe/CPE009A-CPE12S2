def censor_bad_words(sentence, bad_words):
    words = sentence.split()
    filtered_words = []
    
    for word in words:
        clean_word = word.lower().strip('.,!?;:')
        
        if clean_word in bad_words:
            filtered_words.append('*' * len(word))
        else:
            filtered_words.append(word)
    
    return ' '.join(filtered_words)

sentence = input("Enter a sentence: ")
bad = ["bad", "ugly", "terrible", "stupid"]
result = censor_bad_words(sentence, bad)
print("Filtered sentence:", result)
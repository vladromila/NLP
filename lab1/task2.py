from nltk.corpus import wordnet as wn
import random

def get_related_words(word):
    related_words = {
        'synonyms': set(),
        'antonyms': set(),
        'hypernyms': set(),
        'hyponyms': set(),
        'meronyms': set(),
        'holonyms': set()
    }
    synsets = wn.synsets(word)
    
    for synset in synsets:

        for lemma in synset.lemmas():
            related_words['synonyms'].add(lemma.name())

            if lemma.antonyms():
                related_words['antonyms'].add(lemma.antonyms()[0].name())
        

        for hypernym in synset.hypernyms():
            related_words['hypernyms'].update(hypernym.lemma_names())
        
        for hyponym in synset.hyponyms():
            related_words['hyponyms'].update(hyponym.lemma_names())
        
        for meronym in synset.part_meronyms():
            related_words['meronyms'].update(meronym.lemma_names())
        
        for holonym in synset.part_holonyms():
            related_words['holonyms'].update(holonym.lemma_names())
    
    return related_words

def calculate_similarity(word1, word2):
    synset1 = wn.synsets(word1)
    synset2 = wn.synsets(word2)
    
    if not synset1 or not synset2:
        return 0
    
    max_score = 0
    for s1 in synset1:
        for s2 in synset2:
            score = s1.wup_similarity(s2)
            if score and score > max_score:
                max_score = score
    
    return max_score

def play_word_association_game():
    print("Welcome to the Word Association Game!")
    
    interesting_words = ["island", "tree", "car", "book", "computer", "phone", "water", "fire", "earth", "air"]
    word = random.choice(interesting_words)
    related_words = get_related_words(word)
    if not related_words:
        print("No related words found. Please try another word.")
        return
    
    print("Try to come up with words related to:", word)
    score = 0
    
    while True:
        player_word = input("Enter a related word (or type 'exit' to quit): ").strip().lower()
        if player_word == 'exit':
            break
        
        player_word = player_word.replace(" ", "_")
        found = False
        for relation_type, words in related_words.items():
            if player_word in words:
                similarity = calculate_similarity(word, player_word)
                points = int(similarity * 100)
                score += points
                print(f"Good job! '{player_word}' is a {relation_type} of '{word}'. You earned {points} points. Total score: {score}")
                found = True
                break
        
        if not found:
            print(f"'{player_word}' is not related to '{word}'. Try again.")
    
    print(f"Game over! Your total score is: {score}")
    print("\nHere are some related words you might find interesting:")
    for category, words in related_words.items():
        print(f"\n{category.capitalize()}:")
        for word in words:
            print(f" - {word}")

if __name__ == "__main__":
    play_word_association_game()


# Take a word, and calculate the 'score', where the score is the sum of the distances of consecutive letters in the word in the alphabet
# dad  3 + 3 = 6
# add  3 + 0 = 3

# guard against 1 and 0 length input
# only lower case a-z

def word_score(input: string) -> int:
  if len(input) < 2:
    return 0
  
  score = 0
  
  for i in range(len(input)-1):
    score += abs(ord(input[i]) - ord(input[i+1]))
    
  return score

'''
'abc'
'michael'
'rahul'
'samuel'
'aaaaaaa'
'd'
''
'''


class AnagramFinder:
  def __init__(self, words: set):
		self.words = words
    self.max_anagrams = precompute_anagrams(words)
    
  @staticmethod
	def word_score(input: string) -> int:
    # already implemented
    
  # hash_anagram(word1) == hash_anagram(word2) IFF word1 == word2 OR word1 is an anagram of word2
  # anagram: same letters, different order
  @staticmethod
  def hash_anagram(input: string) -> int:
    # already implemented
    
  # takes a word and returns the highest scoring anagram of that word
  # ties -> returns one of those anagrams
  # anagrams are a subset of words
  # word isn't necessarily in words
  
  # preprocess and create equivalence classes for anagrams and their scores
  # receive an input -> you look up the max value anagram for that equivalence class
  # equivalence class: dict(hash: max anagram)
  
  def precompute_anagrams(self, words: set) -> dict:
    groups = {}
    
    for word in words:
      score = self.word_score(word)
      word_hash = self.hash_anagram(word)
      
      if !groups.get(word_hash):
        groups[word_hash] = word
      else:
        current_word = groups[word_hash]
        current_score = self.word_score(current_word)
        if current_score < score:
          groups[word_hash] = word
      
    return groups
  
  # if input doesn't have corresponding words, return the input
  def find_best_anagram(self, input: string) -> string:    
    anagram = max_anagrams.get(self.hash_anagram(input), input)
    return anagram
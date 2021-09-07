class AnagramFinder:
	def __init__(self, words):
		self.words = words
		self.preprocess_words()

	@staticmethod
	def calculate_score(word):
		if (len(word) <= 1): return 0
		total = 0
		for i in range(1, len(word)):
			total += abs(ord(word[i]) - ord(word[i-1]))
		return total

	@staticmethod
	def hash_anagram(word):
		letter_counts = [0] * 26
		for c in word:
			letter_counts[ord(c) - ord('a')] += 1
		res = ""
		for i in range(26):
			res += chr(i+ord('a')) + str(letter_counts[i])
		return res

	def preprocess_words(self):
		self.processed_words = {}
		for word in self.words:
			word_hash = AnagramFinder.hash_anagram(word)
			score = AnagramFinder.calculate_score(word)
			current_vals = self.processed_words.setdefault(word_hash, ["", ""])
			if (score > AnagramFinder.calculate_score(current_vals[0])):
				current_vals[1] = current_vals[0]
				current_vals[0] = word
			elif (score > AnagramFinder.calculate_score(current_vals[1])):
				current_vals[1] = word


	def find_best_anagram(self, word):
		anagrams = self.processed_words.get(AnagramFinder.hash_anagram(word), [])
		for anagram in anagrams:
			if anagram != word:
				return anagram
		return word
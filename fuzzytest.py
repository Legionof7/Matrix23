from fuzzy_extractor import FuzzyExtractor

extractor = FuzzyExtractor(16, 8)

key, helper = extractor.generate('AABBCCDDEEFFGGHH')

print (key)

print (helper)
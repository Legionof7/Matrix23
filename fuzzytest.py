from fuzzy_extractor import FuzzyExtractor

def RunTest():
	
	extractor = FuzzyExtractor(10, 2)
	x = "ABCDEFGHIJ"
	key, helper = extractor.generate(x)

	print (key)
 
	print (helper)

	KeyRecover = raw_input("Enter your key:")

	KeyReturn = extractor.reproduce(KeyRecover, helper) 

	print KeyReturn

RunTest()
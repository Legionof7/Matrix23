
from triplesec import TripleSec
from fuzzy_extractor import FuzzyExtractor

def FuzzyPoro():
	
	extractor = FuzzyExtractor(10, 2) #(CharacterLength, ErrorAllowed)
	BiometricData = "0123456789" #Sample Biometric Data
	key, helper = extractor.generate(BiometricData) #Create the key and the helper

	print key

 	KeyForTripleSec = TripleSec(key) #Runs your generated key through TripleSec
 	EncryptedPrivateKey = KeyForTripleSec.encrypt(b"ThisWouldBeYourPrivateKey") #Encrypts your private key

	KeyRecover = raw_input("Enter your key:") #The second time you scan your fingerprint/biometric data

	KeyReturn = extractor.reproduce(KeyRecover, helper) #Creates your original key

	print KeyReturn
	
	ExtractedKey = TripleSec(KeyReturn) #Runs your regenerated key through TripleSec
	
	
	print(ExtractedKey.decrypt(EncryptedPrivateKey).decode()) #Decodes your EncryptedPrivateKey with your regenerated encryption key


FuzzyPoro()
# Run this with Python 2 because I didn't convert the code to work with 3. FuzzyPoroWithIPFS works with 3 and has custom input anyways.

from triplesec import TripleSec
from fuzzy_extractor import FuzzyExtractor


def FuzzyPoro():

        extractor = FuzzyExtractor(10, 2)  # (CharacterLength, ErrorAllowed)
        # Sample Biometric Data
        BiometricData = raw_input("Enter a biometric data (10 characters):")
        PrivateKey = raw_input("Enter your private key:")
        # Create the key and the helper
        key, helper = extractor.generate(BiometricData)

    print ('Your key is: %s' % (key))

        KeyForTripleSec = TripleSec(key) #Runs your generated key through TripleSec
        EncryptedPrivateKey = KeyForTripleSec.encrypt(PrivateKey) #Encrypts your private key

    print ('Your encrypted private key is: %s' % (EncryptedPrivateKey))

        KeyRecover = input("Enter your key:") #The second time you scan your fingerprint/biometric data

        KeyReturn = extractor.reproduce(KeyRecover, helper) #Creates your original key

    print ('Your recovered key is: %s' % (KeyReturn))

        ExtractedKey = TripleSec(KeyReturn) #Runs your regenerated key through TripleSec

        try:     
                        print ('Your private key is: ')

                        print(ExtractedKey.decrypt(EncryptedPrivateKey).decode()) #Decodes your EncryptedPrivateKey with your regenerated encryption key
        except:
                        print ('Wrong encryption key BAD BAD BAD')

FuzzyPoro()


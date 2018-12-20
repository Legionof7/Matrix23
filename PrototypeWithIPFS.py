from triplesec import TripleSec #Encryption library from Keybase
from fuzzy_extractor import FuzzyExtractor #Fuzzy extractor
import ipfsapi #IPFS connection
def FuzzyPoro():

    extractor = FuzzyExtractor(10, 3)  # (CharacterLength, ErrorAllowed)
    # Sample Biometric Data
    BiometricData = input("Enter biometric data (10 characters):")
    BiometricData = BiometricData.encode('utf-8')
    PrivateKey = input("Enter your private key:")
    PrivateKey = PrivateKey.encode('utf-8')
    # Create the key and the helper
    key, helper = extractor.generate(BiometricData)
  
    print ('Your key is: %s' % (key))

    # Runs your generated key through TripleSec
    KeyForTripleSec = TripleSec(key)
    EncryptedPrivateKey = KeyForTripleSec.encrypt(
        PrivateKey)  # Encrypts your private key

    # Writes a local file with your encrypted private key in it. This file 
    #gets uploaded to IPFS and you get to keep a local backup. You can delete it if you want.
    FileWrite = open("EncryptedKey.txt", "w+")
    FileWrite.write(str(EncryptedPrivateKey))
    FileWrite.close()

    print ('Your encrypted private key is: %s' % (EncryptedPrivateKey))

    # The second time you scan your fingerprint/biometric data
    KeyRecover = input("Enter your biometric data again:")
    KeyReturn = extractor.reproduce(
        KeyRecover, helper)  # Creates your original key

    print ('Your recovered key is: %s' % (KeyReturn))

    # Runs your regenerated key through TripleSec
    ExtractedKey = TripleSec(KeyReturn)

    try:
        print ('Your private key is: ')

        # Decodes your EncryptedPrivateKey with your regenerated encryption key
        print(ExtractedKey.decrypt(EncryptedPrivateKey).decode())
    except:
        print ('Wrong biometric data :(')


def IPFS():
    try:
        api = ipfsapi.connect('127.0.0.1', 5001)
        print(api)

    except ipfsapi.exceptions.ConnectionError as ce:
        print(str(ce))

    UploadKey = api.add('EncryptedKey.txt')
    print(UploadKey)
    hash = api.cat(UploadKey['Hash'])
    print ('The content of the uploaded IPFS file is: %s' % (hash))

FuzzyPoro()
IPFS()

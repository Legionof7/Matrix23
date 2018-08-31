from triplesec import TripleSec
from fuzzy_extractor import FuzzyExtractor


def FuzzyPoro():

    extractor = FuzzyExtractor(10, 2)  # (CharacterLength, ErrorAllowed)
    BiometricData = "0123456789"  # Sample Biometric Data
    # Create the key and the helper
    key, helper = extractor.generate(BiometricData)

    print ('Your key is: %s' % (key))

    # Runs your generated key through TripleSec
    KeyForTripleSec = TripleSec(key)
    EncryptedPrivateKey = KeyForTripleSec.encrypt(
        b"ThisWouldBeYourPrivateKey")  # Encrypts your private key

    print ('Your encrypted private key is: %s' % (EncryptedPrivateKey))

    # The second time you scan your fingerprint/biometric data
    KeyRecover = input("Enter your key:")

    KeyReturn = extractor.reproduce(
        KeyRecover, helper)  # Creates your original key

    print ('Your recovered key is: %s' % (KeyReturn))

    # Runs your regenerated key through TripleSec
    ExtractedKey = TripleSec(KeyReturn)

    print ('Your private key is: ')
    # Decodes your EncryptedPrivateKey with your regenerated encryption key
    print(ExtractedKey.decrypt(EncryptedPrivateKey).decode())


FuzzyPoro()

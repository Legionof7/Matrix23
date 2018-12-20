#https://github.com/blockstack/secret-sharing
#Note:In production, we'd use SecretSharer, not PlaintextToHexSecretSharer. This is for readability.
from secretsharing import PlaintextToHexSecretSharer
#Split the hash into 3 pieces
SplitHash =  PlaintextToHexSecretSharer.split_secret("This is your encrypted private key (that you encrypted with biometric data)", 2, 3)
#Recovery
PlaintextToHexSecretSharer.recover_secret(shares[0:2])




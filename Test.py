import BitcoinECC
import oldBitcoinECC

bitcoin = BitcoinECC.Bitcoin()

#Your private key isn't in "Wallet Import Format" (WIF)
privatekey = "23DKQpDz7bXM7w5KN5Wnmz7bwRNqNHcdQjb2WwrdB1QtTf5gM3pFdf"
#Here is one in with Format :
privatekey = "5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ"

#address    = "12vTsjscg4hYPewUL2onma5pgQmWPMs3ez"
address = bitcoin.AddressFromPrivate(privatekey)

# New lib
print "-- New BitcoinECC --"
print "Addr:  ", bitcoin.AddressFromPrivate(privatekey)
sig = bitcoin.SignMessage("Hello World", privatekey) 
print "Sig:   ", sig
print "Verify:", bitcoin.VerifyMessageFromAddress(address, "Hello World",sig)

# Old lib
print "-- Old Bitcoin ECC --"
bitcoin = oldBitcoinECC.Bitcoin()
print "Public:", bitcoin.BitcoinAddressFromPrivate(privatekey)
print "Addr:  ", bitcoin.BitcoinAddresFromPublicKey()
sig = bitcoin.SignECDSA("Hello World")
print "Sig:   ", sig
print "Verify:", bitcoin.VerifyMessageFromBitcoinAddress(address, "Hello World", sig)

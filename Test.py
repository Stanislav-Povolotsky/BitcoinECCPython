import BitcoinECC

bitcoin = BitcoinECC.Bitcoin()

#Your private key isn't in "Wallet Import Format" (WIF)
privatekey = "23DKQpDz7bXM7w5KN5Wnmz7bwRNqNHcdQjb2WwrdB1QtTf5gM3pFdf"
#Here is one in with Format :
privatekey = "5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ"

#address    = "12vTsjscg4hYPewUL2onma5pgQmWPMs3ez"
address = bitcoin.AddressFromPrivate(privatekey)

# New lib
print("Addr:   %s" % bitcoin.AddressFromPrivate(privatekey))
print("Public: %s" % bitcoin.PublicFromPrivate(privatekey))
sig = bitcoin.SignMessage(b"Hello World", privatekey) 
print("Sig:    %s" % sig)
print("Verify: %s" % bitcoin.VerifyMessageFromAddress(address, b"Hello World",sig))

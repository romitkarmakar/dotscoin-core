from dotscoin.Address import Address
from dotscoin.Transaction import Transaction
from dotscoin.Block import Block
from dotscoin.BlockChain import BlockChain
from threads.Election import Election

if __name__ == '__main__':
    address = Address()
    block = Block("weewwt")
    chain = BlockChain()
    election = Election()

    # address.load('-----BEGIN EC PRIVATE KEY-----\nMF8CAQEEGCG9B1ZuujYTb4bOfGQiau3EiATdcRk9aaAKBggqhkjOPQMBAaE0AzIA\nBIIgUmipFSQFoQPaHVpxSvCga0jep2+PB/4xBSPWTsYm5xhkLhNK2Op+ZDoev/9B\nZg==\n-----END EC PRIVATE KEY-----\n',
    #              '-----BEGIN PUBLIC KEY-----\nMEkwEwYHKoZIzj0CAQYIKoZIzj0DAQEDMgAEgiBSaKkVJAWhA9odWnFK8KBrSN6n\nb48H/jEFI9ZOxibnGGQuE0rY6n5kOh6//0Fm\n-----END PUBLIC KEY-----\n')
    # # print(address.get_public_address())
    # block.calculate_merkle_root()

    # # chain.add_block()
    # # chain.clear_chain()
    # print(chain.read_chain())
    election.get_stakes()



    #     "sfsgg",
    #     "fgshhsh",
    #     "dsdfdsggsg"


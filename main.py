from hashlib import sha256


class BitCoinMinner:
    block_number:  int
    transaction:   str
    previous_hash: str
    prefix_zero:   int
    max_nonce:     int

    def __init__(self, block_number: int, transaction: str, previous_hash: str, prefix_zero: int, max_nonce: int = None):
        self.block_number   = block_number
        self.transaction    = transaction
        self.previous_hash  = previous_hash
        self.prefix_zero    = prefix_zero
        self.max_nonce      = max_nonce
        self.prefix_string  = '0' * self.prefix_zero
        self.encoded_data   = None
        self.new_hash       = None

    def praise_summary(self, nonce: int):
        '''Print summary
        :params nonce (int) Number of attempt 
        '''
        print("------------------------------------------------------------------------")
        print("Congratulations! You successfully mined 6.25 bitcoins with {} nonces".format(nonce + 1))
        print("-------------------------------- Detail --------------------------------")
        print("transaction:    ", self.transaction)
        print("deciphered hash:", self.previous_hash)
        print("new hash:       ", self.new_hash)
        print("nonces:         ", nonce, "times")

    def _hash_sha256(self) -> str:
        '''Convert string to sha256'''
        return sha256(self.encoded_data).hexdigest()
    
    def mining(self, nonce):
        self.data         = str(self.block_number) + self.transaction + self.previous_hash + str(nonce)
        self.encoded_data = self.data.encode('ascii')
        self.new_hash     = self._hash_sha256()

        if self.new_hash.startswith(self.prefix_string):
            self.praise_summary(nonce)
            exit()
    
    def start_miner_with_nonces(self):
        ''' Start miner with maximun nonces'''
        print('Start mining with {} maximun nonces ...'.format(self.max_nonce))
        for nonce in range(self.max_nonce):
            self.mining(nonce)
        raise BaseException(f'Could not find bitcoin after trying {nonce} nonces')
    
    def start_miner(self):
        ''' Start miner with no timeout'''
        nonce = 0
        print('Start mining forever ...')
        while True:
            self.mining(nonce)
            nonce += 1
    
    def run(self):
        if self.max_nonce:
            self.start_miner_with_nonces()
        else:
            self.start_miner()
            

if __name__ == '__main__':

    block_number   = 5
    transaction    = '''Toni -> Mike  = 1 BTC, Rose -> David = 2 BTC'''
    previous_hash  = "0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7"
    difficulty     = 4
    max_nonce      = 100000000
    max_nonce      = None

    # TODO add Logging
    # TODO execution time
    # TODO unittest
    btc_miner = BitCoinMinner(
                    block_number=5,
                    transaction=transaction, 
                    previous_hash=previous_hash, 
                    prefix_zero=difficulty, 
                    max_nonce=max_nonce
                )
    btc_miner.run()

from Crypto.Hash import MD4

##dado = input()
##dado_hash = MD4.new(dado.encode('utf-8')).hexdigest()
dado_hash = input('Insira uma hash: ')

def readwordlist():
    wordSet = set()
    try:
        with open('/usr/share/wordlists/wordlist-utf8.txt', 'r') as wordlist:
            for line in wordlist:
                for word in line.split():
                    wordSet.add(word)  
    except IOError:
        print('Error opening file')
    return wordSet

def hash(dado):
    result = MD4.new(dado.encode('utf-8')).hexdigest()
    return result

def bruteforce(dado_hash, wordSet):
    for word in wordSet:
        if hash(word) == dado_hash:
            print(f'A hash é "{hash(word)}". Em plaintext: {word}')
            exit()

wordSet = readwordlist()
bruteforce(dado_hash, wordSet)
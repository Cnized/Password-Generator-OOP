import random
import string
import nltk
from abc import ABC, abstractmethod
nltk.download('words')


class PasswordGenerator(ABC):
    @abstractmethod
    def generator(self):
        pass
    
class PinCodeGenerator(PasswordGenerator):
    def __init__(self, length: int ):
        self.length = length
        
    def generator(self):
        '''Generates a random PIN code of specified length.
        :param length: Length of the PIN code.
        :type length: int
        :return: Generated PIN code as a string.
        :rtype: str
        '''
        return ''.join(random.choice(string.digits) for _ in range(self.length))

class RandomPasswordGenerator(PasswordGenerator):
    '''Generates a random password with specified length and character types.
    :param length: Length of the password.
    :param include_numbers: Whether to include numbers in the password.
    :param include_symbols: Whether to include symbols in the password.
    :return: Generated password as a string.
    :rtype: str
    '''
    def __init__(self, length: int = 8, include_numbers:bool = False, include_symbols:bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation
    
    def generator(self):
        '''Generates a random password.
        :param length: Length of the password.
        :type length: int
        :return: Generated password as a string.
        :rtype: str
        '''
        return ''.join(random.choice(self.characters) for _ in range(self.length))

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, words_length: int = 4, seperator: str = '-', be_capital:bool = False, Vocabulary: list = None):
        if Vocabulary is None:
            Vocabulary = nltk.corpus.words.words()
        self.words_length = words_length
        self.seperator = seperator
        self.be_capital = be_capital
        self.Vocabulary = Vocabulary
        
        
    def generator(self):
        '''Generates a memorable password using random words from a vocabulary.
        :param words_length: Number of words in the password.
        :param seperator: Separator between words.
        :param be_capital: Whether to randomly capitalize words.
        :return: Generated memorable password as a string.
        :rtype: str 
        '''
        password_words = (random.choice(self.Vocabulary) for _ in range(self.words_length))
        if self.be_capital:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
            
        return self.seperator.join(password_words)




if __name__ == '__main__':
    rpassword = RandomPasswordGenerator(12, include_numbers=True, include_symbols=True)
    print("Random Password:", rpassword.generator())
    
    pin = PinCodeGenerator(4)
    print("PIN Code:", pin.generator())
    
    custom_password = MemorablePasswordGenerator(4, seperator='-', be_capital=True)
    print("Memorable Password:", custom_password.generator())


"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    return contents



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    # split up string and put in list
        # - print it to make sure its printing a list
    words = text_string.split()
    # for loop:
        # -set an i variable
    #     - for index in the len(list above):
    #         pairs = listabove[i:i+1]
    #         chain_key = (words[i], words[i + 1])
    #         chain_value = words[i + 2]
    #         chains[chain_key] = chains.get(chain_key, [])
    
    # # keep track of pairs
    for i in range(0, len(words)-2):
        chain_key = (words[i], words[i+1])
        # chain_key = ('Would, you')
        #chains[chain_key] = ['could', 'could']
        # word_to_add = 'like'
        # 

        chains[chain_key] = chains.get(chain_key, list([]))
        # print(f"---chains: {chains}")
        word_to_add = words[i+2]
        # print(f"---word_to_add: {word_to_add}")
        chain_value = chains[chain_key]
        # print(f"----chain_value: {chain_value}")
        if type(chain_value) is list:
            chain_value.append(word_to_add)
            # print(f"---chain_value in conditional: {chain_value}")
  
        chains[chain_key] = chain_value
        # print(f"----chains at this iteration: {chains}")
        # chains[chain_key] = chains[chain_key].append(chain_value)
        # chains[chain_key] = chain_value

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print(chains)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)

# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string
    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    1 2 3 4, 1 2 4 3
    gp(word[:-1]) or gp(word[1:]
    use for loop?
    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.

    ○ suppose we have a method that can give us a list of all permutations of ​all but 
    the first character​ in ​sequence​ (Hint: think recursion)
    ○ then the permutations of all characters in ​sequence​ would be ​all the different 
    ways​ we can insert the first character into each permutation of the remaining characters
    ■ example: if our word was ‘bust’, we hold out the character ‘b’ and get the 
    list [‘ust’, ‘sut’, ‘stu’, ‘uts’, ‘tus’, ‘tsu’]
    ● then ‘ust’ gives us: ‘​b​ust’, ‘u​b​st’, ‘us​b​t’, ‘ust​b​’
    ● ‘sut’ gives us: ‘​b​sut’, ‘s​b​ut’, ‘su​b​t’, ‘sut​b​’
    '''
    new_seq = []
    if len(sequence) <= 1:
        return sequence
#    sequence = list(sequence)
#    letter_1 = sequence.pop(0) #we have a
#    sequence = ''.join(sequence) # bc
    letter_1 = sequence[0]
    for word in get_permutations(sequence[1:]): #lets say we have [bc, cb], then we have [b] and [c]
        for ind in range(len(word)+1):
            #print(word[0:ind]+ "1" + word[ind:len(word)])
            new_seq.append(word[0:ind]+ letter_1 + word[ind:len(word)]) #just move the first letter to every position and create the list
        #print(new_seq)
    #print()
    return new_seq
        
    

if __name__ == '__main__':
    example_input = 'odlepids'
    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)




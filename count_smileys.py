import re

def count_smileys(arr):

    """
        The function returns the total number of smiling faces.

        Rules for a smiling face:

        - Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
        - A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
        - Every smiling face must have a smiling mouth that should be marked with either ) or D

        No additional characters are allowed except for those mentioned.

        Valid smiley face examples:
         :) :D ;-D :~)

        Invalid smiley faces:
         ;( :> :} :]


        countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;

        countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
        
        countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
    """

    pattern = r'[:;]+[-~]*[)D]'
    count = 0
    for el in arr:
        if re.fullmatch(pattern, el):
            count += 1

    return count

sm = []
# sm = [':D',':~)',';~D',':)']
print(count_smileys(sm))



skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

keep_words = ['go','take','drop']


def filter_words(words, skip_words):
    output = []
    for i in range(len(words)):
        if words[i] not in skip_words:
            output.append(words[i])
    return output

    
def remove_punct(text):
    no_punct = ""
    for char in text:
        if char.isalpha() or char == ' ':
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):
    return filter_words(remove_punct(user_input).lower().split(),skip_words)




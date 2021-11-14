import re
def replace_string(N, sentences):
    for sentence in sentences:
        while ' && ' in sentence:
            sentence = re.sub(' && ', ' and ', sentence)
        while ' || ' in sentence:
            sentence = re.sub(' \|\| ', ' or ', sentence)
        print(sentence)

if __name__ == '__main__':
    replace_string(1, ["x&& &&& && && x || | ||\|| x"])
from urllib.request import urlopen

def fetch_words():
    with urlopen("http://sixty-north.com/c/t.txt") as story:
        story_words = [] # global variable
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    for word in story_words:
        print(word)

# fetch_words()

# python a03...py
# import a03...

# print(__name__) # print module name, but only once even import again
if __name__ == "__main__":

    fetch_words()

# put your code here.
filename = open('twain.txt')

words_in_file = {}

def word_strip(file):
    for line in filename:
        line = line.rstrip()
        words = line.split(' ')
        #print line.split(' ')
        for word in words:
            if word not in words_in_file:
                words_in_file[word] = 1
            else:
                words_in_file[word] += 1

word_strip(filename)
#print words_in_file

for key in words_in_file:
    print key, words_in_file[key]



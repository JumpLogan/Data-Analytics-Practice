import re
import math

# a
fp = open('quotes.txt', 'r')
quote = []
full_list = []
for index, line in enumerate(fp):
    line = line.rstrip()
    convert_string = ''.join(line)
    if index % 2 == 0:
        quote = convert_string
    else:
        quote += ' - ' + convert_string
        full_list.append(quote)
print '(a)',full_list

# b
def extract_word(fullquote):
    word_list = re.findall("\w+", fullquote.lower())
    print '(b)', word_list


extract_word("Two roads diverged in a wood, and I...I took the one less traveled by, and that has made all the difference. - Robert Frost")

# c
def posting_list(fullquote):
    posting_value = {}
    word_list = re.findall("\w+", fullquote.lower())
    dict_key = [word_list[0]]
    dict_value = [0]
    for i in range(len(word_list)):
        for j in range(len(dict_key)):
            if dict_key[j] == word_list[i]:
                dict_value[j] += 1
                repeat = True
                break
            else:
                repeat = False
        if not repeat:
            dict_key.append(word_list[i])
            dict_value.append(1)
    for i in range(len(dict_key)):
        posting_value[dict_key[i]] = dict_value[i]
    posting_list = {fullquote: posting_value}
    print '(c)',posting_list


posting_list("Two roadert Frost Frost Frost")


# d
def reverse_posting(keyword,fullquote):
    keyword = keyword.lower()
    word_list = re.findall("\w+", fullquote.lower())
    cnt = 0
    for i in range(len(word_list)):
        if keyword == word_list[i]:
            cnt += 1
    dict_dict = {fullquote: cnt}
    reverse_posting_list = {keyword: dict_dict}
    print '(d)',reverse_posting_list


reverse_posting('frost', "Two roadert Frost Frost Frost")

# e
def TF_IDF(keyword,fullquote):
    keyword = keyword.lower()
    posting_value = {}
    word_list = re.findall("\w+", fullquote.lower())
    dict_key = [word_list[0]]
    dict_value = [0]
    for i in range(len(word_list)):
        for j in range(len(dict_key)):
            if dict_key[j] == word_list[i]:
                dict_value[j] += 1
                repeat = True
                break
            else:
                repeat = False
        if not repeat:
            dict_key.append(word_list[i])
            dict_value.append(1)
    for i in range(len(dict_key)):
        posting_value[dict_key[i]] = dict_value[i]
    if keyword in posting_value:
        TF = float(posting_value[keyword])/max(dict_value)
    else:
        TF = 0
    # print 'TF',TF

    total = 0
    cnt = 0
    for fullquote in full_list:
        word_list = re.findall("\w+", fullquote.lower())
        for i in range(len(word_list)):
            if keyword == word_list[i]:
                cnt += 1
                break;
        total += 1
    if cnt == 0:
        IDF = 0
    else:
        IDF = math.log(float(total)/cnt)
    # print 'IDF',IDF
    TF_IDF = TF*IDF
    # print '(e) TF_IDF',TF_IDF
    return TF_IDF


TF_IDF('enterainer', 'An actor is at most a poet and at least an entertainer. - Marlon Brando')

# f
def single_TF_IDF(keyword):
    keyword = keyword.lower()
    single_dict = {}
    dict_key = []
    dict_value = []
    for fullquote in full_list:
        word_list = re.findall("\w+", fullquote.lower())
        for i in range(len(word_list)):
            if keyword == word_list[i]:
                dict_key.append(fullquote)
                dict_value.append(TF_IDF(keyword,fullquote))
                break
    for i in range(len(dict_key)):
        single_dict[dict_key[i]] = dict_value[i]
    print '(f)',single_dict


single_TF_IDF('the')

# g
def multiple_TF_IDF(keyword_list):
    multiple_dict = {}
    dict_key = []
    dict_value = []
    match = False
    for fullquote in full_list:
        word_list = re.findall("\w+", fullquote.lower())
        for i in range(len(word_list)):
            for keyword in keyword_list:
                if keyword.lower() == word_list[i]:
                    dict_key.append(fullquote)
                    multi_TF_IDF = 0
                    for key in keyword_list:
                        multi_TF_IDF += TF_IDF(key.lower(), fullquote)
                    dict_value.append(multi_TF_IDF)
                    match = True
                    break
                else:
                    match = False
            if match:
                break
    #Construct the dictionary
    for i in range(len(dict_key)):
        multiple_dict[dict_key[i]] = dict_value[i]
    return multiple_dict


Test_wordlist = ['Picasso', 'actor', 'Miss']
print '(g)', multiple_TF_IDF(Test_wordlist)
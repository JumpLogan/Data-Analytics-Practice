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
print '(a) Build a list of full quotes'
for item in full_list:
    print '"' + item + '"'


# b
def extract_word(fullquote):
    """Extract words without repeating from full quotes"""
    word_list = re.findall("\w+", fullquote.lower())
    merged_word_list = []
    for word in word_list:
        if word not in merged_word_list:
            merged_word_list.append(word)
    return merged_word_list


print '(b)', extract_word("Two roads diverged in a wood, and I...I took the has in the difference. - Robert Frost")


# c
def posting_list(fullquote):
    """Build the postings-list dictionary for single quote"""
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
    return posting_list

"""Iterate through each quote"""
full_posting_list = {}
for quote in full_list:
    full_posting_list.update(posting_list(quote))
print '(c)', full_posting_list


# d
def reverse_posting(keyword,fullquote):
    """Build the reverse postings-list dictionary for single word and single quote"""
    keyword = keyword.lower()
    word_list = re.findall("\w+", fullquote.lower())
    cnt = 0
    for i in range(len(word_list)):
        if keyword == word_list[i]:
            cnt += 1
    reverse_posting_dict_value = {fullquote: cnt}
    if cnt == 0:
        return 0
    else:
        return reverse_posting_dict_value

full_word_list = []
merged_full_word_list = []
reverse_posting_dict = {}
#Extract each word from each quote
for quote in full_list:
    full_word_list += extract_word(quote)
#Create list of words without repeating them
for word in full_word_list:
    if word not in merged_full_word_list:
        merged_full_word_list.append(word)
#Go through each word and each quote to find the occurences of that word
for key in merged_full_word_list:
    full_reverse_posting_list_value = {}
    for quote in full_list:
        if reverse_posting(key, quote) != 0:
            full_reverse_posting_list_value.update(reverse_posting(key, quote))
    reverse_posting_dict[key] = full_reverse_posting_list_value
print '(d)', reverse_posting_dict


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
    return single_dict


print '(f)',single_TF_IDF('Miss')

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


Test_wordlist = ['heart', 'mind']
print '(g)', multiple_TF_IDF(Test_wordlist)
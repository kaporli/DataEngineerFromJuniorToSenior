import string
s = "The English Wikipedia is, along with the Simple English Wikipedia, one of two English-language editions of Wikipedia, an online encyclopedia. It was founded on 15 January 2001 as Wikipedia's first edition and, as of 12 October 2022, has the most articles of any edition, at 6,561,058.[1] As of October 2022, 11% of articles in all Wikipedias belong to the English-language edition; this share was more than 50% in 2003.[2][3] The edition's one-billionth edit was made on 13 January 2021.[4]"
res = sum([i.strip(string.punctuation).isalpha() for i in s.split()])
print(res)
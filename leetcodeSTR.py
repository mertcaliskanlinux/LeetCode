class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) #uzunluk al s değişkenine
        if n == 0: #eğer s değişkeni boş ise
            return "" #boş döndür
        if n == 1: #eğer s değişkeni 1 karakterli ise
            return s #s değişkenini döndür
        maxLen = 1 #maxLen değişkenine 1 ata
        start = 0 #start değişkenine 0 ata
        for i in range(n): #i değişkenini 0'dan n'ye kadar döndür
            if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]: #eğer i-maxLen-1 1'den büyükse ve s[i-maxLen-1:i+1] s[i-maxLen-1:i+1][::-1]'e eşitse
                start = i - maxLen - 1 #start değişkenine i-maxLen-1 ata
                maxLen += 2 #maxLen değişkenine 2 ekle
                continue #devam et 
            if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]: #eğer i-maxLen 0'dan büyükse ve s[i-maxLen:i+1] s[i-maxLen:i+1][::-1]'e eşitse
                start = i - maxLen #start değişkenine i-maxLen işlemini ata
                maxLen += 1 #maxLen değişkenine 1 ekle
        return s[start:start+maxLen] #s[start:start+maxLen]'i döndür

# Path: leetcodeSTR.py
print(Solution.longestPalindrome(Solution, "babad") )#Solution.longestPalindrome fonksiyonunu çağır ve "babad" parametresini gönder)

# yukarıdaki kod'un amaçı: verilen bir string içerisinde en uzun palindromu bulmak ,
# palindrom: tersten okunuşu da aynı olan kelimelerdir. Örneğin: "kazak", "ey edip adanada pide ye", "ey edip adana'da pide ye" gibi.

    
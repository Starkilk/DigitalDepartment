#Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное

def findMostCommonWord(string):
    words = string.lower().split()#разделили текст на слова
    wordsCount = {}#словарь для подсчёта частоты каждого слова

    for word in words:#для слов в списке
        if word in wordsCount:#если слово есть в словаре, то:
            wordsCount[word] += 1#увеличиваем значение этого слова(ключа) на 1
        else:
            wordsCount[word] = 1#если слова нет, то добавляем его и говорим, что встретилось оно 1 раз


    mostCommon = max(wordsCount, key=wordsCount.get)#ключ с максимальным значением

    return mostCommon

print(findMostCommonWord("pasha and pasha and pasha skhfbskbfsdhsf"))

def longestWords(string):
    words = string.split()

    longestWord = max(words, key=len)

    return longestWord

print(longestWords("pasha and pasha and pasha skhfbskbfsdhsf"))
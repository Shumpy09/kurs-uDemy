'''initialCapital = 20000
percent = 0.03
maxTimeYears = 10

year = 0
capital = initialCapital

while year < maxTimeYears:
    year += 1
    capital = round((1 + percent) * capital,2)
    
    print('po tym roku: ', year, ' będziesz miał: ', capital)
else:
    print('Odsetki wynoszą: ', capital - initialCapital)
'''

'''
number = 20730906
tmpnumber = number
suma = 0

while tmpnumber > 0:
    reszta = tmpnumber % 10
    print('Reszta to: ', reszta)
    suma += reszta
    tmpnumber = tmpnumber // 10
else:
    print('Suma liczb liczby', number, ' wynosi: ', suma)
'''

text = '''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.'''

wordLength = 6
shortWords = 0
longWords = 0
i = 0

listOfWords = text.split(' ')

while i < len(listOfWords):
    if len(listOfWords[i]) < wordLength:
        shortWords += 1
    else:
        longWords += 1
    
    i += 1

print('Short words: ', shortWords)
print('Long words: ', longWords)
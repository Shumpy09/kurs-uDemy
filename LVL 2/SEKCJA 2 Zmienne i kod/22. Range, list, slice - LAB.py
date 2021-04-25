colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def funkcja_kolor(colors, n):

    return colors[:n]
    
#n = int(input("Podaj ilosc kolorow: "))
#print(funkcja_kolor(colors, n))

for i in range(1,len(colors)+1):
    print(funkcja_kolor(colors,i))
    
text = """Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, 
        która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. 
        Wydawać się może utopijnym miejscem realizacji pasji zawodowych. 
        W rzeczywistości jednak nie jest wcale tak kolorowo. 
        Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."""


print(text[text.index('(')+1:text.index(')')])
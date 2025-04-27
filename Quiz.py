q = ["Portugal", "Spain", "France", "Andorra", "United Kingdom", "Iceland", "Ireland", "Norway", "Finland", "Sweden", "Russia", "Ukraine", "Romania", "Belgium", "Netherlands", "Germany", "Poland", "Denmark", "Belarus", "Switzerland", "Luxembourg", "Monaco", "Liechtenstein", "San Marino", "Vatican City", "Italy", "Austria", "Slovakia", "Slovenia", "Serbia", "Moldova", "Montenegro", "Albania", "Greece", "Turkiye", "North Macedonia", "Croatia", "Bosnia and Herzegovina", "Malta", "Cyprus", "Czechia", "Hungary", "Bulgaria", "Kosovo", "Lithuania", "Latvia", "Estonia"]
a = ["Lisbon", "Madrid", "Paris", "Andorra la Vella", "London", "Reykjavik", "Dublin", "Oslo", "Helsinki", "Stockholm", "moscow", "Kiev", "Bucharest", "Brussels", "Amsterdam", "Berlin", "Warsaw", "Copenhagen", "Minsk", "Bern", "Luxembourg", "Monaco", "Vaduz", "San Marino", "Vatican City", "Rome", "Vienna", "Bratislava", "Ljubljana", "Belgrade", "Chisinau", "Podgorica", "Tirana", "Athens", "Ankara", "Skopje", "Zagreb", "Sarajevo", "Valletta", "Nicosia", "Prague", "Budapest", "Sofia", "Pristina", "Vilnius", "Riga", "Tallinn"]

score = 0
for i in range (0, len(q)):
    ans = input("What is the capital city of " + q[i]).lower()
    if ans == a[i].lower():
        score +=1
print(score, "/ 3")

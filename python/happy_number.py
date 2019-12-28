'''
Et happy number er gitt ved det følgende: start med et positivt heltall.
Finn summen av kvadratet av sifferene til tallet.
Gjenta så denne prosessen .
Dersom dette resulterer i 1, er tallet et happy number, dersom man ender med en uendelig sekvens, er det et sad number.

For eksempel, 19 er et happy number: 19
12+92=82 82+22=68 62+82=100 12+02+02=1.

Oppgaven: Skriv ut alle happy tall på intervallet [1, 200].

Gjør dette uten bruk av input() eller raw_input().
'''
#My solution follows:

def s(n):
    s=0
    while n:
        s+=(n%10)*(n%10)
        n=n//10
    return s

#The solution is shorter when usong m(n) to find the sum of the digits
def m(n):
    return sum(int(i)**2 for i in str(n))

def j(n):
    t=n
    k=n
    while k!=4 and k!=1:
        k=m(k)
    if k==1:
        print(t)

for i in range(1,201):
    j(i)

#Shorter solution: (got rid of all the functions)
for i in range(1,201):
    t,k=i,i
    while k!=4 and k!=1:
        k=sum(int(i)**2 for i in str(k))
    if k==1:
        print(t)

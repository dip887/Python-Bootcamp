# Building a project of Horoscope
next = True
while next==True:
    print(''' Wanna See your Future, Choose Appropriate option below:
    1. Aries
    2. Tauras
    3. Gemini
    4. Cancer
    5. Leo
    6. Virgo
    7. Libras
    8. Scorpio
    9. Sagittarius
    10. Capricorn
    11. Aquarius
    12. Pisces
    ''')

    o = int(input("**** Know Your Future by Choosing your Zodiac Sign Quickly Here ****\nYou Choose: "))
    #print('\n')
    if o==1:
        print("Luckiest person on the Earth\n")
    elif o==2:
        print("Tauras\n")
    elif o==3:
        print("Gemini\n")
    elif o==4:
        print("cancer\n")
    elif o==5:
        print("leo\n")
    elif o==6:
        print("vigro\n")
    elif o==7:
        print("libra\n")
    elif o==8:
        print("scorpio\n")
    elif o==9:
        print("Sagittarius\n")
    elif o==10:
        print("capricorn\n")
    elif o==11:
        print("aquarius\n")
    elif o==12:
        print("Pisces\n")
    else:
        print("Dont be oversmart..!! choose under given Options")


    if input("Wanna continue(y/n): ")=='Y':
        next = True
    else:
        next = False

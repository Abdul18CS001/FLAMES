from time import sleep

print("\n\t\t\t\U0001F525FLAMES!\U0001F525")

print("\t\t\U0001F4CCTag them. Let's Have a Fun\U0001F4CC\n\n")

a=input("Your Name \U0001F447 :\n")

b=input("\nYour Partner Name \U0001F447:\n")

c=a.lower()

d=b.lower()

alp="abcdefghijklmnopqrstuvwxyz"

count=0

for i in range(0,25):

    j=alp[i]

    if j in c and d:

        c1=c.count(j)

        d1=d.count(j)

        dif=c1-d1

        differ=abs(dif)

        count+=differ

    else:

        c1=c.count(j)

        d1=d.count(j)

        sum=c1+d1

        count+=sum

count=count

a="\n\U0001F4ABProcessing..."

sleep(1)

for i in range(3):

    print(a)

    sleep(1.5)

print("\n\n\n\n")

if (count==3 or count==5 or count==10 or count==14):

    print("\n\t\t\t\U0001F607FRIEND!\U0001F601")

    print('\n "Friendship is born at that moment when one person says to another: What! ..." ' )

    print ('\n "A good friend is like a four-leaf clover; hard to find and lucky to have.” \n\n\n')    

elif (count==8 or count==12 or count==13):

    print("\n\t\t\t\U0001F648AFFECTION!\U0001F60D")

    print('\n"Lets, lets stay together." ... ')

    print('\n "We are most alive when we are in love. ..." \n\n\n' )

    

elif (count==6 or count==11):

    print("\n\t\t\t\U0001F48CMARRIAGE!\U0001F495") 

    print('\n “A successful marriage requires falling in love many times, always with the same person" ')

    print('\n "A great marriage is not when the perfect couple comes together...." \n\n\n')

    

elif (count==2 or count==4 or count==9):

    print("\n\t\t\t\U0001F608ENEMY!\U0001F624")

    print('\n "Always forgive your enemies; nothing annoys them so much.” ...' )

    print('\n "Be who you want to be and not care about what others think.” \n\n\n')

    

elif (count==1 or count==7 or count==15):

    print("\n\t\t\t\U0001F644SISTER!\U0001F47B")

    print('\n“Having a sister is like having a best friend you cant get rid of. ..." ')

    print('\n "A sister can be seen as someone who is both ourselves and very much not ourselves—a special kind of double.” \n\n\n')

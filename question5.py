number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244531613185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001033678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
number = str(number)
li = []

for x in number:
    li.append(int(x))
print(len(li))
maximum = 0
counter = 0
for y in li:

    if(counter < 984 and y * li[counter+1] * li[counter+2] * li[counter+3] * li[counter+4]* li[counter+5] * li[counter+6] * li[counter+7] * li[counter+8] * li[counter+9] * li[counter+10] * li[counter+11] * li[counter+12] > maximum):
        maximum = y * li[counter+1] * li[counter+2] * li[counter+3] * li[counter+4]* li[counter+5] * li[counter+6] * li[counter+7] * li[counter+8] * li[counter+9] * li[counter+10] * li[counter+11] * li[counter+12] 
    counter += 1
print(maximum)
import constants


distKm = float(input("Type how many kilometers do you want to convert: "))



distMiles = distKm / constants.ONE_MILE

distMiles = format(distMiles, '.3f')

distMiles = str(distMiles)

print("It is equal to " + distMiles + " miles")

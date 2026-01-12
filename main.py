from crop import Crop
from farmer import Farmer
from irrigation import Irrigation

maize = Crop("Maize", 3, 2)
farmer = Farmer("Sravanthi", "Expert")
water = Irrigation(6)

farmer.take_care(maize, water)
farmer.take_care(maize, water)
farmer.take_care(maize, water)
farmer.take_care(maize, water)
farmer.take_care(maize, water)
maize.harvest()
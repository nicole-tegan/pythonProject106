print("Average miles per person per year= 14,032");
miles = 14032
sedan = 30
sedanh = 45
suv = 20
suvh = 30
tesla = 126
chevy = 108
print("Sedan:" , miles / sedan , "gallons used")
print("Sedan Hybrid:" , miles / sedanh , "gallons used")
print("SUV:" , miles / suv , "gallons used")
print("SUV Hybrid:" , miles / suvh , "gallons used")
print("Tesla Model 3:" , miles / tesla , "gallons (equivelant) used")
print("Chevy Bolt:" , miles / chevy , "gallons (equivelant) used")
print ("")
print("Cost of Gas in Oregon (USD):")
print("Sedan:$" , ((miles / sedan) * 4.72 ))
print("Sedan Hybrid:$" , ((miles / sedanh) * 4.72 ))
print("SUV:$" , ((miles / suv) * 4.72 ))
print("SUV Hybrid:$" , ((miles / suvh) * 4.72 ))
print("")
print("Cost of Gas in California (USD):")
print("Sedan:$" , ((miles / sedan) * 5.92 ))
print("Sedan Hybrid:$" , ((miles / sedanh) * 5.92 ))
print("SUV:$" , ((miles / suv) * 5.92 ))
print("SUV Hybrid:$" , ((miles / suvh) * 5.92 ))
print("")
print("Cost of Gas Equivalent (At Home Charging) (USD):")
print("Tesla Model 3:$" , ((miles / tesla) *33.7 * 0.1116 ))
print("Chevy Bolt:$" , ((miles / chevy) *33.7 * 0.1116 ))
print ("")
print("Cost of Gas Equivalent (At Charging Station) (USD):")
print("Tesla Model 3:$" , ((miles / tesla) *33.7 * 0.3 ))
print("Chevy Bolt:$" , ((miles / chevy) *33.7 * 0.3 ))
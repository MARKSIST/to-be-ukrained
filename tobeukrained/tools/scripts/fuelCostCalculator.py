# cost1Liter - вартість 1 літру палива
# fuelConsumption - витрата палива на 100 км
# distance - дистанція яку необхідно подолати
# totalFuel - сумарна кфлькість пального
# totalPrice - сума грн

def fuelCostCalculator(cost1Liter, fuelConsumption, distance):
    totalFuel = (distance / 100)*fuelConsumption
    totalPrice = totalFuel*cost1Liter
    return totalFuel, totalPrice

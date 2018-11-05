
def convert(rates, value, from_currency, to_currency):
    if from_currency == to_currency:
        return value
    
        
    available_rates = []
    for conversion in rates:

        available_rates.append(conversion[0])
        available_rates.append(conversion[1])
        
        if (from_currency in conversion) and (to_currency in conversion):
            if from_currency == conversion[0]:
                return value * conversion[2]
            elif from_currency == conversion[1]:
                return value / conversion[2]
    
    for conversion in rates:
        if (from_currency in conversion) and (to_currency not in conversion) and (to_currency in available_rates):
            if from_currency == conversion[0]:
                return convert(rates, value * conversion[2], conversion[1], to_currency)
            elif from_currency == conversion[1]:
                return convert(rates, value / conversion[2], conversion[0], to_currency)
                        
    
    raise ValueError("Conversion rates unknown.")

    




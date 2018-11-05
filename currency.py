
def convert(rates, value, from_currency, to_currency):
    if from_currency == to_currency:
        return value

    for conversion in rates:
        if (from_currency and to_currency) in conversion:
            if from_currency == conversion[0]:
                return value * conversion[2]
            elif from_currency == conversion[1]:
                return value / conversion[2]
        

    




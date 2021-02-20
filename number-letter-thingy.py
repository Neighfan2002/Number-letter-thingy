def TRANSLATE(NUMBER):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    THOUSAND = 1000
    MILLION = 1000000
    BILLION = 1000000000
    TRILLION = 1000000000000
    QUADRILLION = 1000000000000000

    if (NUMBER < 20):
        return d[NUMBER]

    if (NUMBER < 100):
        if NUMBER % 10 == 0:
            return d[NUMBER]
        else:
            return d[NUMBER // 10 * 10] + '' + d[NUMBER % 10]

    if (NUMBER < THOUSAND):
        if NUMBER % 100 == 0:
            return d[NUMBER // 100] + 'hundred'
        else:
            return d[NUMBER // 100] + 'hundredand' + TRANSLATE(NUMBER % 100)

    if (NUMBER < MILLION):
        if NUMBER % THOUSAND == 0:
            return TRANSLATE(NUMBER // THOUSAND) + 'thousand'
        elif NUMBER % THOUSAND >= 100:
            return TRANSLATE(NUMBER // THOUSAND) + 'thousand' + TRANSLATE(NUMBER % THOUSAND)
        else:
            return TRANSLATE(NUMBER // THOUSAND) + 'thousandand' + TRANSLATE(NUMBER % THOUSAND)

    if (NUMBER < BILLION):
        if (NUMBER % MILLION) == 0:
            return TRANSLATE(NUMBER // MILLION) + 'million'
        elif NUMBER % MILLION >= 100:
            return TRANSLATE(NUMBER // MILLION) + 'million' + TRANSLATE(NUMBER % MILLION)
        else:
            return TRANSLATE(NUMBER // MILLION) + 'millionand' + TRANSLATE(NUMBER % MILLION)

    if (NUMBER < TRILLION):
        if (NUMBER % BILLION) == 0:
            return TRANSLATE(NUMBER // BILLION) + 'billion'
        elif (NUMBER % BILLION) >= 100:
            return TRANSLATE(NUMBER // BILLION) + 'billion' + TRANSLATE(NUMBER % BILLION)
        else:
            return TRANSLATE(NUMBER // BILLION) + 'billionand' + TRANSLATE(NUMBER % BILLION)

    if (NUMBER < QUADRILLION):
        if (NUMBER % TRILLION) == 0:
            return TRANSLATE(NUMBER // TRILLION) + 'trillion'
        elif (NUMBER % TRILLION) >= 100:
            return TRANSLATE(NUMBER // TRILLION) + 'trillion' + TRANSLATE(NUMBER % TRILLION)
        else:
            return TRANSLATE(NUMBER // TRILLION) + 'trillionand' + TRANSLATE(NUMBER % TRILLION)

    if (NUMBER % QUADRILLION == 0):
        return TRANSLATE(NUMBER // QUADRILLION) + 'quadrillion'
    elif (NUMBER % QUADRILLION) >= 100:
        return TRANSLATE(NUMBER // QUADRILLION) + 'quadrillion' + TRANSLATE(NUMBER % QUADRILLION)
    else:
        return TRANSLATE(NUMBER // QUADRILLION) + 'quadrillionand' + TRANSLATE(NUMBER % QUADRILLION)

def do():
    start = TRANSLATE(int(input('NUMBER: ')))
    new = start
    on = 1
    while on:
        print(new)
        old, new = new, TRANSLATE(len(new))
        if old == new:
            on = 0
            
while True:
    do()
    print('')







    

"""currency.py

This module provides several functions to implement a simple
currency exchange routine using an online currency service.
The primary function in this module is exchange.

__author__ = "Li Zihan"
__pkuid__  = "1700011735"
__email__  = "chemlzh@pku.edu.cn"
"""

from urllib.request import urlopen
from json import *


def iscurrency(currency):
    """Returns: True if currency is a valid (3 CAPITALIZED letter
    code for a) currency. It returns False otherwise.
    Notice: this function is just a primary examination of the currency.
    It can't guarantee that currency is in use nowadays.
    Any 3 capitalized letter code, such as 'AAA', will be judged
    as a 'valid' currency.

    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    if type(currency) != str:
        return False
    elif not currency.isalpha() or len(currency) != 3:
        return False
    elif not currency.isupper():
        return False
    return True


def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.

    A currency query converts amount_from money in currency currency_from
    to the currency currency_to. The response should be a string of the form

        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'

    where the values old-amount and new-amount contain the value and name
    for the original and new currencies. If the query is invalid, both
    old-amount and new-amount will be empty, while "success" will be followed
    by the value false.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    website = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?' + \
        'from=' + currency_from + '&' + 'to=' + currency_to + '&' + \
        'amt=' + str(amount_from)
    doc = urlopen(website)
    docstr = doc.read()
    return docstr
    doc.close()


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange
    if these parameters are valid. If these parameters are not valid,
    the function will return -1.0, printing the error information at the
    same time.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to if these
    parameters are valid.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    if not iscurrency(currency_from):
        print('Source currency code is invalid.')
        return -1.0
    elif not iscurrency(currency_to):
        print('Exchange currency code is invalid.')
        return -1.0
    elif (not isinstance(amount_from, int) and
          not isinstance(amount_from, float)):
        print('Currency amount is invalid.')
        return -1.0
    elif amount_from < 0:
        print('Currency amount is not a non-negative number.')
        return -1.0
    else:
        json_string = currency_response(currency_from,
                                        currency_to, amount_from)
        result = loads(json_string)
        if result['success']:
            t = result['to'].split()
            return float(t[0])
        else:
            print(result['error'])
            return -1.0


def main():
    """Return: none, but it can print the result according to input.

    The main function reads the source currency, the target currency
    and the amount of the source currency, and it prints the amount
    of the target currency."""
    source = input('Please input the currency on hand:')
    target = input('Please input the currency to convert to:')
    amount_s = float(input('Please input the amount of currency to convert:'))
    amount_t = exchange(source, target, amount_s)
    print('The amount of currency received in the given exchange is ', amount_t)


def test_iscurrency():
    """Test function iscurrency()."""
    assert iscurrency('USD')
    assert not iscurrency(123)
    assert not iscurrency('123')
    assert not iscurrency('12a')
    assert not iscurrency('usd')
    assert iscurrency('ABC')


def test_currency_response():
    """Test function currency_response()."""
    assert currency_response('12a', 'EUR', 2.5) == \
        b'{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
    assert currency_response('USD', '1ab', 2.5) == \
        b'{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }'
    assert currency_response('USD', 'EUR', 'abc') == \
        b'{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }'
    assert currency_response('USD', 'EUR', 2.5) == \
        b'{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'


def test_exchange():
    """Test function exchange()."""
    assert exchange('USDL', 'EUR', 2.5) == -1.0
    assert exchange('US', 'EUR', 2.5) == -1.0
    assert exchange('12AB', 'EUR', 2.5) == -1.0
    assert exchange('usd', 'EUR', 2.5) == -1.0
    assert exchange('12a', 'EUR', 2.5) == -1.0

    assert exchange('USD', 'EURO', 2.5) == -1.0
    assert exchange('USD', 'EU', 2.5) == -1.0
    assert exchange('USD', '12CD', 2.5) == -1.0
    assert exchange('USD', 'eur', 2.5) == -1.0
    assert exchange('USD', '1ab', 2.5) == -1.0

    assert exchange('USD', 'EUR', 'abc') == -1.0
    assert exchange('USD', 'EUR', -2.5) == -1.0
    assert exchange('ABC', 'EUR', 2.5) == -1.0
    assert exchange('USD', 'DEF', 2.5) == -1.0

    assert exchange('USD', 'EUR', 2.5) == 2.0952375


def test_all():
    """Test all functions."""
    test_currency_response()
    test_exchange()
    test_iscurrency()


if __name__ == '__main__':
    main()





def zad1(in1: str, in2: str):
    """
    function checks 2 given strings and creates list of post codes between them
    it doesnt matter which string is bigger or if they are the same, all outcomes should be correct

    :param in1: string variable
    :param in2: string variable
    :return: list of post codes
    """
    if in1 == in2:
        return in1

    v11 = in1.split("-")
    v22 = in2.split("-")

    v1 = [int(x) for x in v11]
    v2 = [int(x) for x in v22]

    if v1[0] == v2[0] and v1[1] == v2[1]:
        return in1
    addresses_list = []
    if v1[0] < v2[0]:
        for i in range(v1[0], v2[0] + 1):
            if i == v1[0]:
                for j in range(v1[1], 1000):
                    address = str(i) + "-" + str(j)
                    addresses_list.append(address)
            elif i == v2[0]:
                for j in range(0, v2[1] + 1):
                    address = str(i) + "-" + str(j)
                    addresses_list.append(address)
            else:
                for j in range(0, 1000):
                    address = str(i) + "-" + str(j)
                    addresses_list.append(address)

    elif v1[0] > v2[0]:
        for i in range(v2[0], v1[0] + 1):
            if i == v2[0]:
                for j in range(v2[1], 1000):
                    address = str(i) + "-" + str(j)
                    addresses_list.append(address)
            elif i == v1[0]:
                for j in range(0, v1[1] + 1):
                    address = str(i) + "-" + str(j)
                    addresses_list.append(address)
            else:
                for j in range(0, 1000):
                    address = str(i) + "-" + str(j)
                    addresses_list.append(address)
    else:
        if v1[1] <= v2[1]:
            for i in range(v1[1], v2[1] + 1):
                address = str(v1[0]) + "-" + str(i)
                addresses_list.append(address)
        else:
            for i in range(v2[1], v1[1] + 1):
                address = str(v2[0]) + "-" + str(i)
                addresses_list.append(address)
    return addresses_list


def zad2(list, n):
    """
    function takes list and number of elements and then checks how many elements the list is missing

    :param list: List
    :param n: int variable
    :return: list of missing elements
    """
    if n < max(list):
        print("error: n shorter than list")
        return []

    missing = []
    for i in range(1, n):
        if i not in list:
            missing.append(i)
    return missing


def zad3(n1, n2):
    """
    returns list of decimal numbers in range of 2 to 5.5 with step 0.5 of decimal type

    :param n1: int
    :param n2: int
    :return: list of decimal type variables
    """
    from decimal import Decimal
    result = []
    for i in range(n1, n2):
        d = Decimal(i)/Decimal(2)
        result.append(d)
    return result


if __name__ == "__main__":
    w1 = "79-150"
    w2 = "80-320"

    post_code_list = zad1(w1, w2)
    print("zad1: ", post_code_list)

    list = [1, 3, 5, 7, 9]
    n = 10
    missing = zad2(list, n + 1)
    print("zad2: ", missing)

    result = zad3(4, 12)
    print("zad3: ", result)

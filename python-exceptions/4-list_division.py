#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """İki siyahının elementlərini bir-birinə bölür.

    Args:
        my_list_1 (list): Birinci siyahı.
        my_list_2 (list): İkinci siyahı.
        list_length (int): Hesablanacaq element sayı.

    Returns:
        Yeni siyahı (bölmə nəticələri ilə).
    """
    new_list = []
    for i in range(list_length):
        div_result = 0
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div_result)
    return new_list

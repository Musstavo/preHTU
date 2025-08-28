# "hello" => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# " s p a c e s " => [ " S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "]

def wave(string):
    empty_lst = []
    scnd_empty_lst = []
    string = string.replace(" ", "")
    for num in range(len(string)):
        new_str = string[:num] + string[num].capitalize() + string[num+1:]
        empty_lst.append(new_str)

    for word in empty_lst:
        scnd_empty_lst.append(" " + " ".join(word) + " ")

    #I DONT KNOW WHAT TO DO


wave("hello")
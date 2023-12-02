for char in s:
            if char.isdigit():
                index = s.index(char)
                if s[index:].isdigit() and int(char) != 0:
                    return True
                else:
                    return False
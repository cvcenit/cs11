def len_side_comment(s):
    return len(s[1 + s.find("("):s.rfind(")")])
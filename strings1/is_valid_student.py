def is_valid_student_number(s):
    return len(s) == 10 and (s[0] == '2') and (s[4] == "-") and "0" <= s[1] <= "9" and "0" <= s[2] <= "9" and "0" <= s[3] <= "9" and "0" <= s[5] <= "9" and "0" <= s[6] <= "9" and "0" <= s[7] <= "9" and "0" <= s[8] <= "9" and "0" <= s[9] <= "9"

print(is_valid_student_number("2"))
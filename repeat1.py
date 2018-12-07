def most_frequent_char(str):

            dict1 = {}

            max_repeat_count = 0

            for letter in string:

                    if letter not in dict1:

                            dict1[letter] = 1

                    else:

                            dict1[letter] += 1

                    if dict1[letter]> max_repeat_count:

                            max_repeat_count = dict1[letter]

                            most_repeated_char = letter

            return most_repeated_char

if __name__ == '__main__':

        string =raw_input("")

        print ""+ most_frequent_char(string)


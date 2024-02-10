class Magic:
    @staticmethod
    def replace(s, old_char, new_char):
        return s.replace(old_char, new_char)

    @staticmethod
    def str_length(s):
        return len(s)

    @staticmethod
    def trim(s):
        return s.strip()

    @staticmethod
    def list_slice(lst, indexes):
        start, end = indexes
        sliced = lst[start:end+1]
        return sliced if sliced else -1

magic = Magic()

replace_example = magic.replace("AzErty-QwErty", "E", "e")
str_length_example = magic.str_length("hello world")
trim_example = magic.trim("      python is awesome      ")
list_slice_example = magic.list_slice([1, 2, 3, 4, 5], (1, 3))

replace_example, str_length_example, trim_example, list_slice_example

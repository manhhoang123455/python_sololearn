
# def countdown():
#     i = 5
#     while i > 0:
#         yield i
#         i -= 1

# for i in countdown():
#     print(i)

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))
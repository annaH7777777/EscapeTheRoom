# Q9: Which method is called when using len() on an object?
# Options:
#   - __len__
#   - __size__
#   - __length__
#   - __count__
# Answer: __len__
#
# Explanation:
# len(obj) calls obj.__len__() under the hood. A class becomes
# "sized" (supports len()) by defining __len__, which must return
# a non-negative integer.
# __size__, __length__, __count__ are not real Python magic methods.
# Built-ins like list, tuple, str, dict, set all define __len__.


class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)

    def __len__(self):
        # Called automatically by len(playlist_instance)
        return len(self.songs)


p = Playlist(["song A", "song B", "song C"])

print(f"len(p)        = {len(p)}")          # triggers __len__
print(f"p.__len__()   = {p.__len__()}")     # same thing, called directly

# Built-ins use the same protocol
print(f"len('hello')  = {len('hello')}")
print(f"len([1,2,3])  = {len([1, 2, 3])}")
print(f"len({{'a':1}}) = {len({'a': 1})}")

# An object with __len__ also becomes truthy/falsy by its length:
#   empty (len == 0) -> False, non-empty -> True
print(f"bool(Playlist([])) = {bool(Playlist([]))}")   # False
print(f"bool(p)            = {bool(p)}")              # True

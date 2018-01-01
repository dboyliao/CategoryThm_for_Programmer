#!/usr/bin/env python3
# https://bartoszmilewski.com/2014/11/04/category-the-essence-of-composition
# Challenges


def identity(x):
  return x


def compose(f, g):
  return lambda *args, **kwargs: f(g(*args, **kwargs))


if __name__ == "__main__":
  to_str = str
  foo = compose(identity, to_str)
  bar = compose(to_str, identity)
  print(foo(1.0) == bar(1.0))

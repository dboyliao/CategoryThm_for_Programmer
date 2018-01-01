#!/usr/bin/env python3
# -*- coding:utf8 -*-
from functools import wraps
from inspect import signature
from time import sleep


def _make_key(func, *args, **kwargs):
  sig = signature(func)
  bd = sig.bind(*args, **kwargs)
  return bd.args


def memorize(func):
  def _inner(func):
    cache = {}
    make_key = _make_key

    @wraps(func)
    def cached(*args, **kwargs):
      key = make_key(func, *args, **kwargs)
      if key in cache:
        print('cahce hit!')
        return cache[key]
      result = func(*args, **kwargs)
      cache[key] = result
      return result
    return cached

  return _inner(func)


if __name__ == "__main__":
  @memorize
  def func(a, b):
    sleep(2)
    return a + b

  for _ in range(10):
    print(func(1, 1))

  @memorize
  def func2(a, b=2, c=3):
    sleep(2)
    return a * b * c

  for _ in range(5):
    print(func2(1, 2, c=3))

  for _ in range(5):
    print(func2(1, b=3, c=2))

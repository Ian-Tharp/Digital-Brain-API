
from functools import lru_cache


@lru_cache()
def build_llms():
  print('Building LLMS')

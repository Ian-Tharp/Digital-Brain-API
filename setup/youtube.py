from functools import lru_cache
import os


@lru_cache()
def setup_youtube():
  print('Setting up YouTube')
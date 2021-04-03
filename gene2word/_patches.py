import functools

# Apply some monkey patches to functools emulating the newer `cache` and `cached_property`
# convenience functions
try:
    functools.cache
except:
    functools.cache = functools.lru_cache()
try:
    functools.cached_property
except:

    def cached_property(f):
        cf = functools.cache(f)
        return property(cf)

    functools.cached_property = cached_property

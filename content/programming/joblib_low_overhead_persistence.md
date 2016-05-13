Title: Joblib persistence improvements
Date: 2016-05-20
Category: Python
Tags: joblib, persistence, big data
Slug: New low-overhead persistence in joblib for big data
Authors: Alexandre Abadie, Gaël Varoquaux
Summary: New persistence in joblib enables low-overhead storage of big data contained in arbitrary objects

## Joblib persistence improvements

### Introduction

Started to work recently on joblib trying to improve the persistence of numpy
arrays. 2 problems:
* memory copies
* one file per array

Example :
```python
>>> import numpy as np
>>> import joblib
>>> obj = [np.arange(10), np.ones((5,5))]

# Note that 3 files are generated:
>>> joblib.dump(obj, '/tmp/test.pkl')
['/tmp/test.pkl', '/tmp/test_01.npy', '/tmp/test_02.npy']
>>> joblib.load('/tmp/test.pkl')
[2 numpy arrays]
```

The memory footprint of each step can be retrieved using the excellent package
memory_profiler:
<image>nice picture</image>

This behavior is now lost to history. Let's discover these new features and then
explain them a bit.

### What's new

Starting from 0.10, joblib is able to persist numpy arrays in a single file and
without duplicating them in memory during read and write steps. This opens
contextlib syntaxic sugar usage possibility when playing with cache file. The
other big step forward is internal usage of __all__ compression formats
available in the python standard library.

For people early joblib adopters, be reassured : this new version is compatible
with pickles generated using older version (>= 0.8.4). By the way, you are
encourage to update (rebuild?) your cache if you want to take advantage of this
new version.

Examples of new features:
```python
>>> import joblib
>>> import numpy as np

# Create an object with 2 numpy arrays
>>> obj = [np.arange(10), np.ones((5,5))]

# The resulting pickle only consists in 1 file
>>> joblib.dump(obj, '/tmp/test.pkl')
['/tmp/test.pkl']

# Let's try the compressors available in the standard library.
# The compressor is selected automatically by looking at the output file
# extension :
>>> joblib.dump(obj, '/tmp/test.pkl.z')   # zlib
['/tmp/test.pkl.z']
>>> joblib.dump(obj, '/tmp/test.pkl.gz')  # gzip
['/tmp/test.pkl.gz']
>>> joblib.dump(obj, '/tmp/test.pkl.bz2')  # bz2
['/tmp/test.pkl.bz2']
>>> joblib.dump(obj, '/tmp/test.pkl.lzma')  # lzma
['/tmp/test.pkl.lzma']
>>> joblib.dump(obj, '/tmp/test.pkl.xz')  # xz
['/tmp/test.pkl.xz']

# Of course one can play with the compression level, but then the compressor
# has to be given explicitly:
>>> joblib.dump(obj, '/tmp/test.pkl.compressed', compress=('zlib', 6))
['/tmp/test.pkl.compressed']
>>> joblib.dump(obj, '/tmp/test.compressed', compress=('lzma', 6))
['/tmp/test.pkl.compressed']

# The compressed files have a valid magic number so joblib can select
# automatically the matching decompressor to read their content:
>>> joblib.load('/tmp/test.compressed')
[2 numpy arrays]
```

Examples of usage with file handles:
```python
>>> import joblib
>>> data = "some data to persist"

# persist to/from a raw file
>>> with open('/tmp/test.pkl', 'wb') as f:
>>>    joblib.dump(data, f)
['/tmp/test.pkl']
>>> with open('/tmp/test.pkl', 'rb') as f:
>>>    print(joblib.load(f))
"some data to persist"

# compressors are also supported:
>>> import gzip
>>> with gzip.GzipFile('/tmp/test.pkl.gz', 'wb') as f:
>>>    joblib.dump(data, f)
['/tmp/test.pkl.gz']
>>> with gzip.GzipFile('/tmp/test.pkl.gz', 'rb') as f:
>>>    print(joblib.load(f))
"some data to persist"

# auto detection of compression works as well:
>>> with open('/tmp/test.pkl.gz', 'rb') as f:
>>>     print(joblib.load(f))
"some data to persist"

# finally it's possible to pickle in a buffer in memory using io.BytesIO:
>>> import io
>>> buf = io.BytesIO()
>>> joblib.dump(data, buf)
>>> joblib.load(buf)
```

### Enhancement strategy

Hack on top of pickle (already there), different strategies tested, use low level numpy primitives
(e.g nditer). No more compatible with

Performance improvements : implemented a custom Zlib file compressor (for zlib and
gzip) + heavy use of buffering.

Side effects : the generated pickle is not compatible with standard library
pickle module.

### Memory consumption and performance comparisons

No more memory copies ! The overhead only corresponds to the size of the buffer
used during writing/reading steps.

With large arrays the speed is slightly faster : put nice matplotlib figures here.

Discussion with dict/list : io.BytesIO does copy in memory but is faster
compared to io.BufferedIO : put some profiling here.

### Conclusion and future work

Memory copies were a ressource gap when caching on disk very large
numpy arrays, e.g arrays with a size close to the available RAM on the computer.
The solution was to use intensive buffering and a lot of hacking on top of
pickle and numpy.

Pickling numpy arrays using file handle is a first step toward pickling in
sockets. Then it make broadcasting of data possible between computing units on a
network.

Another potential improvements is to make the supported list of compressors
extendable by allowing external project to register new ones. Some work has
already been started with LZO (using python-lzo) but LZ4 also seems to be an
interesting ones.

Thanks to @lesteve, @ogrisel and @GaelVaroquaux for the valuable help, reviews
and support.


###Notes

Data: sklearn.datasets.fetch_lfw_people

Strategies:

- pickle
- numpy.savez
- old joblib
  no zlib
  zlib3
- new joblib
  no zlib
  zlib3

Info displayed:
- read time
- write time
- memory footprint
- DU

Other graph:
 - comparison of compressions



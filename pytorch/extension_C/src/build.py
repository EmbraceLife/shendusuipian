# build.py
from torch.utils.ffi import create_extension
ffi = create_extension(
name='_ext.my_lib',
headers='src/my_lib.h',
sources=['src/my_lib.c'],
with_cuda=False,
)
ffi.build()

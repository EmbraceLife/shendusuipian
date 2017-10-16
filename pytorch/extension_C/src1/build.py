# build.py
from torch.utils.ffi import create_extension
ffi = create_extension(
name='_ext.my_lib1',
headers='src1/my_lib1.h',
sources=['src1/my_lib1.c'],
with_cuda=False,
)
ffi.build()

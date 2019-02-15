# encoding: utf-8
from .a import A
from .b import B

# # For large module, use lazy import
# def A():
#     from .a import A
#     return A()
#
# def A():
#     from .b import B
#     return B()
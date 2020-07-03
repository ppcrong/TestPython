from ctypes import *

# visual studio
# dll_c = CDLL('dll/ctypes_dll.dll')
# vscode
dll_c = CDLL('dll/libctypes_dll.dll')

# read data of value
# method1 byref
c_value = c_int(0)
ret = dll_c.test_value(byref(c_value))
print('ret: {}'.format(ret))
print('c_value: {}'.format(c_value))
# method2 pointer
c_value = c_int(0)
c_value_p = pointer(c_value)
ret = dll_c.test_value(c_value_p)
print('ret: {}'.format(ret))
print('c_value: {}'.format(c_value))
# method3 POINTER type in argtypes
dll_c.test_value.argtypes = [POINTER(c_int)]
c_value = c_int(0)
ret = dll_c.test_value(c_value)
# ret = dll_c.test_value(byref(c_value)) #  the same result as above line => https://blog.csdn.net/Kelvin_Yan/article/details/86546784
print('ret: {}'.format(ret))
print('c_value: {}'.format(c_value))

# read data of byte array
import numpy as np

# c_buf_p assign method 1
buf = np.arange(1, 17, dtype=np.byte)
c_buf_p = (c_byte * len(buf))(*buf)
dll_c.test_buf(c_buf_p)
# dll_c.test_buf(byref(c_buf_p)) #  the same result as above line
buf = list(c_buf_p)
print('buf: {}'.format(buf))
buf = np.ctypeslib.as_array(c_buf_p, np.int8)
print('buf: {}'.format(buf))

# c_buf_p assign method 2
c_buf_p = (c_byte * 16)()
dll_c.test_buf(c_buf_p)
buf = list(c_buf_p)
print('buf: {}'.format(buf))
buf = cast(c_buf_p, POINTER(c_byte * 16)).contents
print('buf: {}'.format(buf))
for b in buf:
    print(b)


# read data of bounding_box_s
class bounding_box_s(Structure):
    _fields_ = [
        ('x1', c_float),
        ('y1', c_float),
        ('x2', c_float),
        ('y2', c_float),
        ('score', c_float),
        ('class_num', c_int32)
    ]

    def __repr__(self):
        ret_str = ''
        for field in self._fields_:
            ret_str = '\n'.join((ret_str, '\t{}: {}'.format(field[0], getattr(self, field[0]))))
        return ret_str


box1 = bounding_box_s(x1=0, y1=0, x2=0, y2=0, score=0, class_num=0)
box2 = bounding_box_s(x1=0, y1=0, x2=0, y2=0, score=0, class_num=0)
boxes = [box1, box2]
print('\n===1==={}'.format(boxes))

# c_boxes_p assign method 1
c_boxes_p = (bounding_box_s * len(boxes))(*boxes)
c_boxes_pp = pointer(c_boxes_p)
ret = dll_c.test_struct_array(byref(c_boxes_pp), len(boxes))
print('ret: {}'.format(ret))
boxes = list(c_boxes_p)
print('\n===2==={}'.format(boxes))

# c_boxes_p assign method 2
boxes = [box1, box2]
print('\n===3==={}'.format(boxes))
c_boxes_p = (bounding_box_s * 2)()
c_boxes_pp = pointer(c_boxes_p)
ret = dll_c.test_struct_array(byref(c_boxes_pp), len(boxes))
print('ret: {}'.format(ret))
boxes = list(c_boxes_p)
print('\n===4==={}'.format(boxes))
boxes = cast(c_boxes_p, POINTER(bounding_box_s * 2)).contents
for b in boxes:
    print('\n===5==={}'.format(b))


# read data of test_result_s
class test_result_s(Structure):
    _fields_ = [
        ("class_count", c_uint),  # uint32_t
        ("box_count", c_uint),  # boxes of all classes
        ("boxes", POINTER(POINTER(bounding_box_s)))  # box array
    ]

    def __repr__(self):
        ret_str = ''
        for field in self._fields_:
            ret_str = '\n'.join((ret_str, '\t{}: {}'.format(field[0], getattr(self, field[0]))))
        return ret_str


# box3 = bounding_box_s(x1=0, y1=0, x2=0, y2=0, score=0, class_num=0)
# boxes = [box1, box2, box3]
# c_boxes = (bounding_box_s * 3)()
# c_boxes_p = pointer(c_boxes)
# res1 = test_result_s(boxes=byref(c_boxes_p))
# res2 = test_result_s(boxes=byref(c_boxes_p))
# res3 = test_result_s(boxes=byref(c_boxes_p))
# results = [res1, res2, res3]
# print('\n///1///{}'.format(results))
# c_results = (test_result_s * len(results))(*results)
# c_results_p = pointer(c_results)
# ret = dll_c.test_struct_array2(byref(c_results_p), len(results))
# print('ret: {}'.format(ret))
# results = list(c_results)
# print('\n///2///{}'.format(results))

"""
reference: https://chrisheydrick.com/2016/02/06/passing-a-ctypes-array-of-struct-from-python-to-dll/
"""
class structtest(Structure):
    _fields_ = [
        ("x", c_char),
        ("y", c_int),
        ("z", c_long)
    ]

    def __repr__(self):
        ret_str = ''
        for field in self._fields_:
            ret_str = '\n'.join((ret_str, '\t{}: {}'.format(field[0], getattr(self, field[0]))))
        return ret_str


n_struct2 = 5
struct1 = structtest()
struct2 = (structtest * n_struct2)()

print("\n///////////////////\nBefore passing to .dll")
print(struct1)
for i in range(n_struct2):
    print("struct2[{}] {}".format(i, struct2[i]))

dll_c.fillonestruct(byref(struct1))
dll_c.fillmultiplestruct(byref(struct2), c_int(n_struct2))
print("\nAfter passing to .dll")
print(struct1)
for i in range(n_struct2):
    print("struct2[{}] {}".format(i, struct2[i]))

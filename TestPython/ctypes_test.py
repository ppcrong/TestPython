from ctypes import *

# visual studio
# dll_c = CDLL('dll/ctypes_dll.dll')
# vscode
dll_c = CDLL('dll/libctypes_dll.dll')

# read data of value
c_value = c_int(0)
ret = dll_c.test_value(byref(c_value))
print('ret: {}'.format(ret))
print('c_value: {}'.format(c_value))

# read data of byte array
import numpy as np

# c_buf_p assign method 1
buf = np.arange(1, 17, dtype=np.byte)
c_buf_p = (c_byte * len(buf))(*buf)
dll_c.test_buf(c_buf_p)
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

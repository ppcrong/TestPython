from ctypes import *

# visual studio
#dll_c = CDLL('dll/ctypes_dll.dll')
# vscode
dll_c = CDLL('dll/libctypes_dll.dll')

# read data of value
c_value = c_int(0)
ret = dll_c.test_value(byref(c_value))
print('ret: {}'.format(ret))
print('c_value: {}'.format(c_value))

# read data of byte array
import numpy as np

buf = np.arange(1, 17, dtype=np.byte)
c_buf_p = (c_byte * len(buf))(*buf)
dll_c.test_buf(c_buf_p)
buf = list(c_buf_p)
print('buf: {}'.format(buf))
buf = np.ctypeslib.as_array(c_buf_p, np.int8)
print('buf: {}'.format(buf))


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


box1 = bounding_box_s(x1=0, y1=0, x2=0, y2=0, score=0, class_num=0)
box2 = bounding_box_s(x1=0, y1=0, x2=0, y2=0, score=0, class_num=0)
boxes = [box1, box2]
print('boxes: {}'.format(boxes))
c_boxes_p = (bounding_box_s * len(boxes))(*boxes)
c_boxes_pp = pointer(c_boxes_p)
ret = dll_c.test_struct_array(byref(c_boxes_pp), len(boxes))
print('ret: {}'.format(ret))
boxes = list(c_boxes_p)
print('boxes: {}'.format(boxes))
print('boxes[0]: x1:{:.1f},y1:{:.1f}'.format(boxes[0].x1, boxes[0].y1))
print('boxes[0]: x2:{:.1f},y2:{:.1f}'.format(boxes[0].x2, boxes[0].y2))
print('boxes[1]: x1:{:.1f},y1:{:.1f}'.format(boxes[1].x1, boxes[1].y1))
print('boxes[1]: x2:{:.1f},y2:{:.1f}'.format(boxes[1].x2, boxes[1].y2))

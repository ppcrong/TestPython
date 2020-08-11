"""
ref: https://github.com/BusKill/buskill-app/blob/6c84587b25f7ef3b5300d8c0eda354b11051215e/src/buskill.py#L212-L275
"""
import win32api, win32con, win32gui
from ctypes import *

# Device change events (WM_DEVICECHANGE wParam)
DBT_DEVICEARRIVAL = 0x8000
DBT_DEVICEQUERYREMOVE = 0x8001
DBT_DEVICEQUERYREMOVEFAILED = 0x8002
DBT_DEVICEMOVEPENDING = 0x8003
DBT_DEVICEREMOVECOMPLETE = 0x8004
DBT_DEVICETYPESSPECIFIC = 0x8005
DBT_CONFIGCHANGED = 0x0018

# type of device in DEV_BROADCAST_HDR
DBT_DEVTYP_OEM = 0x00000000
DBT_DEVTYP_DEVNODE = 0x00000001
DBT_DEVTYP_VOLUME = 0x00000002
DBT_DEVTYPE_PORT = 0x00000003
DBT_DEVTYPE_NET = 0x00000004

# media types in DBT_DEVTYP_VOLUME
DBTF_MEDIA = 0x0001
DBTF_NET = 0x0002

WORD = c_ushort
DWORD = c_ulong


class DEV_BROADCAST_HDR(Structure):
    _fields_ = [
        ("dbch_size", DWORD),
        ("dbch_devicetype", DWORD),
        ("dbch_reserved", DWORD)
    ]


def triggerWin():
    msg = "DEBUG: BusKill lockscreen trigger executing now"
    print(msg)

    windll.user32.LockWorkStation()


class DEV_BROADCAST_HDR(Structure):
    _fields_ = [
        ("dbch_size", DWORD),
        ("dbch_devicetype", DWORD),
        ("dbch_reserved", DWORD)
    ]


class DEV_BROADCAST_VOLUME(Structure):
    _fields_ = [
        ("dbcv_size", DWORD),
        ("dbcv_devicetype", DWORD),
        ("dbcv_reserved", DWORD),
        ("dbcv_unitmask", DWORD),
        ("dbcv_flags", WORD)
    ]


def drive_from_mask(mask):
    n_drive = 0
    while 1:
        if (mask & (2 ** n_drive)):
            return n_drive
        else:
            n_drive += 1


class Notification:

    def WndProc(self, hwnd, msg, wParam, lParam):
        if msg == win32con.WM_PAINT:
            print('WM_PAINT')
            hdc, ps = win32gui.BeginPaint(hwnd)
            rect = win32gui.GetClientRect(hwnd)
            win32gui.DrawText(hdc, 'GUI Python', len('GUI Python'), rect,
                              win32con.DT_SINGLELINE | win32con.DT_CENTER | win32con.DT_VCENTER)
            win32gui.EndPaint(hwnd, ps)
        if msg == win32con.WM_DESTROY:
            print('WM_DESTROY')
            win32gui.PostQuitMessage(0)
        if msg == win32con.WM_DEVICECHANGE:
            print('WM_DEVICECHANGE')
            self.hotplugCallbackWin(hwnd, msg, wParam, lParam)
        return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)

    def __init__(self):
        print('init notify window')
        message_map = {
            win32con.WM_DEVICECHANGE: self.hotplugCallbackWin
        }

        wc = win32gui.WNDCLASS()
        hinst = wc.hInstance = win32api.GetModuleHandle(None)
        wc.lpszClassName = "DeviceChangeDemo"
        wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
        wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        wc.hbrBackground = win32con.COLOR_WINDOW
        wc.lpfnWndProc = self.WndProc
        classAtom = win32gui.RegisterClass(wc)
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow(
            classAtom,
            "Device Change Demo",
            style,
            win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
            0, 0,
            hinst, None
        )
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOWNORMAL)
        win32gui.UpdateWindow(self.hwnd)
        win32gui.PumpMessages()

    # this is a callback function that is registered to be called when a usb
    # hotplug event occurs in windows
    # WM_DEVICECHANGE:
    #  wParam - type of change: arrival, removal etc.
    #  lParam - what's changed?
    #    if it's a volume then...
    #  lParam - what's changed more exactly
    def hotplugCallbackWin(self, hwnd, message, wparam, lparam):
        dev_broadcast_hdr = DEV_BROADCAST_HDR.from_address(lparam)
        print(f'dev_broadcast_hdr:{dev_broadcast_hdr}')
        print(f'wparam:{wparam:08X}')
        print(f'lparam:{lparam:08X}')

        if wparam == DBT_DEVICEREMOVECOMPLETE:
            triggerWin()

            msg = "hwnd:|" + str(hwnd) + "|"
            print(msg)

            msg = "message:|" + str(message) + "|"
            print(msg)

            msg = "wparam:|" + str(wparam) + "|"
            print(msg)

            msg = "lparam:|" + str(lparam) + "|"
            print(msg)

            dev_broadcast_volume = DEV_BROADCAST_VOLUME.from_address(lparam)
            msg = "dev_broadcast_volume:|" + str(dev_broadcast_volume) + "|"
            print(msg)

            drive_letter = drive_from_mask(dev_broadcast_volume.dbcv_unitmask)
            msg = "drive_letter:|" + str(drive_letter) + "|"
            print(msg)

            msg = "ch( ord('A') + drive_letter):|" + str(chr(ord('A') + drive_letter)) + '|'
            print(msg)

        return 1


if __name__ == '__main__':
    notify = Notification()

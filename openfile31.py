import ctypes
from ctypes import wintypes

OFN_ENABLEHOOK = 0x00000020
# OFN_EXPLORER = 0x00080000  ← If this value is set, the Win95 style dialog will appear instead of Win31 style.

LPOFNHOOKPROC = ctypes.WINFUNCTYPE(
    wintypes.UINT, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)

def dummy_hook(hdlg, uiMsg, wParam, lParam):
    return 0

class OPENFILENAMEW(ctypes.Structure):
    _fields_ = [
        ("lStructSize",      wintypes.DWORD),
        ("hwndOwner",        wintypes.HWND),
        ("hInstance",        wintypes.HINSTANCE),
        ("lpstrFilter",      wintypes.LPCWSTR),
        ("lpstrCustomFilter",wintypes.LPWSTR),
        ("nMaxCustFilter",   wintypes.DWORD),
        ("nFilterIndex",     wintypes.DWORD),
        ("lpstrFile",        wintypes.LPWSTR),
        ("nMaxFile",         wintypes.DWORD),
        ("lpstrFileTitle",   wintypes.LPWSTR),
        ("nMaxFileTitle",    wintypes.DWORD),
        ("lpstrInitialDir",  wintypes.LPCWSTR),
        ("lpstrTitle",       wintypes.LPCWSTR),
        ("Flags",            wintypes.DWORD),
        ("nFileOffset",      wintypes.WORD),
        ("nFileExtension",   wintypes.WORD),
        ("lpstrDefExt",      wintypes.LPCWSTR),
        ("lCustData",        wintypes.LPARAM),
        ("lpfnHook",         LPOFNHOOKPROC),
        ("lpTemplateName",   wintypes.LPCWSTR),
        ("pvReserved",       wintypes.LPVOID),
        ("dwReserved",       wintypes.DWORD),
        ("FlagsEx",          wintypes.DWORD),
    ]

ofn = OPENFILENAMEW()
ofn.lStructSize = ctypes.sizeof(OPENFILENAMEW)
file_buffer = ctypes.create_unicode_buffer(260)
ofn.lpstrFile = ctypes.cast(file_buffer, wintypes.LPWSTR)
ofn.nMaxFile = 260
ofn.lpstrTitle = "Windows 3.1 Style Dialog"
ofn.Flags = OFN_ENABLEHOOK
hook_func_ptr = LPOFNHOOKPROC(dummy_hook)  # Necessary to prevent GC(Garbage Collector)
ofn.lpfnHook = hook_func_ptr

success = ctypes.windll.comdlg32.GetOpenFileNameW(ctypes.byref(ofn))
if success:
    print(f"Selected file: {ofn.lpstrFile}")
else:
    print("Task cancelled or closed by user.")

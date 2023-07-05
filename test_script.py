import pygetwindow as gw
import win32gui
import win32ui

def get_window_position():
    # Get the position of the RuneLite window
    runelite_window = gw.getWindowsWithTitle("RuneLite")[0]
    x, y = runelite_window.left, runelite_window.top

    return x, y

# Function to overlay a rectangle on the RuneLite window
def overlay_rectangle(window, x, y, width, height):
    hwnd = window._hWnd
    rect = (x, y, x + width, y + height)

    dc = win32gui.GetWindowDC(hwnd)
    dc_obj = win32ui.CreateDCFromHandle(dc)
    pen = win32ui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(255, 0, 0))
    dc_obj.SelectObject(pen)
    dc_obj.Rectangle(rect)

    dc_obj.DeleteDC()
    win32gui.ReleaseDC(hwnd, dc)

# Find the RuneLite window
runelite_window = gw.getWindowsWithTitle("RuneLite")[0]

# Define the position and size of the inventory zone
inventory_x = 100  # Modify the values based on your inventory position
inventory_y = 200  # Modify the values based on your inventory position
inventory_width = 200  # Modify the values based on your inventory size
inventory_height = 150  # Modify the values based on your inventory size

# Overlay the rectangle on the RuneLite window
overlay_rectangle(runelite_window, inventory_x, inventory_y, inventory_width, inventory_height)

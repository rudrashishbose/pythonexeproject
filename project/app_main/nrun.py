import ctypes

def nrun():
    message = "This is the nrun function."
    ctypes.windll.user32.MessageBoxW(0, message, "Message", 1)

if __name__ == "__main__":
    nrun()

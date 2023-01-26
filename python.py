import pyautogui,time
posisi = pyautogui.position()
pesan = "=== Tes Hacking With Solaris Dark Net ==="
for a in range (1000000):
    pyautogui.click(posisi.x,posisi.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])

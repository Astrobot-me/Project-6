import pyautogui
import time
# import asyncio,aiofiles

search_button_x=980
search_button_y=649

input_x=68
input_y=667


# Specify the file path
file_path = '2610to3110.txt'
print("switch to window")
time.sleep(5)

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read and print each line
    for line in file.readlines():
        a = line.rstrip() 
        # a = line.rstrip()
        # pyautogui.sleep(1)
        pyautogui.click(input_x, input_y)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        # pyautogui.sleep(0.2) # strip() removes leading and trailing whitespaces (including newline characters)
        if a:
            time.sleep(0.5)
            pyautogui.write(a)
            print(f"{a} is written")
        # pyautogui.press("enter")
         
        pyautogui.click(search_button_x, search_button_y)
        print(f"{a} Submitted \n")
        # pyautogui.sleep(0)
        time.sleep(1)
        file.close()
        

# async def open_and_read_file(file_path):
#     async with aiofiles.open(file_path, mode='r') as file:
#         content = await file.readline()
#         return content


# async def main():
#     # file_path = '2109_to_2509_D4.txt'
#     a = await open_and_read_file(file_path)

#     pyautogui.sleep(1)
#     pyautogui.click(input_x, input_y)
#     pyautogui.hotkey('ctrl', 'a')
#     pyautogui.press('backspace') # strip() removes leading and trailing whitespaces (including newline characters)
#     pyautogui.write(a)
#     print(f"{a} is written")
#     # pyautogui.press("enter")
#     pyautogui.click(search_button_x, search_button_y)
#     print(f"{a} Submitted \n")
#     await asyncio.sleep(1)


# with open(file_path, 'r') as file:
# #     # Read and print each line
#     for line in file:
#         asyncio.run(main())

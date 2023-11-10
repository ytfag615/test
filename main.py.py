
# guess_the_number_game.py
import random
import xml.etree.ElementTree as ET

def load_game_settings(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    max_attempts = int(root.find('max_attempts').text)
    return x1, x2, max_attempts

def guess_the_number(x1, x2, max_attempts):
    target_number = random.randint(x1, x2)
    attempts = 0

    print(f"猜数字游戏开始！目标数字在 {x1} 和 {x2} 之间。")

    while attempts < max_attempts:
        guess = int(input("请输入你的猜测数字: "))

        if guess == target_number:
            print(f"恭喜！你猜对了，目标数字是 {target_number}。")
            break
        elif guess < target_number:
            print("你的猜测太低了，请再试一次。")
        else:
            print("你的猜测太高了，请再试一次。")

        attempts += 1

    if attempts == max_attempts:
        print(f"很抱歉，你已经达到最大尝试次数 {max_attempts}，游戏结束。目标数字是 {target_number}。")

if __name__ == "__main__":
    file_path = "game_settings.xml"
    x1, x2, n = load_game_settings(file_path)
    guess_the_number(x1, x2, n)

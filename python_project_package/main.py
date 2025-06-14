from user import UserManager
import os
import time

os.system("cls")

def main():
    manager = UserManager()

    while True:

        try:
            answer = int(input("유저 추가: 1\n목록 보기: 2\n종료: 3\n: "))

            os.system("cls")

            if answer == 1:
                manager.add_user(input("유저의 이름을 입력해 주세요\n: "), input("유저의 이메일을 입력해 주세요\n: "))
                print("유저가 성공적으로 추가 되었습니다!")
                time.sleep(3)

            elif answer == 2:
                print("이름 - 이메일\n" + "-" * 13)
                for user in manager.list_users():
                    print(f"{user['username']} - {user['email']}")
                input("\n나가기 위해 아무 단어나 입력\n: ")

            elif answer == 3:
                break

            else:
                os.system("cls")
                print("1, 2, 3 중에서 선택해 주세요\n")
                continue

            os.system("cls")

        except:
            os.system("cls")
            print("1, 2, 3 중에서 선택해 주세요\n")
            continue

if __name__ == "__main__":
    main()
print("종료되었습니다")
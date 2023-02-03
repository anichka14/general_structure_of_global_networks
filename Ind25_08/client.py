import socket
import re


# функція, яка буде відповідати програмі клієнта
def run_client(host, port):
    s = socket.socket()
    s.connect((host, port))
    print(f"Під`єднано до {host}:{port}")

    # після цих дій відбувається обмін даними

    while True:
        expression = input("Введіть арифметичний вираз: ")
        # зробимо обмін даними
        if expression == "":
            s.sendall(b"")
            break
        if not re.search(EXPRESSION, str(expression)):
            print("Вираз неправильний. Спробуйте знову")
        else:
            out_b = bytes(expression, encoding="utf-8")  # переводимо у байти цей рядок
            # відправляємо байти на сервер
            s.sendall(out_b)
            print(f"Відправлено на сервер {out_b}")
            inp_b = s.recv(1024)
            print("Отримано з сервера")
            inp_s = str(inp_b, encoding="utf-8")
            print(inp_s)

    s.sendall(b"")

    s.close()
    print("Клієнт завершив роботу")


EXPRESSION = r"^(?P<num1>\d+)\s(?P<sign>\+|\-|\*{1,2}|\/{1,2})\s(?P<num2>\d+)$"
HOST = "127.0.0.1"
PORT = 5000


if __name__ == "__main__":
    run_client(HOST, PORT)

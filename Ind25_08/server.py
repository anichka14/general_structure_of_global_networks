import socket
import operator


def calculate(a, b, op):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow,
        "//": operator.floordiv
    }
    return ops[op](int(a), int(b))


def run_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # передаємо сім`ю протоколів IP та TCP

    try:
        # прив`яжемо сервер до даного хосту і порту
        s.bind((host, port))

        # запускаємо сервер
        s.listen()  # сервер буде очікувати на те, щоб клієнт під`єднувався до нього
        print("Сервер запущено")

        # опишемо команду в якій клієнт приєднується до сервера
        conn, address = s.accept()  # дана функція повертає об`єкт типу socket, connection i address клієнта
        print(f"Під`єднано {address}")

        while True:
            # приймаємо дані
            inp = conn.recv(1024).decode()
            print(f"Отримано {inp}")
            if not inp:  # якщо пустий рядок
                break

            a, op, b = inp.split()
            out = calculate(a, b, op)
            out_b = bytes(str(out), encoding="utf-8")
            # відправляємо рядок клієнту
            conn.sendall(out_b)
            print(f"Відправлення {out}")
            print(out)

        conn.close()
        print(f"Від`єднано {address}")
        s.close()
        print("Сервер завершив роботу")

    except Exception as e:
        print(e)


HOST = ""
PORT = 5000


if __name__ == "__main__":
    run_server(HOST, PORT)

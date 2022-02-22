import time


def main():
    while True:
        option = int(input("Enter Value:\n1.Start\t 2.Stop\t 3.Exit\n"))
        if option == 1:
            start_time = time.time()
        if option == 2:
            print(f"Time Elapsed(seconds) --> {time.time() - start_time}")
        if option == 3:
            break


if __name__ == "__main__":
    main()




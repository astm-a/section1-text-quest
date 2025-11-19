import random;
import os;

clear = lambda:os.system('cls');
try:
    def start_quest():
        clear();
        print("Гуляя по улице, вам в глаза бросается вывеска казино. Хотите ли вы войти ?");
        print("1. Да");
        print("2. Нет!");
        enter = input("Выберите действие (1 или 2): ");

        if enter == "1":
            clear();
            print("Вы входите в казино и перед вами выбор: \n1. рулетка\n2. Покер \n3. 'Однорукий бандит'");
            choice = input("Выберите действие (1, 2 или 3): ");
            if choice == "1":
                ruletka();
            elif choice =="2":
                clear();
                print("К сожелени. покер пока не доступен (");
                start_quest();
            elif choice == "3":
                clear();
                print("'Однорукий бандит' сейчас в ремонте");
                start_quest();

        elif enter == "2":
            clear();
            print("Вы прошли мимо казино");
        else:
            print("Неверный выбор. Попробуй снова.");
            start_quest();

    def ruletka():
        clear();
        print("\nДобро пожаловать в Рулетку!");
        num = input("Загадай число от 0 до 32 и запиши его: ");

        num = int(num)
        if num < 0 or num > 32:
            print("Число должно быть от 0 до 32.");
            ruletka();
            return

        roulette_num = random.randint(0, 32);
        print(f"Выпало: {roulette_num}");

        if num == roulette_num:
            print("Угадал! Поздравляем, ты везунчик.");
        else:
            print("Не угадал. Хочешь попробуешь ещё раз?");

        again = input("Сыграем ещё? (да/нет): ");
        if again == "да":
            ruletka();
        else:
            print("Спасибо за игру!");

except(Exception):
    print("Непредвиденная ошибка");

start_quest();

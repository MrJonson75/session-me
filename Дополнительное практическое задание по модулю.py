import time
from random import randint


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.current_video = ""
        self.current_duration = 0
        self.current_time_now = 0
        self.v_acc = False

    def __str__(self):
        return self.current_user, self.users, self.videos

    def log_out(self):
        my_output = input("Хотите выйте из акаунта Y/N: ")
        if my_output.upper() == "Y":
            self.current_user = None
            self.nickname = ""
            self.password = hash('')
            self.age = 0
        else:
            return self.current_user

        return self.current_user

    def login_form(self):
        self.nickname = input("Введите логин: ")
        self.password = hash(input("Введите пароль: "))
        return self.nickname, self.password

    def log_in(self, nickname, password, age):
        my_user = False
        self.nickname = nickname
        self.password = password
        self.age = age
        self.login_form()
        if self.users == []:
            print("список пользователей пуст")
            self.age = int(input("Введите возраст: "))
            self.register(nickname=self.nickname, password=self.password, age=self.age)
        else:
            for user in self.users:
                if user[0] == self.nickname:
                    my_user = True
                    for i in range(3):
                        if user[1] != self.password:
                            print("Неправельный пароль")
                            self.password = hash(input("Введите пароль: "))
                        else:
                            self.current_user = self.nickname
                            self.age = user[2]
                            break
                    break
                else:
                    my_user = False

            if my_user == False:
                print("=============пользователь не найден===================")
                user_new = input("Добавить? Y/N:")
                if user_new.upper() == "Y":
                    self.age = int(input("Введите возраст: "))
                    self.register(nickname=self.nickname, password=self.password, age=self.age)

        return current_user

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        user = [self.nickname, self.password, self.age]
        self.users.append(user)
        print(f"Пользователь {self.nickname} зарегистрирован")
        print("================================================================================")

    def add_Video(self, fid, title, duration, time_now, adult_mode):
        my_p = False
        self.fid = fid
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.title = input("Введите заголовок фильма: ")
        if self.videos == []:
            self.fid = 1
        else:
            final_element = self.videos[-1]
            self.fid = final_element[0] + 1

        self.duration = randint(10, 25)  # продолжительность, секунды
        self.time_now = 0  # секунда остановки (изначально 0)

        self.adult_mode = False  # ограничение по возрасту, bool (False по умолчанию)
        if self.videos == []:
            video = [self.fid, self.title, self.duration, self.time_now, self.adult_mode]
            self.videos.append(video)
            print(f"\033[31mФильм     {self.title} добавлен\033[0m")
            print("\033[31m================================================================================\033[0m")
        else:
            for i in self.videos:
                if i[1] == self.title:
                    my_p = False
                    break
                else:
                    my_p = True
            if my_p == True:
                video = [self.fid, self.title, self.duration, self.time_now, self.adult_mode]
                self.videos.append(video)
                print(f"\033[31mФильм     {self.title} добавлен\033[0m")
                print("\033[31m============================================================================\033[0m")
            else:
                print(f"\033[31m Фильм  {self.title} уже существует на хостинге \033[0m")
                time.sleep(4)

    def list_video(self):
        if self.videos == []:
            print("\033[34m Список фильмов пуст: \033[0m")
        else:
            for list in self.videos:
                print(f"\033[34m Фильм: {list}\033[0m")
        time.sleep(4)
    def get_videos(self):
        my_serch_list = []
        my_serch_bool = False
        if self.videos == []:
            print("\033[34m Список фильмов пуст: \033[0m")
        else:
            my_serch = input("Введите поисковое слово: ")
            for i in self.videos:
                if i[1].find(my_serch) != -1:
                    my_serch_bool = True
                    my_serch_list.append(i[1])

        if my_serch_bool == True:
            for j in my_serch_list:
                print(f"\033[34m Фильм: {j}\033[0m")
            time.sleep(4)
        else:
            print("\033[33m Совпадений не найдено\033[0m")
    def video_access(self):
        if self.videos == []:
            print("\033[34m Список фильмов пуст: \033[0m")
            self.v_acc = False
        else:
            if self.age < 18:
                print("\033[31m Фильм не доступен Вам меньше 18 лет \033[0m")
                self.v_acc = False
            else:
                for i in range(len(self.videos)):
                    self.videos[i][4] = True
                self.v_acc = True
        return self.v_acc
    def watch_video(self):
        self.video_access()
        if self.v_acc == True:
            self.current_video = input("Введите название фильма для воспроизведения: ")
            for i in self.videos:
                if i[1] == self.current_video and i[4] == True:
                    self.current_duration =i[2]
                    self.current_time_now =i[3]
                    print()
                    print()
                    print()
                    print()
                    print()
                    print(f"\033[34m Воспроизводится:  {self.current_video}\033[0m")
                    print()
                    print()
                    for j in range(self.current_duration):
                        self.current_time_now = j
                        print("\033[35m * \033[0m", end="")
                        print(self.current_time_now, sep="", end="")
                        time.sleep(1)
                    print("\033[31m   Конец видео\033[0m")
                    time.sleep(4)


    pass


class Video:
    def __init__(self):
        self.fid = 0
        self.title = ""
        self.duration = 0
        self.time_now = 0
        self.adult_mode = False

    def __str__(self):
        return self.title, self.duration, self.time_now, self.adult_mode

    pass


class User:
    def __init__(self):
        self.nickname = ""
        self.password = hash('')
        self.age = 0

    def __str__(self):
        return self.nickname, self.password, self.age



    pass


current_user = UrTube()
user = User()
video = Video()

while current_user.current_user == None:
    UrTube.log_in(self=current_user, nickname=user.nickname, password=user.password, age=user.age)
    while current_user.current_user != None:
        print(f"\033[31m           Приветствую {current_user.current_user} на видео хостинге UrTube\033[0m")
        print("                                                          ")
        print("\033[33m            *________________________________*\033[0m")
        print("\033[33m            *    1. Найти видео.             *\033[0m")
        print("\033[33m            *    2. Добавить видео.          *\033[0m")
        print("\033[33m            *    3. Просмотр видео.          *\033[0m")
        print("\033[33m            *    4. Выйти из акаунта.        *\033[0m")
        print("\033[33m            *    5. Вывести список видео.   *\033[0m")
        print("\033[33m            *________________________________*\033[0m")
        print("                                                          ")
        my_menu = int(input("               Выберете от 1 до 5: "))
        if my_menu == 4:
            UrTube.log_out(current_user)  # Метод log_out для сброса текущего пользователя на None
        elif my_menu == 2:
            UrTube.add_Video(self=current_user, fid=video.fid, title=video.title, duration=video.duration,
                             time_now=video.time_now, adult_mode=video.adult_mode)
        elif my_menu == 5:
            UrTube.list_video(current_user)
        elif my_menu == 1:
            UrTube.get_videos(current_user)
        elif my_menu == 3:
            UrTube.watch_video(current_user)

        else:
            continue



import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    video = []
    check_video = False

    def __init__(self, users=None, videos=None):
        self.users = users
        self.user = []
        self.verify_user = 0
        self.videos = videos
        self.current_user = None
        self.search_video = ""
        self.get_video = ""

    def add(self, *args):
        for i in args:
            self.video = [i.title, i.duration, i.time_now, i.adult_mode]
            if self.videos is None:
                self.videos = []
                self.videos.append(self.video)
            else:
                for j in self.videos:
                    if i.title != j[0]:
                        self.check_video = True
                    else:
                        self.check_video = False
                        break
                if self.check_video is True:
                    self.videos.append(self.video)
                else:
                    print(f"\033[31m фильм {i.title} уже существует !!! \033[0m")
                    time.sleep(1)
            self.video = []

    def get_videos(self, search_video):
        self.search_video = search_video.lower()
        my_search_list = []
        for i in self.videos:
            my_str = i[0]
            my_str = my_str.lower()
            if my_str.find(self.search_video) != -1:
                my_search_list.append(i[0])
        return my_search_list

    def watch_video(self, get_video):
        self.get_video = get_video
        if self.current_user is not None:  # Проверка авторизации пользователя

            """Ниже модуль сравнения запроса и воспроизведения видео"""

            for i in self.videos:
                if i[0] == self.get_video and i[3] is True:
                    current_duration = i[1]

                    """Сюда вставить проверку возвраста"""
                    if self.user[2] > 18:
                        print(f"\033[34m Воспроизводится:  {self.get_video}\033[0m")
                        for j in range(current_duration):
                            current_time_now = j
                            print("\033[35m * \033[0m", end="")
                            print(current_time_now, sep="", end="")
                            time.sleep(1)
                        print("\033[31m   Конец видео\033[0m")
                        time.sleep(2)
                    else:
                        print("\033[31m Вам нет 18 лет, пожалуйста покиньте страницу\033[0m")
                    # выход из акаeyn
                    self.log_out()
        else:
            print("\033[31mВойдите в аккаунт чтобы смотреть видео\033[0m")

    def register(self, nickname, password, age):
        self.user = [nickname, password, age]
        if self.users is None:
            self.users = []
        else:
            for i in self.users:
                if i[0] == self.user[0]:  # Проверка имени пользователя
                    self.log_in(self.user[0], self.user[1])  # Авторизация

        if self.verify_user == 0:  # Если пользователь не найден добавляем и автоматическая авторизация
            self.users.append(self.user)
            self.log_in(self.user[0], self.user[1])
            print(f"\033[32m Пользователь {self.user[0]} авторизован\033[0m")
            self.verify_user = 0
        elif self.verify_user == 1:  # Авторизация успешна
            print(f"\033[32m Пользователь {self.user[0]} авторизован\033[0m")
            self.verify_user = 0
        elif self.verify_user == 2:  # Авторизация не успешна
            print(f"\033[32m Пользователь {self.user[0]} уже существует\033[0m")
            self.verify_user = 0

    def log_in(self, login, password):
        for i in self.users:
            if i[0] == login and i[1] == password:
                self.current_user = self.user
                self.verify_user = 1
            elif i[0] == login and i[1] != password:
                self.verify_user = 2
        return self.verify_user

    def log_out(self):
        self.current_user = None


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)
p1 = User('vasya_pupkin', 'lolkekcheburek', 13)
p2 = User('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
p3 = User('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register(p1.nickname, p1.password, p1.age)
print(f"\033[32m Текущий пользователь {ur.user[0]} ему {ur.user[2]} лет\033[0m")
ur.watch_video('Для чего девушкам парень программист?')
ur.register(p2.nickname, p2.password, p2.age)
print(f"\033[32m Текущий пользователь {ur.user[0]} ему {ur.user[2]} лет\033[0m")
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register(p3.nickname, p3.password, p3.age)

print(" Попытка воспроизведения несуществующего видео")
ur.register(p2.nickname, p2.password, p2.age)
print(f"\033[32m Текущий пользователь {ur.user[0]} ему {ur.user[2]} лет\033[0m")
ur.watch_video('Лучший язык программирования 2024 года!')

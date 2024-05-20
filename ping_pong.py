import pygame  # Import biblioteki Pygame do obsługi grafiki i interakcji
import sys  # Import modułu sys, który zapewnia dostęp do zmiennych i funkcji obsługujących interpreter Pythona
import random  # Import modułu random do generowania losowych liczb


# stałe określające prędkość gracza, piłki, szerokość oraz długość okna gry, ilość klatek na sekundę
PLAYER_SPEED = 7
BALL_SPEED = 6
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
FPS = 60


def exit_game():  # Funkcja obsługująca wyjście z gry
    for event in pygame.event.get():  # Iteracja przez wszystkie zgłoszone zdarzenia w grze
        if event.type == pygame.QUIT:  # Sprawdzenie, czy zgłoszone zdarzenie to zamknięcie okna gry
            pygame.quit()  # Wyjście z biblioteki Pygame
            sys.exit()  # Wyjście z interpretera Pythona


def ball_movement():  # Funkcja obsługująca ruch piłki
    global ball_speed_x, ball_speed_y, player_score, opponent_score  # Deklaracja globalnych zmiennych
    ball.x += ball_speed_x  # Zmiana pozycji piłki w osi X
    ball.y += ball_speed_y  # Zmiana pozycji piłki w osi Y

    # Sprawdzenie warunków dotyczących wyjścia piłki poza ekran
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        pygame.mixer.Sound.play(sd_pong)
        ball_speed_y *= -1  # Odwrócenie kierunku ruchu piłki w osi Y

    if ball.left <= 0:  # jeśli piłka wyszła za lewą granicę okna gry
        pygame.mixer.Sound.play(random.choice(sd_point))  # dźwięk komentarzu zdobycia punktu losowy z podanej listy
        player_score += 1  # Zwiększenie wyniku gracza o 1
        ball_restart()  # Restart pozycji piłki

    if ball.right >= SCREEN_WIDTH:  # jeśli piłka wyszła za prawą granicę okna gry
        pygame.mixer.Sound.play(random.choice(sd_point))
        opponent_score += 1  # Zwiększenie wyniku przeciwnika o 1
        ball_restart()  # Restart pozycji piłki

    # Sprawdzenie warunku dotyczącego kolizji piłki z paletką gracza lub przeciwnika
    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.Sound.play(random.choice(sd_bounce))  # dźwięk komentarzu odbica od paletki
        ball_speed_x *= -1  # Odwrócenie kierunku ruchu piłki w osi X


def player_movement():  # Funkcja obsługująca ruch gracza
    global player_speed
    keys = pygame.key.get_pressed()  # Pobranie stanu klawiszy
    if keys[pygame.K_UP]:
        player_speed = -PLAYER_SPEED  # Ustawienie prędkości gracza w górę
    elif keys[pygame.K_DOWN]:
        player_speed = PLAYER_SPEED  # Ustawienie prędkości gracza w dół
    else:
        player_speed = 0  # Zatrzymanie gracza

    player.y += player_speed  # Zmiana pozycji gracza w osi Y

    # Warunki zapobiegające wyjściu paletki gracza poza ekran
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def player2_movement():  # Funkcja obsługująca ruch gracza 2 (jeśli gra dwóch graczy)
    global player2_speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player2_speed = -PLAYER_SPEED
    elif keys[pygame.K_s]:
        player2_speed = PLAYER_SPEED
    else:
        player2_speed = 0

    opponent.y += player2_speed

    # Warunki zapobiegające wyjściu paletki gracza 2 poza ekran
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT


def opponent_movement():  # Funkcja obsługująca ruch przeciwnika (jeśli gra z botem)
    # Sprawdzenie, czy piłka jest nad paletką przeciwnika i przesunięcie paletki w górę
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    # Sprawdzenie, czy piłka jest poniżej paletki przeciwnika i przesunięcie paletki w dół
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # Zapobieganie wyjściu paletki przeciwnika poza górny brzeg ekranu
    if opponent.top <= 0:
        opponent.top = 0
    # Zapobieganie wyjściu paletki przeciwnika poza dolny brzeg ekranu
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT


def ball_restart():  # Funkcja restartująca pozycję piłki
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Ustawienie pozycji piłki na środku ekranu
    ball_speed_x *= random.choice((-1, 1))  # Losowa zmiana kierunku ruchu piłki w osi X
    ball_speed_y *= random.choice((-1, 1))  # Losowa zmiana kierunku ruchu piłki w osi Y


if __name__ == "__main__":

    pygame.mixer.pre_init(44100, -16, 2, 512)
    # Inicjalizacja miksowania dźwięku: częstotliwość 44100 Hz, 16-bit, stereo, bufor 512
    pygame.init()  # Inicjalizacja biblioteki Pygame

    # Menu
    print("GRA W PING PONGA")
    print("Wybierz tryb gry:")
    print("1 - Gra z botem (sterowanie strzałkami)")
    print("2 - Gra dwóch graczy (sterowanie strzałkami oraz klawiszami W i S)")

    game_mode = input("Twój wybór: ")  # Wybranie przez gracza trybu gry

    if game_mode == '1':
        opponent_speed = PLAYER_SPEED  # Jeśli wybrano tryb gry z botem, prędkość przeciwnika = prędkość gracza
    elif game_mode == '2':
        opponent_speed = 0  # Przy wybprze drugiego trybu gry, prędkość przeciwnika = 0 (gracz steruje obiema paletkami)
    else:
        print("Niepoprawny wybór trybu gry.")
        pygame.quit()  # Wyjście z biblioteki Pygame
        sys.exit()  # Wyjście z interpretera Pythona

    clock = pygame.time.Clock()  # Obiekt zegara, który można użyć do kontrolowania liczby klatek na sekundę w grze
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Utworzenie ekranu gry o określonych wymiarach
    pygame.display.set_caption('PING PONG - KOTECKI, RADECKI, JÓZWIAK')  # Ustawienie tytułu okna gry

    # Dźwięki - sd(sound)
    sd_pong = pygame.mixer.Sound("sounds\\pong.wav")
    sd_start = pygame.mixer.Sound("sounds\\321start.mp3")

    # Grupy dźwięków
    # Utworzenie listy dźwięków przy zdobyciu punktu
    sd_point = [pygame.mixer.Sound(f"sounds\\wik{i}.mp3") for i in range(1, 7)] + \
                [pygame.mixer.Sound(f"sounds\\mik{i}.mp3") for i in range(1, 4)]
    # Utworzenie listy dźwięków przy odbiciu paletki piłki od paletki
    sd_bounce = [pygame.mixer.Sound(f"sounds\\mik{i}.mp3") for i in range(4, 9)] + \
                [pygame.mixer.Sound(f"sounds\\rad{i}.mp3") for i in range(1, 12)]

    pygame.mixer.Sound.play(sd_start)  # Odtworzenie dźwięku przypisanego do zmiennej sd_start
    # opóźnienie 4 sekund
    pygame.time.delay(4000)

    # Prostokąty (Rectangles) reprezentujące piłkę i paletki
    # rect = pygame.Rect(left, top, width, height)
    # left - odległość od lewej krawędzi okna, top - odległość od górnej krawędzi okna
    # width - szerokość prostokąta, height - wysokość prostokąta
    # Przykład: rect = pygame.Rect(100, 150, 50, 75) tworzy prostokąt o współrzędnych (100, 150) i wymiarach 50x75.
    ball = pygame.Rect(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 - 10, 20, 20)
    player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - 60, 10, 120)
    opponent = pygame.Rect(10, SCREEN_HEIGHT / 2 - 60, 10, 120)

    # Kolory
    white = pygame.Color('white')
    blue = pygame.Color('blue4')

    # Predkość piłki i graczy
    ball_speed_x = BALL_SPEED * random.choice((-1, 1))  # Ustawienie losowego kierunku piłki w prawo albo w lewo
    ball_speed_y = BALL_SPEED * random.choice((-1, 1))  # Ustawienie losowego kierunku piłki w górę albo w dół
    player_speed = 0
    player2_speed = 0

    # Tekst - wyniki
    player_score = 0
    opponent_score = 0
    game_font = pygame.font.Font("font\\RubikMonoOne-Regular.ttf", 48)  # Ustawienie czcionki do wyświetlania wyników

    while True:  # Główna pętla gry - pętla nieskończona

        exit_game()
        ball_movement()
        player_movement()

        if game_mode == '2':
            # Wywołanie funkcji obsługującej ruch paletki przeciwnika (jeśli gra dwóch graczy)
            player2_movement()
        else:
            # Wywołanie funkcji obsługującej ruch przeciwnika (jeśli gra z botem)
            opponent_movement()

        # Wizualizacja planszy z paletkami i piłką
        screen.fill(blue)  # wypełnienie okna gry kolorem
        pygame.draw.rect(screen, white, player)
        # narysowanie:  obiektu rectangle player w oknie gry (screen), o kolorze white
        pygame.draw.rect(screen, white, opponent)
        pygame.draw.ellipse(screen, white, ball)
        # Linia środkowa
        pygame.draw.aaline(screen, white, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        # Wyświetlenie wyników graczy na ekranie
        player_text = game_font.render(f"{player_score}", False, white)  # Renderowanie tekstu z fontem
        # Umieszczenie tekstu przeciwnika na ekranie w określonym miejscu (x=400, y=40)
        screen.blit(player_text, (520, 40))  # blit - na powierzchni screena

        opponent_text = game_font.render(f"{opponent_score}", False, white)
        screen.blit(opponent_text, (400, 40))

        # Odświeżenie zawartości okna
        pygame.display.flip()
        # Ustawienie liczby klatek na sekundę
        clock.tick(FPS)

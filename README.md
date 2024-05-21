# Gra w PONGA

Gra w PONGA, czyli ping ponga 2D, wykonana przez uczniów PLOPŁ, tj. Mikołaj Kotecki, Jan Radecki, Wiktoria Józwiak. Gra została wykonana przy użyciu biblioteki Pygame.

## Opis

Gra PING PONG działa poprzez ciągłe aktualizowanie pozycji piłki i paletek w głównej pętli gry. Gracz kontroluje ruch swojej paletki za pomocą strzałek (lub klawiszy W i S dla drugiego gracza), a przeciwnik porusza się automatycznie lub jest sterowany przez drugiego gracza. Kiedy piłka uderza w krawędź ekranu lub paletkę, jej kierunek jest odpowiednio zmieniany, a dźwięk odtwarzany. Celem gry jest zdobycie jak największej ilości punktów przez graczy poprzez przemieszczenie piłki ruchem paletki, tak aby przeciwnik nie był w stanie odbić piłki. Do gry został dodany również wynik, który się automycznie aktualizuje przy zdobyciu punktu przez jednego z graczy. Dodatkowo gra wyposażona jest w profesjonalny komentarz, posiadający kilkadziesiąt różnych dźwięków.

## Funkcje

- `exit_game()`: Obsługa wyjścia z gry.
- `ball_movement()`: Ruch piłki i wykrywanie kolizji.
- `player_movement()`: Ruch gracza 1.
- `player2_movement()`: Ruch gracza 2.
- `opponent_movement()`: Ruch przeciwnika (bot).
- `ball_restart()`: Restart pozycji piłki.

## Główna pętla gry

```python
while True:
    exit_game()
    ball_movement()
    player_movement()

    if game_mode == '2':
        player2_movement()
    else:
        opponent_movement()

    screen.fill(blue)
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, opponent)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    player_text = game_font.render(f"{player_score}", False, white)
    screen.blit(player_text, (520, 40))

    opponent_text = game_font.render(f"{opponent_score}", False, white)
    screen.blit(opponent_text, (400, 40))

    pygame.display.flip()
    clock.tick(FPS)

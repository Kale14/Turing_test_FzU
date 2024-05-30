# Author: Khalil Hasan
# Data based: https://www.kaggle.com/datasets/prajwaldongre/llm-detect-ai-generated-vs-student-generated-text?resource=download

import pygame
import sys
import random
import numpy as np

# Initialisierung von Pygame
pygame.init()

# Festlegen von Bildschirmabmessungen (für Vollbild)
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 120

# Feste Größen für das zentrale Tile und die Buttons
TILE_WIDTH = 550
TILE_HEIGHT = 380
BUTTON_SIZE = 100
CENTER_AREA_WIDTH = 600
CENTER_AREA_HEIGHT = SCREEN_HEIGHT

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HTWGreen = (118, 185, 0)
GREEN = (0, 100, 0)
RED = (220, 20, 60)

# Schriftarten
title_font_size = 60
title_font = pygame.font.Font(None, title_font_size)
font_size = 31
font = pygame.font.Font(None, font_size)
small_font_size = 27
small_font_two_size = 24
small_font = pygame.font.Font(None, small_font_size)
small_font_two = pygame.font.Font(None, small_font_two_size)
# Lade Icon-Bilder
icon_brain = pygame.image.load('images/ai.png')  # Pfad zu deinem Gehirn-Icon
icon_person = pygame.image.load('images/benutzer.png')  # Pfad zu deinem Personen-Icon


# Lade Hintergrundbilder
background_image_1 = pygame.image.load('images/responsive-piktos-01.png')
background_image_2 = pygame.image.load('images/responsive-piktos-02.png')

# Liste von Aussagen mit Kennzeichnung ("human" oder "machine")
all_statements = [
    {"text": "Warum bist du immer zu spät zu den Meetings?", "label": "mensch"},
    {"text": "Das Projektteam verfolgte einen nutzerzentrierten Designansatz für die Produktentwicklung.", "label": "maschine"},
    {"text": "Ich mag es nicht, mich mit Risiken zu befassen, das ist zu stressig.", "label": "mensch"},
    {"text": "Ich mache mir keine Sorgen um Zuverlässigkeit, es ist gut genug.", "label": "mensch"},
    {"text": "Mir ist menschzentriertes Design egal, gib mir einfach das Endprodukt.", "label": "mensch"},
    {"text": "Die Methodik der Studie gewährleistete eine repräsentative Stichprobe über verschiedene Demografien hinweg.", "label": "maschine"},
    {"text": "Mir sind Branchenpraktiken egal, gib mir einfach die Lösung.", "label": "mensch"},
    {"text": "Das Projektteam dokumentierte alle Prozesse zur Transparenz.", "label": "maschine"},
    {"text": "Das Projektteam hielt offene Kommunikationswege aufrecht.", "label": "maschine"},
    {"text": "Die Ergebnisse stimmen mit den bestehenden theoretischen Rahmenbedingungen überein.", "label": "maschine"},
    {"text": "Ich mag keine inklusive Entscheidungsfindung, das dauert zu lange.", "label": "mensch"},
    {"text": "Die Ergebnisse sind in einer logisch organisierten Weise präsentiert.", "label": "maschine"},
    {"text": "Die Forschungsergebnisse haben praktische Implikationen für Fachleute in der Industrie.", "label": "maschine"},
    {"text": "Ich spreche nicht über Einschränkungen, das lässt mich schlecht aussehen.", "label": "mensch"},
    {"text": "Die Forschungsmethodik beinhaltete einen multimethodischen Ansatz für umfassende Daten.", "label": "maschine"},
    {"text": "Mir sind Teilnehmerantworten egal, gib mir einfach die Daten.", "label": "mensch"},
    {"text": "Die Einschränkungen der Studie werden offen anerkannt und die Studiengrenzen berücksichtigt.", "label": "maschine"},
    {"text": "Die Einschränkungen der Studie werden offen diskutiert, mögliche Schwächen werden erkannt.", "label": "maschine"},
    {"text": "Ich mag es nicht, Probleme zu lösen, das ist zu viel Aufwand.", "label": "mensch"},
    {"text": "Mir ist die Entwicklung von Fähigkeiten egal, das ist irrelevant.", "label": "mensch"},
    {"text": "Die Forschungsergebnisse tragen zur theoretischen Grundlage des Fachgebiets bei.", "label": "maschine"},
    {"text": "Das Projektteam verfolgte einen kollaborativen und inklusiven Entscheidungsprozess.", "label": "maschine"},
    {"text": "Ich mache mir keine Sorgen um Voreingenommenheit, das ist unvermeidlich.", "label": "mensch"},
    {"text": "Ich arbeite lieber alleine, Teamarbeit ist zu kompliziert.", "label": "mensch"},
    {"text": "Die Verhaltensökonomie untersucht die psychologischen Faktoren, die wirtschaftliche Entscheidungen beeinflussen.", "label": "maschine"},
    {"text": "Lol, deine Witze sind so lahm.", "label": "mensch"},
    {"text": "Das Projektteam priorisierte transparente Kommunikation mit den Stakeholdern.", "label": "maschine"},
    {"text": "In der Umweltwissenschaft ist die Auswirkung der Abholzung auf die Biodiversität ein kritisches Anliegen.", "label": "maschine"},
    {"text": "Das Forschungsdesign berücksichtigt mögliche störende Variablen.", "label": "maschine"},
    {"text": "Im Bereich der Robotik führt Biomimikry zur Entwicklung effizienterer Roboter.", "label": "maschine"},
    {"text": "Ich mag es nicht, Probleme zu lösen, das ist zu viel Aufwand.", "label": "mensch"},
    {"text": "Ich spreche nicht über Einschränkungen, das lässt mich schlecht aussehen.", "label": "mensch"},
    {"text": "Das Projektteam hielt sich an den Projektzeitplan.", "label": "maschine"},
    {"text": "Ich mache mir keine Sorgen um Genauigkeit, es ist gut genug.", "label": "mensch"},
    {"text": "Es ist wichtig, Quellen in akademischen Schriften richtig zu zitieren.", "label": "maschine"},
    {"text": "Das Projektteam nutzte Feedback, um die Projektergebnisse zu verbessern.", "label": "maschine"},
    {"text": "Mir sind psychologische Faktoren egal, gib mir einfach die Daten.", "label": "mensch"},
    {"text": "Die Einschränkungen der Studie werden offen diskutiert und mögliche Voreingenommenheiten angesprochen.", "label": "maschine"},
    {"text": "Ich verstehe maschinelles Lernen nicht, gib mir einfach das Fazit.", "label": "mensch"},
    {"text": "Das Projektteam zeigte Kreativität bei der Problemlösung.", "label": "maschine"},
    {"text": "Das Projektteam hielt bei der Dateneingabe ein hohes Maß an Genauigkeit ein.", "label": "maschine"},
    {"text": "Ich mag kein kontinuierliches Feedback, das ist zu repetitiv.", "label": "mensch"},
    {"text": "Die Einschränkungen der Studie werden transparent dargestellt, mögliche Herausforderungen werden anerkannt.", "label": "maschine"},
    {"text": "Ich mag keine offene Kommunikation, das ist zu zeitaufwendig.", "label": "mensch"},
    {"text": "Mir ist interne Validität egal, das ist zu technisch.", "label": "mensch"},
    {"text": "Ich folge lieber, Führung ist zu viel Verantwortung.", "label": "mensch"}
]



# Variablen zur Zählung der Entscheidungen
correct_guesses = 0
incorrect_guesses = 0
current_statement_index = 0

# Liste zur Speicherung der Ergebnisse der letzten 14 Spiele
last_14_results = []
all_results = []

# Variablen zur Speicherung der Tipps
guesses = []

# Spielzustände
GAME_START = 0
GAME_PLAYING = 1
GAME_TIPS = 2
game_state = GAME_START

# Funktion zur Berechnung der Positionen für das Layout
def calculate_layout(screen_width, screen_height):
    center_x = (screen_width - CENTER_AREA_WIDTH) // 2
    center_y = (screen_height - CENTER_AREA_HEIGHT) // 2

    tile_x = center_x + (CENTER_AREA_WIDTH - TILE_WIDTH) // 2
    tile_y = center_y + (CENTER_AREA_HEIGHT - TILE_HEIGHT) // 2 - 50

    button_y = center_y + CENTER_AREA_HEIGHT - BUTTON_SIZE - 80
    button1_x = center_x + (CENTER_AREA_WIDTH // 2) - BUTTON_SIZE - 20
    button2_x = center_x + (CENTER_AREA_WIDTH // 2) + 20

    return (center_x, center_y, tile_x, tile_y, button1_x, button2_x, button_y)

# Funktion zum Zeichnen von zentriertem Text mit automatischem Zeilenumbruch und anpassbarem Zeilenabstand
def draw_text(surface, text, font, color, rect, padding=10, line_spacing=1.0):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= rect.width - 2 * padding:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    lines.append(current_line.strip())

    # Berechne die gesamte Höhe des Textes mit dem zusätzlichen Zeilenabstand
    line_height = font.get_linesize()
    total_text_height = len(lines) * line_height + (len(lines) - 1) * int(line_height * (line_spacing - 1))

    # Starte das Zeichnen von der vertikalen Mitte des Rechtecks minus halbe Texthöhe
    y = rect.top + (rect.height - total_text_height) // 2

    for line in lines:
        text_surface = font.render(line, True, color)
        text_width = text_surface.get_width()
        # Zeichne die Zeile zentriert im Rechteck
        surface.blit(text_surface, (rect.left + (rect.width - text_width) // 2, y))
        y += line_height * line_spacing

# Funktion zum Zeichnen eines Rechtecks mit abgerundeten Ecken
def draw_rounded_rect(surface, rect, color, shadow_color, radius, shadow_offset=15):
    # Zeichne den Schatten, leicht verschoben
    shadow_rect = pygame.Rect(rect.left + shadow_offset, rect.top + shadow_offset, rect.width, rect.height)
    pygame.draw.rect(surface, shadow_color, shadow_rect, border_radius=20)

    # Zeichne das Hauptrechteck
    pygame.draw.rect(surface, color, rect, border_radius=radius)


# Funktion zum Zeichnen eines Kreises mit Schatten
def draw_circle_with_shadow(surface, color, shadow_color, center, radius, shadow_offset=5):
    shadow_center = (center[0] + shadow_offset, center[1] + shadow_offset)
    pygame.draw.circle(surface, shadow_color, shadow_center, radius)
    pygame.draw.circle(surface, color, center, radius)


# Funktion zum Neustart des Spiels
def restart_game():
    global correct_guesses, incorrect_guesses, current_statement_index, statements, game_state, guesses
    correct_guesses = 0
    incorrect_guesses = 0
    current_statement_index = 0
    guesses = []  # Setze die Liste der Tipps zurück
    statements = random.sample(all_statements, 5)
    game_state = GAME_PLAYING


# Funktion zum Zeichnen des kachelartigen Hintergrunds nur innerhalb eines Rechtecks
def draw_tiled_background(surface, image, rect, y_offset=0):
    img_width, img_height = image.get_size()
    for x in range(rect.left, rect.right, img_width):
        for y in range(rect.top + y_offset, rect.bottom, img_height):
            if x + img_width > rect.right:
                clipped_width = rect.right - x
            else:
                clipped_width = img_width

            if y + img_height > rect.bottom:
                clipped_height = rect.bottom - y
            else:
                clipped_height = img_height

            # Verwende die Subsurface-Methode, um einen zugeschnittenen Teil des Bildes zu zeichnen
            surface.blit(image, (x, y), (0, 0, clipped_width, clipped_height))

# Funktion zum Zeichnen des Startbildschirms
def draw_start_screen(surface):
    surface.fill(BLACK)

    # Weißen Bereich zentriert zeichnen
    center_x, center_y, tile_x, tile_y, _, _, _ = calculate_layout(SCREEN_WIDTH, SCREEN_HEIGHT)
    rect = pygame.Rect(center_x, center_y, CENTER_AREA_WIDTH, CENTER_AREA_HEIGHT)
    pygame.draw.rect(surface, WHITE, rect)

    # Hintergrundbild nur im weißen Bereich kacheln
    draw_tiled_background(surface, background_image_1, rect, y_offset=-50)

    # Zeichne das zentrale Tile mit abgerundeten Ecken
    tile_rect = pygame.Rect(tile_x + 50, tile_y, TILE_WIDTH - 100, TILE_HEIGHT + 100)
    draw_rounded_rect(surface, tile_rect, HTWGreen, (50, 50, 50), 20, shadow_offset=10)  # Angepasster Schatten

    title_text = "Turing-Test"
    title_rect = pygame.Rect(tile_rect.left-50, tile_rect.top + 10, TILE_WIDTH, 100)
    draw_text(surface, title_text, title_font, BLACK, title_rect, padding=10)

    # Beschreibungstext
    description_text = (
        "Der Turing-Test bewertet die Fähigkeit einer Maschine, "
        "intelligentes Verhalten zu zeigen, "
        "das von dem eines Menschen nicht unterscheidbar ist. "
        "In diesem Spiel wirst du daher Aussagen sehen und entscheiden müssen, "
        "ob sie von einem Menschen oder einer Maschine stammen."
    )

    # Zeichne den Beschreibungstext mit Zeilenumbruch
    description_rect = pygame.Rect(title_rect.left + 50, title_rect.top+90, tile_rect.width, 200)
    draw_text(surface, description_text, small_font, BLACK, description_rect, padding=25, line_spacing=1.2)

    # Zeichne den Autorentext auf zwei Zeilen innerhalb des zentralen Tiles
    author_line_1 = "Khalil Hasan,"
    author_line_2 = "Fallstudien zur Unternehmensfuehrung, 2024"

    # Positioniere den Autorentext
    author_rect_1 = pygame.Rect(title_rect.left + 20, title_rect.top + 400, TILE_WIDTH - 40, 30)  # Erste Zeile
    author_rect_2 = pygame.Rect(tile_x + 20, title_rect.top + 420, TILE_WIDTH - 40, 30)  # Zweite Zeile

    draw_text(surface, author_line_1, small_font_two, BLACK, author_rect_1, padding=10)
    draw_text(surface, author_line_2, small_font_two, BLACK, author_rect_2, padding=10)

    # Start-Button
    button_width = 200
    button_height = 60
    start_button_rect = pygame.Rect(title_rect.left + 175, title_rect.top + 320, button_width, button_height)
    pygame.draw.rect(surface, WHITE, start_button_rect, border_radius=10)
    start_text = font.render("Start", True, BLACK)
    start_text_rect = start_text.get_rect(center=start_button_rect.center)
    surface.blit(start_text, start_text_rect)

    return start_button_rect

# Funktion zum Zeichnen des Tipps-Bildschirms und Ergebnisanzeige
# Funktion zum Zeichnen des Tipps-Bildschirms und Ergebnisanzeige
def draw_tips_screen(surface):
    surface.fill(BLACK)

    # Weißen Bereich zentriert zeichnen
    center_x, center_y, tile_x, tile_y, button1_x, button2_x, button_y = calculate_layout(SCREEN_WIDTH, SCREEN_HEIGHT)
    rect = pygame.Rect(center_x, center_y, CENTER_AREA_WIDTH, CENTER_AREA_HEIGHT)
    pygame.draw.rect(surface, WHITE, rect)

    # Hintergrundbild nur im weißen Bereich kacheln
    draw_tiled_background(surface, background_image_1, rect, y_offset=-50)

    # Zeichne das zentrale Tile mit abgerundeten Ecken und Schatten
    tile_rect = pygame.Rect(tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT + 100)
    draw_rounded_rect(surface, tile_rect, HTWGreen, (50, 50, 50), 20, shadow_offset=10)  # Angepasster Schatten

    # Berechnung des Durchschnitts der richtigen Antworten
    if len(all_results) > 0:
        average_correct_all = np.mean([result['correct'] for result in all_results])
    else:
        average_correct_all = 0

    # Überschrift für das Ergebnis innerhalb des zentralen Tiles
    result_header_text = f"Ergebnis: {correct_guesses}/5"
    result_header_font_size = 35
    result_header_font = pygame.font.Font(None, result_header_font_size)
    result_header_surface = result_header_font.render(result_header_text, True, BLACK)
    result_header_rect = result_header_surface.get_rect(center=(tile_rect.centerx, tile_rect.top + 30))
    surface.blit(result_header_surface, result_header_rect)



    player_average_correct = np.mean([result['correct'] for result in all_results] + [correct_guesses])

    if player_average_correct > average_correct_all:
        comparison_text = f"und bist besser als der Durchschnitt aller Spieler*innen, die {average_correct_all:.2f} der Aussagen richtig haben."
    elif player_average_correct < average_correct_all:
        comparison_text = f"und bist schlechter als der Durchschnitt aller Spieler*innen, die {average_correct_all:.2f} der Aussagen richtig haben."
    else:
        comparison_text = f"und bist genau so gut wie der Durchschnitt aller Spieler*innen, die {average_correct_all:.2f} der Aussagen richtig haben."

    result_text = (
        f"Du hast {correct_guesses}/5 Aussagen richtig beantwortet "
        f"{comparison_text}"
    )

    result_rect = pygame.Rect(tile_rect.left + 20, tile_rect.top + 70, TILE_WIDTH - 40, 100)
    #draw_text(surface, result_text, small_font, BLACK, result_rect, padding=10)

    # Tipps anzeigen (nur die letzten 5 Aussagen)
    for i, guess in enumerate(guesses[-5:]):
        y_offset = 150 + i * 60  # Y-Position innerhalb des zentralen Tiles
        tip_text = f"Aussage {i + 1}: '{guess['text']}' - Getippt: {guess['guess']} - {'Richtig' if guess['correct'] else 'Falsch'}"

        # Textfarbe basierend auf der Richtigkeit
        text_color = GREEN if guess['correct'] else RED

        # Textbereich begrenzen mit zusätzlichem inneren Abstand
        tip_rect = pygame.Rect(tile_rect.left + 20, result_header_rect.bottom + y_offset -100, TILE_WIDTH - 40, 60)

        # Text mit Zeilenumbruch und Abstand zeichnen
        draw_text(surface, tip_text, small_font, text_color, tip_rect, padding=10)

    # "Zurück zum Start"-Button innerhalb des zentralen Tiles
    button_width = 250  # Breite des Buttons
    button_height = 50  # Höhe des Buttons

    back_to_start_button_rect = pygame.Rect(
        tile_rect.left + (TILE_WIDTH - button_width) // 2,
        tile_rect.bottom - button_height - 8,
        button_width, button_height
    )
    pygame.draw.rect(surface, WHITE, back_to_start_button_rect, border_radius=10)
    back_to_start_text = small_font.render("Zurück zum Start", True, BLACK)
    back_to_start_text_rect = back_to_start_text.get_rect(center=back_to_start_button_rect.center)
    surface.blit(back_to_start_text, back_to_start_text_rect)

    text_d = f"Durschnitt Spieler: {average_correct_all:.2f}"

    # Textbereich begrenzen mit zusätzlichem inneren Abstand
    tip_rect = pygame.Rect(tile_rect.left + 20, result_header_rect.bottom - 20, TILE_WIDTH - 40, 60)

    # Text mit Zeilenumbruch und Abstand zeichnen
    draw_text(surface, text_d, small_font_two, BLACK, tip_rect, padding=10)

    return back_to_start_button_rect




# Hauptschleife
running = True

# Initialisiere den Bildschirm im Vollbildmodus
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Turing-Test Spiel")

# Initialisierung der Animation
tile_x_offset = 0  # Versatz für die Animation des Tiles
tile_alpha = 255  # Alpha-Wert für die Transparenz des Tiles
animation_speed = 5  # Geschwindigkeit der Animation
next_statement_index = current_statement_index
animation_active = False  # Flag für die aktive Animation

# Position des neuen Tiles
center_x, center_y, initial_tile_x, initial_tile_y, button1_x, button2_x, button_y = calculate_layout(SCREEN_WIDTH,
                                                                                                      SCREEN_HEIGHT)
tile_x = initial_tile_x
tile_y = initial_tile_y

# Auswahl von 5 zufälligen Aussagen
statements = random.sample(all_statements, 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if game_state == GAME_START:
                start_button_rect = draw_start_screen(screen)
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    restart_game()  # Setze das Spiel zurück, bevor es beginnt
                    game_state = GAME_PLAYING  # Wechsle zum Spielzustand

            elif game_state == GAME_PLAYING:
                button1_rect = pygame.Rect(button1_x, button_y, BUTTON_SIZE, BUTTON_SIZE)
                button2_rect = pygame.Rect(button2_x, button_y, BUTTON_SIZE, BUTTON_SIZE)

                if button1_rect.collidepoint(mouse_x, mouse_y) or button2_rect.collidepoint(mouse_x, mouse_y):
                    chosen_label = "mensch" if button1_rect.collidepoint(mouse_x, mouse_y) else "maschine"
                    correct_label = statements[current_statement_index]["label"]

                    if chosen_label == correct_label:
                        correct_guesses += 1  # Zähle die korrekte Entscheidung
                        guess_correct = True
                    else:
                        incorrect_guesses += 1  # Zähle die falsche Entscheidung
                        guess_correct = False

                    # Speichern der Tipps
                    guesses.append({
                        "text": statements[current_statement_index]["text"],
                        "guess": chosen_label,
                        "correct": guess_correct
                    })

                    tile_x_offset = -1 if button1_rect.collidepoint(mouse_x, mouse_y) else 1
                    animation_active = True
                    next_statement_index = (current_statement_index + 1) % len(statements)

                    if current_statement_index == len(statements) - 1:
                        # Speichere das aktuelle Ergebnis in den letzten 14 Spielen
                        all_results.append({"correct": correct_guesses, "incorrect": incorrect_guesses})
                        last_14_results.append(correct_guesses)
                        if len(last_14_results) > 14:
                            last_14_results.pop(0)

                        game_state = GAME_TIPS  # Wechsle direkt zum Tipps-Bildschirm nach dem Spiel

            elif game_state == GAME_TIPS:
                back_to_start_button_rect = draw_tips_screen(screen)
                if back_to_start_button_rect.collidepoint(mouse_x, mouse_y):
                    restart_game()  # Setze das Spiel zurück, wenn der Benutzer zum Start zurückkehrt
                    game_state = GAME_START  # Wechsle zurück zur Startseite

    # Bildschirm aktualisieren basierend auf dem Spielzustand
    if game_state == GAME_START:
        draw_start_screen(screen)

    elif game_state == GAME_PLAYING:
        # Bildschirm mit Schwarz füllen
        screen.fill(BLACK)

        rect = pygame.Rect(center_x, center_y, CENTER_AREA_WIDTH, CENTER_AREA_HEIGHT)
        # Zentralen blauen Bereich zeichnen
        pygame.draw.rect(screen, WHITE, rect)

        # Hintergrundbild nur im weißen Bereich kacheln
        draw_tiled_background(screen, background_image_2, rect, y_offset=-50)

        if animation_active:
            tile_x += tile_x_offset * animation_speed
            tile_alpha = max(0, tile_alpha - animation_speed * 2)

            # Prüfen, ob die Animation beendet ist
            if abs(tile_x - center_x) > CENTER_AREA_WIDTH // 2:
                animation_active = False
                tile_x_offset = 0
                current_statement_index = next_statement_index  # Nächste Aussage laden
                tile_x = initial_tile_x  # Zurücksetzen auf die Mitte
                tile_alpha = 255  # Wieder vollständig sichtbar machen

        # Großes Tile mit abgerundeten Ecken und Transparenz zeichnen
        tile_surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)
        tile_surface.set_alpha(tile_alpha)
        draw_rounded_rect(tile_surface, tile_surface.get_rect(), HTWGreen, (0, 0, 0), 20,
                          shadow_offset=0)  # Angepasster Schatten
        screen.blit(tile_surface, (tile_x, tile_y))

        # Text im zentralen Tile mit automatischem Zeilenumbruch und Zentrierung
        if tile_alpha > 0:
            tile_rect = pygame.Rect(tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT)
            draw_text(screen, statements[current_statement_index]["text"], font, BLACK, tile_rect, padding=10)

        # Button 1 zeichnen (Mensch-Icon)
        pygame.draw.circle(screen, HTWGreen, (button1_x + BUTTON_SIZE // 2, button_y + BUTTON_SIZE // 2), BUTTON_SIZE // 2)
        draw_circle_with_shadow(screen, HTWGreen, (0, 0, 0, 50), (button1_x + BUTTON_SIZE // 2, button_y + BUTTON_SIZE // 2), BUTTON_SIZE // 2)
        icon_person_scaled = pygame.transform.scale(icon_person, (int(BUTTON_SIZE * 0.6), int(BUTTON_SIZE * 0.6)))
        screen.blit(icon_person_scaled, (button1_x + (BUTTON_SIZE - icon_person_scaled.get_width()) // 2,
                                         button_y + (BUTTON_SIZE - icon_person_scaled.get_height()) // 2))

        # Button 2 zeichnen (Maschinen-Icon)
        pygame.draw.circle(screen, HTWGreen, (button2_x + BUTTON_SIZE // 2, button_y + BUTTON_SIZE // 2), BUTTON_SIZE // 2)
        draw_circle_with_shadow(screen, HTWGreen, (0, 0, 0, 50), (button2_x + BUTTON_SIZE // 2, button_y + BUTTON_SIZE // 2), BUTTON_SIZE // 2)
        icon_brain_scaled = pygame.transform.scale(icon_brain, (int(BUTTON_SIZE * 0.6), int(BUTTON_SIZE * 0.6)))
        screen.blit(icon_brain_scaled, (button2_x + (BUTTON_SIZE - icon_brain_scaled.get_width()) // 2,
                                        button_y + (BUTTON_SIZE - icon_brain_scaled.get_height()) // 2))

        # Fortschrittsanzeige oben rechts
        progress_font_size = 25
        progress_font = pygame.font.Font(None, progress_font_size)
        progress_text = progress_font.render(f"{current_statement_index + 1}/{len(statements)}", True,
                                             BLACK)
        progress_rect = pygame.draw.circle(screen, HTWGreen, (center_x + CENTER_AREA_WIDTH - 40, center_y + 40), 30)
        screen.blit(progress_text, progress_text.get_rect(center=(center_x + CENTER_AREA_WIDTH - 40, center_y + 40)))

    elif game_state == GAME_TIPS:
        back_to_start_button_rect = draw_tips_screen(screen)

    # Aktualisierung des Bildschirms
    pygame.display.flip()

# Beenden von Pygame
pygame.quit()
sys.exit()

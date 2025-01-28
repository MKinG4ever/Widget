long_beep = {
    "name": "Beep",  # The name of the sound pattern
    "notes": [
        (440, 500),  # A4 note for 500ms
        (0, 250),  # Rest for 250ms
        (440, 500),  # A4 note for 500ms
        (0, 250),  # Rest for 250ms
        (440, 500),  # A4 note for 500ms
        (0, 250),  # Rest for 250ms
        (440, 500),  # A4 note for 500ms
        (0, 250),  # Rest for 250ms
        (440, 500),  # A4 note for 500ms
    ]
}

alert_with_variation = {
    "name": "Alert with Variation",  # Name of the alert pattern
    "notes": [
        (392, 300),  # G4 note for 300ms
        (440, 200),  # A4 note for 200ms
        (392, 300),  # G4 note for 300ms
        (349, 200),  # F4 note for 200ms
        (440, 500),  # A4 note for 500ms
    ]
}

pulse_alert = {
    "name": "Pulse Alert",  # Name of the pulse alert pattern
    "notes": [
        (523, 100),  # C5 note for 100ms
        (0, 50),  # Rest for 50ms
        (523, 100),  # C5 note for 100ms
        (0, 50),  # Rest for 50ms
        (523, 100),  # C5 note for 100ms
        (0, 50),  # Rest for 50ms
    ]
}

rising_tone_alert = {
    "name": "Rising Tone Alert",  # Rising tone alert sound pattern
    "notes": [
        (330, 200),  # E4 note for 200ms
        (349, 200),  # F4 note for 200ms
        (392, 200),  # G4 note for 200ms
        (440, 200),  # A4 note for 200ms
    ]
}

descending_tone_alert = {
    "name": "Descending Tone Alert",  # Descending tone alert sound pattern
    "notes": [
        (440, 200),  # A4 note for 200ms
        (392, 200),  # G4 note for 200ms
        (349, 200),  # F4 note for 200ms
        (330, 200),  # E4 note for 200ms
    ]
}

mozart = {
    "name": "Mozart",  # A segment of a Mozart composition
    "notes": [
        (659, 300),  # E5 note for 300ms
        (622, 300),  # D#5 note for 300ms
        (659, 300),  # E5 note for 300ms
        (622, 300),  # D#5 note for 300ms
        (659, 300),  # E5 note for 300ms
        (494, 300),  # B4 note for 300ms
        (587, 300),  # D5 note for 300ms
        (523, 600),  # C5 note for 600ms
        (440, 300),  # A4 note for 300ms
        (494, 300),  # B4 note for 300ms
        (523, 300),  # C5 note for 300ms
        (587, 300),  # D5 note for 300ms
        (659, 600),  # E5 note for 600ms
        (523, 300),  # C5 note for 300ms
        (587, 300),  # D5 note for 300ms
        (659, 600),  # E5 note for 600ms
    ]
}

twinkle = {
    "name": "Twinkle, Twinkle, Little Star",  # Popular children's song
    "notes": [
        (262, 400),  # C4 note for 400ms (Twinkle)
        (262, 400),  # C4 note for 400ms (Twinkle)
        (392, 400),  # G4 note for 400ms (Little)
        (392, 400),  # G4 note for 400ms (Star)
        (440, 400),  # A4 note for 400ms (How I)
        (440, 400),  # A4 note for 400ms (Wonder)
        (392, 800),  # G4 note for 800ms (What You Are)
        (349, 400),  # F4 note for 400ms (Up)
        (349, 400),  # F4 note for 400ms (Above)
        (330, 400),  # E4 note for 400ms (The)
        (330, 400),  # E4 note for 400ms (World)
        (294, 400),  # D4 note for 400ms (So)
        (294, 400),  # D4 note for 400ms (High)
        (262, 800),  # C4 note for 800ms (Like a Diamond)
        (392, 400),  # G4 note for 400ms (Twinkle)
        (392, 400),  # G4 note for 400ms (Twinkle)
        (349, 400),  # F4 note for 400ms (Little)
        (349, 400),  # F4 note for 400ms (Star)
        (330, 400),  # E4 note for 400ms (How I)
        (330, 400),  # E4 note for 400ms (Wonder)
        (294, 800),  # D4 note for 800ms (What You Are)
    ]
}

happy_birthday = {
    "name": "Happy Birthday",  # The well-known "Happy Birthday" song
    "notes": [
        (264, 300),  # C4 note for 300ms
        (264, 300),  # C4 note for 300ms
        (297, 600),  # D4 note for 600ms
        (264, 600),  # C4 note for 600ms
        (352, 600),  # F4 note for 600ms
        (330, 1200),  # E4 note for 1200ms
        (264, 300),  # C4 note for 300ms
        (264, 300),  # C4 note for 300ms
        (297, 600),  # D4 note for 600ms
        (264, 600),  # C4 note for 600ms
        (396, 600),  # G4 note for 600ms
        (352, 1200),  # F4 note for 1200ms
        (264, 300),  # C4 note for 300ms
        (264, 300),  # C4 note for 300ms
        (528, 600),  # C5 note for 600ms
        (440, 600),  # A4 note for 600ms
        (352, 600),  # F4 note for 600ms
        (330, 600),  # E4 note for 600ms
        (297, 1200),  # D4 note for 1200ms
        (466, 300),  # A#4 note for 300ms
        (466, 300),  # A#4 note for 300ms
        (440, 600),  # A4 note for 600ms
        (352, 600),  # F4 note for 600ms
        (396, 600),  # G4 note for 600ms
        (352, 1200),  # F4 note for 1200ms
    ]
}

mary_lamb = {
    "name": "Mary Had a Little Lamb",  # The children's song "Mary Had a Little Lamb"
    "notes": [
        (330, 400),  # E4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (262, 400),  # C4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 800),  # E4 note for 800ms
        (294, 400),  # D4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (294, 800),  # D4 note for 800ms
        (330, 400),  # E4 note for 400ms
        (392, 400),  # G4 note for 400ms
        (392, 800),  # G4 note for 800ms
        (330, 400),  # E4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (262, 400),  # C4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (262, 1600),  # C4 note for 1600ms
    ]
}

jingle_bells = {
    "name": "Jingle Bells",  # "Jingle Bells" melody
    "notes": [
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 800),  # E4 note for 800ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 800),  # E4 note for 800ms
        (330, 400),  # E4 note for 400ms
        (392, 400),  # G4 note for 400ms
        (262, 400),  # C4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (330, 1200),  # E4 note for 1200ms
        (349, 400),  # F4 note for 400ms
        (349, 400),  # F4 note for 400ms
        (349, 400),  # F4 note for 400ms
        (349, 400),  # F4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (294, 400),  # D4 note for 400ms
        (392, 800),  # G4 note for 800ms
    ]
}

fur_elise = {
    "name": "Fur Elise",  # A piece from Beethoven's "Fur Elise"
    "notes": [
        (330, 300),  # E4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (440, 300),  # A4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (440, 300),  # A4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (261, 300),  # C4 note for 300ms
        (261, 300),  # C4 note for 300ms
        (330, 300),  # E4 note for 300ms
        (261, 300),  # C4 note for 300ms
        (392, 300),  # G4 note for 300ms
    ]
}

chopsticks = {
    "name": "Chopsticks",  # The well-known "Chopsticks" melody
    "notes": [
        (262, 400),  # C4 note for 400ms
        (262, 400),  # C4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (392, 400),  # G4 note for 400ms
        (392, 400),  # G4 note for 400ms
        (440, 400),  # A4 note for 400ms
        (440, 400),  # A4 note for 400ms
        (392, 400),  # G4 note for 400ms
        (392, 400),  # G4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (330, 400),  # E4 note for 400ms
        (262, 400),  # C4 note for 400ms
    ]
}

_info = {
    "name": "melodies.py",
    "version": "v1.0"
}

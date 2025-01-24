# hello.py

import random

# Dictionnaire de réponses spéciales
reponses_speciales = {
    "bonjour": [
        "Bonjour ! Comment allez-vous ?",
        "Salut ! Comment ça va ?",
        "Bonjour, bienvenue !",
        "Enchanté ! Comment allez-vous ?",
        "Bonjour, je suis ravi de vous rencontrer !",
        "Bonjour, comment allez-vous aujourd'hui ?",
        "Bonjour, je suis heureux de vous voir !",
        "Bonjour, comment ça va ?",
        "Bonjour, je suis là pour vous aider !",
        "Bonjour, bienvenue dans notre conversation !"
    ],
    "merci": [
        "De rien !",
        "Pas de problème.",
        "Avec plaisir.",
        "Je vous en prie.",
        "C'est normal, je suis là pour vous aider.",
        "Je suis ravi de vous aider !",
        "C'est mon plaisir !",
        "Je suis heureux de vous aider !",
        "Je suis là pour vous aider, sans problème !",
        "Je suis ravi de vous aider, c'est mon plaisir !"
    ],
    "au revoir": [
        "Au revoir ! À bientôt.",
        "À plus tard.",
        "Bonne journée !",
        "Bonne soirée !",
        "Je vous souhaite une bonne journée.",
        "Je vous souhaite une bonne soirée.",
        "Je suis désolé de vous quitter.",
        "Je suis heureux de vous avoir rencontré.",
        "Je vous souhaite une bonne chance.",
        "Je vous souhaite une bonne santé."
    ],
    "comment ça va": [
        "Ça va bien, merci.",
        "Je vais bien, merci.",
        "Je vais bien, merci pour votre question.",
        "Je suis en forme, merci.",
        "Je vais bien, merci pour votre intérêt.",
        "Je suis heureux de vous répondre.",
        "Je suis en train de bien aller.",
        "Je suis en forme, merci pour votre question.",
        "Je vais bien, merci pour votre intérêt.",
        "Je suis ravi de vous répondre."
    ],
    "qu'est-ce que tu fais": [
        "Je suis un programme informatique, je ne fais rien de particulier.",
        "Je suis en train de discuter avec vous.",
        "Je suis là pour vous aider.",
        "Je suis en train de vous répondre.",
        "Je suis un programme informatique, je suis là pour vous assister.",
        "Je suis en train de vous aider.",
        "Je suis là pour vous répondre.",
        "Je suis en train de vous assister.",
        "Je suis un programme informatique, je suis là pour vous aider.",
        "Je suis en train de vous aider, c'est mon plaisir !"
    ],
    "je m'appelle": [
        "Enchanté ! Je suis ravi de vous rencontrer.",
        "Bonjour, je suis heureux de vous connaître.",
        "Je suis ravi de vous rencontrer, je suis un programme informatique.",
        "Je suis heureux de vous connaître, je suis là pour vous aider.",
        "Je suis un programme informatique, je suis ravi de vous rencontrer.",
        "Je suis heureux de vous connaître, je suis là pour vous assister.",
        "Je suis ravi de vous rencontrer, je suis un programme informatique.",
        "Je suis heureux de vous connaître, je suis là pour vous aider.",
        "Je suis un programme informatique, je suis ravi de vous rencontrer.",
        "Je suis heureux de vous connaître, je suis là pour vous assister."
    ],
    "tu es qui": [
        "Je suis un programme informatique.",
        "Je suis un programme informatique, je suis là pour vous aider.",
        "Je suis un programme informatique, je suis ravi de vous rencontrer.",
        "Je suis un programme informatique, je suis là pour vous assister.",
        "Je suis un programme informatique, je suis heureux de vous connaître.",
        "Je suis un programme informatique, je suis là pour vous aider.",
        "Je suis un programme informatique, je suis ravi de vous rencontrer.",
        "Je suis un programme informatique, je suis là pour vous assister.",
        "Je suis un programme informatique, je suis heureux de vous connaître.",
        "Je suis un programme informatique, je suis là pour vous aider."
    ],
    "tu aimes": [
        "Je suis un programme informatique, je n'ai pas de goûts personnels.",
        "Je suis un programme informatique, je n'aime pasz les noirs."
        ],}
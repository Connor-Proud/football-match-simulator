from random import choice, choices
from json import load, dump
import os
import numpy as np
from time import sleep
import matplotlib.pyplot as plt

outfield_ten = {
    "Aston Villa": {
        "Ezri Konsa": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 50,
            "clearance_percentage": 40,
            "key_pass_percentage": 20,
            "dribble_percentage": 10,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Pau Torres": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 20,
            "tackle_percentage": 45,
            "clearance_percentage": 50,
            "key_pass_percentage": 25,
            "dribble_percentage": 15,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Matty Cash": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 55,
            "clearance_percentage": 30,
            "key_pass_percentage": 40,
            "dribble_percentage": 25,
            "interception_percentage": 45,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Lucas Digne": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 40,
            "clearance_percentage": 35,
            "key_pass_percentage": 45,
            "dribble_percentage": 30,
            "interception_percentage": 40,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Douglas Luiz": {
            "scoring_percentage": 30,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 45,
            "clearance_percentage": 20,
            "key_pass_percentage": 55,
            "dribble_percentage": 35,
            "interception_percentage": 40,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "John McGinn": {
            "scoring_percentage": 35,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 50,
            "clearance_percentage": 15,
            "key_pass_percentage": 50,
            "dribble_percentage": 40,
            "interception_percentage": 35,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Boubacar Kamara": {
            "scoring_percentage": 15,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 60,
            "clearance_percentage": 25,
            "key_pass_percentage": 35,
            "dribble_percentage": 20,
            "interception_percentage": 55,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Ollie Watkins": {
            "scoring_percentage": 70,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 10,
            "clearance_percentage": 5,
            "key_pass_percentage": 35,
            "dribble_percentage": 65,
            "interception_percentage": 8,
            "special_position": "Striker",
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Leon Bailey": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 45,
            "dribble_percentage": 70,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Moussa Diaby": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 15,
            "clearance_percentage": 5,
            "key_pass_percentage": 50,
            "dribble_percentage": 75,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Brighton & Hove Albion": {
        "Lewis Dunk": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 55,
            "clearance_percentage": 60,
            "key_pass_percentage": 20,
            "dribble_percentage": 5,
            "interception_percentage": 65,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Pervis Estupiñán": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 50,
            "clearance_percentage": 35,
            "key_pass_percentage": 45,
            "dribble_percentage": 30,
            "interception_percentage": 50,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Tariq Lamptey": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 45,
            "clearance_percentage": 30,
            "key_pass_percentage": 40,
            "dribble_percentage": 35,
            "interception_percentage": 45,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Adam Webster": {
            "scoring_percentage": 7,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 50,
            "clearance_percentage": 55,
            "key_pass_percentage": 15,
            "dribble_percentage": 5,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Pascal Groß": {
            "scoring_percentage": 40,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 55,
            "tackle_percentage": 30,
            "clearance_percentage": 15,
            "key_pass_percentage": 65,
            "dribble_percentage": 45,
            "interception_percentage": 25,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Billy Gilmour": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 45,
            "clearance_percentage": 20,
            "key_pass_percentage": 50,
            "dribble_percentage": 30,
            "interception_percentage": 40,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Kaoru Mitoma": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 25,
            "clearance_percentage": 10,
            "key_pass_percentage": 55,
            "dribble_percentage": 70,
            "interception_percentage": 15,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "João Pedro": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 12,
            "clearance_percentage": 5,
            "key_pass_percentage": 35,
            "dribble_percentage": 60,
            "interception_percentage": 10,
            "special_position": "Striker",
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Simon Adingra": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 18,
            "clearance_percentage": 5,
            "key_pass_percentage": 45,
            "dribble_percentage": 65,
            "interception_percentage": 12,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Evan Ferguson": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 15,
            "clearance_percentage": 8,
            "key_pass_percentage": 30,
            "dribble_percentage": 55,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Arsenal": {
        "Ben White": {"scoring_percentage": 5,
                    "shots_total": 0,
                    "goals_total_match": 0,
                    "assist_percentage": 30,
                    "tackle_percentage": 4,
                    "clearance_percentage": 30,
                    "key_pass_percentage": 40,
                    "dribble_percentage": 10,
                    "interception_percentage": 30,
                    "position": "Defender",
            "red_card": False,
            "yellow_card": False},
        "William Saliba": {"scoring_percentage": 8,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 10,
                        "tackle_percentage": 50,
                        "clearance_percentage": 40,
                        "key_pass_percentage": 10,
                        "dribble_percentage": 4,
                        "interception_percentage": 50,
                        "position": "Defender",
            "red_card": False,
            "yellow_card": False},
        "Gabriel Magalhães": {"scoring_percentage": 8,
                            "shots_total": 0,
                            "goals_total_match": 0,
                            "assist_percentage": 10,
                            "tackle_percentage": 60,
                            "clearance_percentage": 40,
                            "key_pass_percentage": 10,
                            "dribble_percentage": 4,
                            "interception_percentage": 50,
                            "position": "Defender",
            "red_card": False,
            "yellow_card": False},
        "Ricardo Calafiori": {"scoring_percentage": 5,
                            "shots_total": 0,
                            "goals_total_match": 0,
                            "assist_percentage": 10,
                            "tackle_percentage": 30,
                            "clearance_percentage": 35,
                            "key_pass_percentage": 20,
                            "dribble_percentage": 12,
                            "interception_percentage": 30,
                            "position": "Defender",
            "red_card": False,
            "yellow_card": False},
        "Martin Ødegaard": {"scoring_percentage": 50,
                            "shots_total": 0,
                            "goals_total_match": 0,
                            "assist_percentage": 50,
                            "tackle_percentage": 10,
                            "clearance_percentage": 20,
                            "key_pass_percentage": 60,
                            "dribble_percentage": 40,
                            "interception_percentage": 10,
                            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False},
        "Declan Rice": {"scoring_percentage": 12,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 18,
                        "tackle_percentage": 70,
                        "clearance_percentage": 20,
                        "key_pass_percentage": 10,
                        "dribble_percentage": 10,
                        "interception_percentage": 30,
                        "position": "Midfielder",
            "red_card": False,
            "yellow_card": False},
        "Mikel Merino": {"scoring_percentage": 50,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 30,
                        "tackle_percentage": 20,
                        "clearance_percentage": 20,
                        "key_pass_percentage": 40,
                        "dribble_percentage": 30,
                        "interception_percentage": 20,
                        "position": "Midfielder",
            "red_card": False,
            "yellow_card": False},
        "Bukayo Saka": {"scoring_percentage": 60,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 70,
                        "tackle_percentage": 12,
                        "clearance_percentage": 4,
                        "key_pass_percentage": 80,
                        "dribble_percentage": 70,
                        "interception_percentage": 5,
                        "position": "Forward",
            "red_card": False,
            "yellow_card": False},
        "Kai Havertz": {"scoring_percentage": 40,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 40,
                        "tackle_percentage": 40,
                        "clearance_percentage": 4,
                        "key_pass_percentage": 50,
                        "dribble_percentage": 50,
                        "interception_percentage": 1,
                        "special_position": "Striker",
                        "position": "Forward",
            "red_card": False,
            "yellow_card": False},
        "Gabriel Martinelli": {"scoring_percentage": 40,
                            "shots_total": 0,
                            "goals_total_match": 0,
                            "assist_percentage": 40,
                            "tackle_percentage": 12,
                            "clearance_percentage": 4,
                            "key_pass_percentage": 40,
                            "dribble_percentage": 40,
                            "interception_percentage": 5,
                            "position": "Forward",
            "red_card": False,
            "yellow_card": False}
    },
    "Newcastle United": {
        "Tino Livramento": {"scoring_percentage": 10,
                            "shots_total": 0,
                            "goals_total_match": 0,
                            "assist_percentage": 40,
                            "tackle_percentage": 45,
                            "clearance_percentage": 30,
                            "key_pass_percentage": 50,
                            "dribble_percentage": 20,
                            "interception_percentage": 35,
                            "position": "Defender",
            "red_card": False,
            "yellow_card": False},
        "Sven Botman": {"scoring_percentage": 5,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 5,
                        "tackle_percentage": 55,
                        "clearance_percentage": 45,
                        "key_pass_percentage": 10,
                        "dribble_percentage": 5,
                        "interception_percentage": 45,
                        "position": "Defender",
            "red_card": False,
            "yellow_card": False},
        "Fabian Schar": {"scoring_percentage": 8,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 8,
                        "tackle_percentage": 50,
                        "clearance_percentage": 40,
                        "key_pass_percentage": 15,
                        "dribble_percentage": 10,
                        "interception_percentage": 40,
                        "position": "Defender",
            "red_card": False,
            "yellow_card": False},
        "Lewis Hall": {"scoring_percentage": 10,
                            "shots_total": 0,
                            "goals_total_match": 0,
                            "assist_percentage": 40,
                            "tackle_percentage": 45,
                            "clearance_percentage": 30,
                            "key_pass_percentage": 50,
                            "dribble_percentage": 20,
                            "interception_percentage": 35,
                            "position": "Defender",
            "red_card": False,
            "yellow_card": False},
        "Bruno Guimaraes": {"scoring_percentage": 25,
                            "shots_total": 0,
                            "goals_total_match": 0,
                            "assist_percentage": 35,
                            "tackle_percentage": 40,
                            "clearance_percentage": 15,
                            "key_pass_percentage": 45,
                            "dribble_percentage": 35,
                            "interception_percentage": 30,
                            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False},
        "Sandro Tonali": {"scoring_percentage": 20,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 30,
                        "tackle_percentage": 45,
                        "clearance_percentage": 20,
                        "key_pass_percentage": 40,
                        "dribble_percentage": 30,
                        "interception_percentage": 35,
                        "position": "Midfielder",
            "red_card": False,
            "yellow_card": False},
        "Joelinton": {"scoring_percentage": 30,
                    "shots_total": 0,
                    "goals_total_match": 0,
                    "assist_percentage": 25,
                    "tackle_percentage": 35,
                    "clearance_percentage": 15,
                    "key_pass_percentage": 30,
                    "dribble_percentage": 40,
                    "interception_percentage": 25,
                    "position": "Midfielder",
            "red_card": False,
            "yellow_card": False},
        "Alexander Isak": {"scoring_percentage": 65,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 25,
                        "tackle_percentage": 10,
                        "clearance_percentage": 5,
                        "key_pass_percentage": 30,
                        "dribble_percentage": 55,
                        "interception_percentage": 10,
                        "special_position": "Striker",
                        "position": "Forward",
            "red_card": False,
            "yellow_card": False},
        "Jacob Murphy": {"scoring_percentage": 45,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 35,
                        "tackle_percentage": 15,
                        "clearance_percentage": 5,
                        "key_pass_percentage": 40,
                        "dribble_percentage": 60,
                        "interception_percentage": 15,
                        "position": "Forward",
            "red_card": False,
            "yellow_card": False},
        "Anthony Gordon": {"scoring_percentage": 40,
                        "shots_total": 0,
                        "goals_total_match": 0,
                        "assist_percentage": 35,
                        "tackle_percentage": 20,
                        "clearance_percentage": 5,
                        "key_pass_percentage": 35,
                        "dribble_percentage": 55,
                        "interception_percentage": 15,
                        "position": "Forward",
            "red_card": False,
            "yellow_card": False}
    },

    "Liverpool": {
        "Virgil van Dijk": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 55,
            "clearance_percentage": 45,
            "key_pass_percentage": 15,
            "dribble_percentage": 5,
            "interception_percentage": 50,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Trent Alexander-Arnold": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 40,
            "clearance_percentage": 30,
            "key_pass_percentage": 60,
            "dribble_percentage": 25,
            "interception_percentage": 35,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Andy Robertson": {
            "scoring_percentage": 6,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 50,
            "clearance_percentage": 35,
            "key_pass_percentage": 40,
            "dribble_percentage": 20,
            "interception_percentage": 40,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Ibrahima Konaté": {
            "scoring_percentage": 7,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 8,
            "tackle_percentage": 60,
            "clearance_percentage": 50,
            "key_pass_percentage": 10,
            "dribble_percentage": 5,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Dominik Szoboszlai": {
            "scoring_percentage": 30,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 25,
            "clearance_percentage": 10,
            "key_pass_percentage": 55,
            "dribble_percentage": 45,
            "interception_percentage": 20,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Alexis Mac Allister": {
            "scoring_percentage": 25,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 40,
            "clearance_percentage": 15,
            "key_pass_percentage": 50,
            "dribble_percentage": 35,
            "interception_percentage": 30,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Thiago Alcântara": {
            "scoring_percentage": 15,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 30,
            "clearance_percentage": 10,
            "key_pass_percentage": 60,
            "dribble_percentage": 50,
            "interception_percentage": 25,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Mohamed Salah": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 10,
            "clearance_percentage": 5,
            "key_pass_percentage": 50,
            "dribble_percentage": 70,
            "interception_percentage": 8,
            "special_position": "Striker",
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Darwin Núñez": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 15,
            "clearance_percentage": 8,
            "key_pass_percentage": 35,
            "dribble_percentage": 60,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Luis Díaz": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 40,
            "dribble_percentage": 65,
            "interception_percentage": 12,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Manchester City": {
        "Rúben Dias": {
            "scoring_percentage": 6,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 8,
            "tackle_percentage": 60,
            "clearance_percentage": 50,
            "key_pass_percentage": 10,
            "dribble_percentage": 5,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Kyle Walker": {
            "scoring_percentage": 5,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 50,
            "clearance_percentage": 35,
            "key_pass_percentage": 40,
            "dribble_percentage": 25,
            "interception_percentage": 45,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "John Stones": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 20,
            "tackle_percentage": 55,
            "clearance_percentage": 40,
            "key_pass_percentage": 30,
            "dribble_percentage": 15,
            "interception_percentage": 50,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Nathan Aké": {
            "scoring_percentage": 7,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 45,
            "clearance_percentage": 35,
            "key_pass_percentage": 25,
            "dribble_percentage": 10,
            "interception_percentage": 40,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Kevin De Bruyne": {
            "scoring_percentage": 40,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 60,
            "tackle_percentage": 25,
            "clearance_percentage": 10,
            "key_pass_percentage": 70,
            "dribble_percentage": 50,
            "interception_percentage": 20,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Rodri": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 55,
            "clearance_percentage": 20,
            "key_pass_percentage": 45,
            "dribble_percentage": 30,
            "interception_percentage": 50,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Bernardo Silva": {
            "scoring_percentage": 35,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 30,
            "clearance_percentage": 15,
            "key_pass_percentage": 60,
            "dribble_percentage": 60,
            "interception_percentage": 25,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Erling Haaland": {
            "scoring_percentage": 75,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 20,
            "tackle_percentage": 5,
            "clearance_percentage": 5,
            "key_pass_percentage": 25,
            "dribble_percentage": 50,
            "interception_percentage": 5,
            "special_position": "Striker",
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Phil Foden": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 15,
            "clearance_percentage": 8,
            "key_pass_percentage": 50,
            "dribble_percentage": 65,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Jérémy Doku": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 45,
            "dribble_percentage": 70,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Chelsea": {
        "Thiago Silva": {
            "scoring_percentage": 5,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 50,
            "clearance_percentage": 45,
            "key_pass_percentage": 15,
            "dribble_percentage": 5,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Reece James": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 55,
            "clearance_percentage": 30,
            "key_pass_percentage": 50,
            "dribble_percentage": 25,
            "interception_percentage": 45,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Levi Colwill": {
            "scoring_percentage": 6,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 45,
            "clearance_percentage": 40,
            "key_pass_percentage": 20,
            "dribble_percentage": 10,
            "interception_percentage": 50,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Ben Chilwell": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 40,
            "clearance_percentage": 30,
            "key_pass_percentage": 45,
            "dribble_percentage": 20,
            "interception_percentage": 40,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Enzo Fernández": {
            "scoring_percentage": 25,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 35,
            "clearance_percentage": 15,
            "key_pass_percentage": 60,
            "dribble_percentage": 40,
            "interception_percentage": 30,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Moisés Caicedo": {
            "scoring_percentage": 15,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 60,
            "clearance_percentage": 20,
            "key_pass_percentage": 40,
            "dribble_percentage": 25,
            "interception_percentage": 55,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Conor Gallagher": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 50,
            "clearance_percentage": 15,
            "key_pass_percentage": 45,
            "dribble_percentage": 30,
            "interception_percentage": 40,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Raheem Sterling": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 15,
            "clearance_percentage": 5,
            "key_pass_percentage": 50,
            "dribble_percentage": 65,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Nicolas Jackson": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 10,
            "clearance_percentage": 5,
            "key_pass_percentage": 30,
            "dribble_percentage": 60,
            "interception_percentage": 5,
            "special_position": "Striker",
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Cole Palmer": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 55,
            "dribble_percentage": 70,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Tottenham Hotspur": {
        "Cristian Romero": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 55,
            "clearance_percentage": 50,
            "key_pass_percentage": 15,
            "dribble_percentage": 5,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Destiny Udogie": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 45,
            "clearance_percentage": 30,
            "key_pass_percentage": 40,
            "dribble_percentage": 25,
            "interception_percentage": 40,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Micky van de Ven": {
            "scoring_percentage": 6,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 8,
            "tackle_percentage": 50,
            "clearance_percentage": 45,
            "key_pass_percentage": 10,
            "dribble_percentage": 5,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Pedro Porro": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 35,
            "clearance_percentage": 25,
            "key_pass_percentage": 50,
            "dribble_percentage": 30,
            "interception_percentage": 35,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "James Maddison": {
            "scoring_percentage": 45,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 55,
            "tackle_percentage": 20,
            "clearance_percentage": 10,
            "key_pass_percentage": 65,
            "dribble_percentage": 50,
            "interception_percentage": 15,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Yves Bissouma": {
            "scoring_percentage": 15,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 60,
            "clearance_percentage": 20,
            "key_pass_percentage": 35,
            "dribble_percentage": 30,
            "interception_percentage": 55,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Pape Matar Sarr": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 50,
            "clearance_percentage": 15,
            "key_pass_percentage": 40,
            "dribble_percentage": 35,
            "interception_percentage": 45,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Son Heung-min": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 10,
            "clearance_percentage": 5,
            "key_pass_percentage": 55,
            "dribble_percentage": 70,
            "interception_percentage": 8,
            "special_position": "Striker",
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Richarlison": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 15,
            "clearance_percentage": 8,
            "key_pass_percentage": 35,
            "dribble_percentage": 60,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Dejan Kulusevski": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 25,
            "clearance_percentage": 5,
            "key_pass_percentage": 45,
            "dribble_percentage": 65,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Everton": {
        "James Tarkowski": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 65,
            "clearance_percentage": 70,
            "key_pass_percentage": 15,
            "dribble_percentage": 10,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Vitalii Mykolenko": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 60,
            "clearance_percentage": 45,
            "key_pass_percentage": 30,
            "dribble_percentage": 20,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Seamus Coleman": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 55,
            "clearance_percentage": 40,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 50,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Michael Keane": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 50,
            "clearance_percentage": 65,
            "key_pass_percentage": 20,
            "dribble_percentage": 15,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Idrissa Gueye": {
            "scoring_percentage": 15,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 70,
            "clearance_percentage": 25,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 65,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Amadou Onana": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 65,
            "clearance_percentage": 30,
            "key_pass_percentage": 30,
            "dribble_percentage": 30,
            "interception_percentage": 60,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Alex Iwobi": {
            "scoring_percentage": 35,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 40,
            "clearance_percentage": 15,
            "key_pass_percentage": 50,
            "dribble_percentage": 60,
            "interception_percentage": 30,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Dwight McNeil": {
            "scoring_percentage": 40,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 35,
            "clearance_percentage": 10,
            "key_pass_percentage": 55,
            "dribble_percentage": 65,
            "interception_percentage": 25,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Dominic Calvert-Lewin": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 10,
            "clearance_percentage": 8,
            "key_pass_percentage": 30,
            "dribble_percentage": 60,
            "interception_percentage": 12,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Demarai Gray": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 45,
            "dribble_percentage": 70,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Brentford": {
        "Ivan Toney": {
            "scoring_percentage": 75,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 15,
            "clearance_percentage": 10,
            "key_pass_percentage": 40,
            "dribble_percentage": 60,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Bryan Mbeumo": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 50,
            "dribble_percentage": 70,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Rico Henry": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 60,
            "clearance_percentage": 40,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Ethan Pinnock": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 55,
            "clearance_percentage": 70,
            "key_pass_percentage": 20,
            "dribble_percentage": 15,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Mathias Jensen": {
            "scoring_percentage": 30,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 45,
            "clearance_percentage": 20,
            "key_pass_percentage": 55,
            "dribble_percentage": 35,
            "interception_percentage": 40,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Christian Nørgaard": {
            "scoring_percentage": 18,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 70,
            "clearance_percentage": 35,
            "key_pass_percentage": 30,
            "dribble_percentage": 20,
            "interception_percentage": 65,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Josh Dasilva": {
            "scoring_percentage": 45,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 35,
            "clearance_percentage": 15,
            "key_pass_percentage": 50,
            "dribble_percentage": 60,
            "interception_percentage": 30,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Yoane Wissa": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 15,
            "clearance_percentage": 5,
            "key_pass_percentage": 40,
            "dribble_percentage": 65,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Ben Mee": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 60,
            "clearance_percentage": 65,
            "key_pass_percentage": 15,
            "dribble_percentage": 10,
            "interception_percentage": 58,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Mikkel Damsgaard": {
            "scoring_percentage": 40,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 30,
            "clearance_percentage": 10,
            "key_pass_percentage": 55,
            "dribble_percentage": 70,
            "interception_percentage": 25,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Fulham": {
        "Aleksandar Mitrović": {
            "scoring_percentage": 70,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 10,
            "clearance_percentage": 12,
            "key_pass_percentage": 30,
            "dribble_percentage": 55,
            "interception_percentage": 8,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "João Palhinha": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 75,
            "clearance_percentage": 40,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 65,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Tim Ream": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 55,
            "clearance_percentage": 70,
            "key_pass_percentage": 20,
            "dribble_percentage": 10,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Antonee Robinson": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 60,
            "clearance_percentage": 45,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Andreas Pereira": {
            "scoring_percentage": 45,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 55,
            "tackle_percentage": 30,
            "clearance_percentage": 15,
            "key_pass_percentage": 60,
            "dribble_percentage": 65,
            "interception_percentage": 25,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Harrison Reed": {
            "scoring_percentage": 25,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 65,
            "clearance_percentage": 30,
            "key_pass_percentage": 45,
            "dribble_percentage": 35,
            "interception_percentage": 60,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Bobby Decordova-Reid": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 25,
            "clearance_percentage": 10,
            "key_pass_percentage": 50,
            "dribble_percentage": 70,
            "interception_percentage": 20,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Willian": {
            "scoring_percentage": 40,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 20,
            "clearance_percentage": 8,
            "key_pass_percentage": 55,
            "dribble_percentage": 75,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Tosin Adarabioyo": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 50,
            "clearance_percentage": 65,
            "key_pass_percentage": 20,
            "dribble_percentage": 15,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Harry Wilson": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 60,
            "tackle_percentage": 15,
            "clearance_percentage": 5,
            "key_pass_percentage": 65,
            "dribble_percentage": 75,
            "interception_percentage": 10,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        }
    },
    "West Ham United": {
        "Kurt Zouma": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 65,
            "clearance_percentage": 75,
            "key_pass_percentage": 15,
            "dribble_percentage": 10,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Emerson Palmieri": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 60,
            "clearance_percentage": 40,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Vladimír Coufal": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 55,
            "clearance_percentage": 50,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 58,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Thilo Kehrer": {
            "scoring_percentage": 9,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 20,
            "tackle_percentage": 50,
            "clearance_percentage": 60,
            "key_pass_percentage": 25,
            "dribble_percentage": 20,
            "interception_percentage": 52,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Declan Rice": {
            "scoring_percentage": 25,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 70,
            "clearance_percentage": 35,
            "key_pass_percentage": 50,
            "dribble_percentage": 30,
            "interception_percentage": 65,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Tomáš Souček": {
            "scoring_percentage": 30,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 60,
            "clearance_percentage": 45,
            "key_pass_percentage": 35,
            "dribble_percentage": 20,
            "interception_percentage": 55,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Lucas Paquetá": {
            "scoring_percentage": 45,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 55,
            "tackle_percentage": 35,
            "clearance_percentage": 15,
            "key_pass_percentage": 60,
            "dribble_percentage": 70,
            "interception_percentage": 30,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Jarrod Bowen": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 25,
            "clearance_percentage": 10,
            "key_pass_percentage": 45,
            "dribble_percentage": 70,
            "interception_percentage": 20,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Michail Antonio": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 15,
            "clearance_percentage": 12,
            "key_pass_percentage": 35,
            "dribble_percentage": 65,
            "interception_percentage": 18,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Saïd Benrahma": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 20,
            "clearance_percentage": 8,
            "key_pass_percentage": 55,
            "dribble_percentage": 75,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Crystal Palace": {
        "Joachim Andersen": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 60,
            "clearance_percentage": 70,
            "key_pass_percentage": 20,
            "dribble_percentage": 15,
            "interception_percentage": 65,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Marc Guéhi": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 12,
            "tackle_percentage": 55,
            "clearance_percentage": 65,
            "key_pass_percentage": 18,
            "dribble_percentage": 10,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Tyrick Mitchell": {
            "scoring_percentage": 9,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 65,
            "clearance_percentage": 50,
            "key_pass_percentage": 30,
            "dribble_percentage": 20,
            "interception_percentage": 58,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Nathaniel Clyne": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 50,
            "clearance_percentage": 45,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 52,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Cheick Doucouré": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 70,
            "clearance_percentage": 40,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 68,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Jeffrey Schlupp": {
            "scoring_percentage": 35,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 45,
            "clearance_percentage": 25,
            "key_pass_percentage": 45,
            "dribble_percentage": 60,
            "interception_percentage": 35,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Eberechi Eze": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 20,
            "clearance_percentage": 8,
            "key_pass_percentage": 55,
            "dribble_percentage": 75,
            "interception_percentage": 15,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Michael Olise": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 18,
            "clearance_percentage": 5,
            "key_pass_percentage": 60,
            "dribble_percentage": 80,
            "interception_percentage": 12,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Wilfried Zaha": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 15,
            "clearance_percentage": 5,
            "key_pass_percentage": 40,
            "dribble_percentage": 80,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Jean-Philippe Mateta": {
            "scoring_percentage": 58,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 12,
            "clearance_percentage": 10,
            "key_pass_percentage": 30,
            "dribble_percentage": 60,
            "interception_percentage": 8,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Nottingham Forest": {
        "Joe Worrall": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 60,
            "clearance_percentage": 75,
            "key_pass_percentage": 15,
            "dribble_percentage": 10,
            "interception_percentage": 62,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Willy Boly": {
            "scoring_percentage": 9,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 12,
            "tackle_percentage": 58,
            "clearance_percentage": 70,
            "key_pass_percentage": 18,
            "dribble_percentage": 12,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Renan Lodi": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 55,
            "clearance_percentage": 40,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 50,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Neco Williams": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 50,
            "clearance_percentage": 45,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Morgan Gibbs-White": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 30,
            "clearance_percentage": 15,
            "key_pass_percentage": 60,
            "dribble_percentage": 65,
            "interception_percentage": 25,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Remo Freuler": {
            "scoring_percentage": 25,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 60,
            "clearance_percentage": 35,
            "key_pass_percentage": 45,
            "dribble_percentage": 30,
            "interception_percentage": 58,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Ryan Yates": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 65,
            "clearance_percentage": 40,
            "key_pass_percentage": 35,
            "dribble_percentage": 20,
            "interception_percentage": 62,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Brennan Johnson": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 15,
            "clearance_percentage": 5,
            "key_pass_percentage": 50,
            "dribble_percentage": 75,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Taiwo Awoniyi": {
            "scoring_percentage": 70,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 10,
            "clearance_percentage": 8,
            "key_pass_percentage": 30,
            "dribble_percentage": 60,
            "interception_percentage": 12,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Chris Wood": {
            "scoring_percentage": 70,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 10,
            "clearance_percentage": 8,
            "key_pass_percentage": 30,
            "dribble_percentage": 60,
            "interception_percentage": 12,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
    },
        "Leicester City": {
        "Wout Faes": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 65,
            "clearance_percentage": 70,
            "key_pass_percentage": 15,
            "dribble_percentage": 10,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Ricardo Pereira": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 60,
            "clearance_percentage": 45,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "James Justin": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 55,
            "clearance_percentage": 50,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 58,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Jannik Vestergaard": {
            "scoring_percentage": 9,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 12,
            "tackle_percentage": 50,
            "clearance_percentage": 75,
            "key_pass_percentage": 18,
            "dribble_percentage": 10,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Wilfred Ndidi": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 75,
            "clearance_percentage": 40,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 70,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Kiernan Dewsbury-Hall": {
            "scoring_percentage": 45,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 40,
            "clearance_percentage": 20,
            "key_pass_percentage": 55,
            "dribble_percentage": 60,
            "interception_percentage": 35,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Dennis Praet": {
            "scoring_percentage": 35,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 50,
            "clearance_percentage": 15,
            "key_pass_percentage": 50,
            "dribble_percentage": 55,
            "interception_percentage": 40,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Patson Daka": {
            "scoring_percentage": 70,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 10,
            "clearance_percentage": 8,
            "key_pass_percentage": 30,
            "dribble_percentage": 65,
            "interception_percentage": 12,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Jamie Vardy": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 15,
            "clearance_percentage": 5,
            "key_pass_percentage": 40,
            "dribble_percentage": 70,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Stephy Mavididi": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 45,
            "dribble_percentage": 75,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Manchester United": {
        "Lisandro Martínez": {
            "scoring_percentage": 7,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 15,
            "tackle_percentage": 60,
            "clearance_percentage": 50,
            "key_pass_percentage": 20,
            "dribble_percentage": 10,
            "interception_percentage": 65,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Raphaël Varane": {
            "scoring_percentage": 6,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 55,
            "clearance_percentage": 55,
            "key_pass_percentage": 15,
            "dribble_percentage": 5,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Luke Shaw": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 45,
            "clearance_percentage": 30,
            "key_pass_percentage": 45,
            "dribble_percentage": 25,
            "interception_percentage": 40,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Diogo Dalot": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 40,
            "clearance_percentage": 25,
            "key_pass_percentage": 50,
            "dribble_percentage": 30,
            "interception_percentage": 35,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Bruno Fernandes": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 60,
            "tackle_percentage": 25,
            "clearance_percentage": 10,
            "key_pass_percentage": 70,
            "dribble_percentage": 45,
            "interception_percentage": 20,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Casemiro": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 65,
            "clearance_percentage": 25,
            "key_pass_percentage": 35,
            "dribble_percentage": 20,
            "interception_percentage": 60,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Mason Mount": {
            "scoring_percentage": 35,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 30,
            "clearance_percentage": 15,
            "key_pass_percentage": 55,
            "dribble_percentage": 50,
            "interception_percentage": 25,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Marcus Rashford": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 15,
            "clearance_percentage": 5,
            "key_pass_percentage": 45,
            "dribble_percentage": 70,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Rasmus Højlund": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 10,
            "clearance_percentage": 5,
            "key_pass_percentage": 30,
            "dribble_percentage": 55,
            "interception_percentage": 8,
            "special_position": "Striker",
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Alejandro Garnacho": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 50,
            "dribble_percentage": 75,
            "interception_percentage": 12,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Southampton": {
        "Kyle Walker-Peters": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 60,
            "clearance_percentage": 45,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Armel Bella-Kotchap": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 65,
            "clearance_percentage": 70,
            "key_pass_percentage": 15,
            "dribble_percentage": 10,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Mohammed Salisu": {
            "scoring_percentage": 9,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 12,
            "tackle_percentage": 58,
            "clearance_percentage": 75,
            "key_pass_percentage": 18,
            "dribble_percentage": 12,
            "interception_percentage": 62,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Romain Perraud": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 55,
            "clearance_percentage": 50,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 58,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "James Ward-Prowse": {
            "scoring_percentage": 40,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 55,
            "tackle_percentage": 50,
            "clearance_percentage": 25,
            "key_pass_percentage": 60,
            "dribble_percentage": 35,
            "interception_percentage": 45,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Stuart Armstrong": {
            "scoring_percentage": 45,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 35,
            "clearance_percentage": 15,
            "key_pass_percentage": 55,
            "dribble_percentage": 65,
            "interception_percentage": 30,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Joe Aribo": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 45,
            "clearance_percentage": 20,
            "key_pass_percentage": 50,
            "dribble_percentage": 70,
            "interception_percentage": 25,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Che Adams": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 15,
            "clearance_percentage": 8,
            "key_pass_percentage": 35,
            "dribble_percentage": 60,
            "interception_percentage": 12,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Adam Armstrong": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 40,
            "dribble_percentage": 70,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Sékou Mara": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 10,
            "clearance_percentage": 6,
            "key_pass_percentage": 30,
            "dribble_percentage": 65,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Ipswich Town": {
        "Luke Woolfenden": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 60,
            "clearance_percentage": 70,
            "key_pass_percentage": 15,
            "dribble_percentage": 10,
            "interception_percentage": 58,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Leif Davis": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 55,
            "clearance_percentage": 45,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 50,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Cameron Burgess": {
            "scoring_percentage": 9,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 12,
            "tackle_percentage": 58,
            "clearance_percentage": 65,
            "key_pass_percentage": 18,
            "dribble_percentage": 12,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Harry Clarke": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 50,
            "clearance_percentage": 55,
            "key_pass_percentage": 30,
            "dribble_percentage": 20,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Sam Morsy": {
            "scoring_percentage": 25,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 70,
            "clearance_percentage": 35,
            "key_pass_percentage": 45,
            "dribble_percentage": 30,
            "interception_percentage": 65,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Massimo Luongo": {
            "scoring_percentage": 30,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 60,
            "clearance_percentage": 30,
            "key_pass_percentage": 50,
            "dribble_percentage": 35,
            "interception_percentage": 55,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Conor Chaplin": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 20,
            "clearance_percentage": 8,
            "key_pass_percentage": 50,
            "dribble_percentage": 70,
            "interception_percentage": 15,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Wes Burns": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 25,
            "clearance_percentage": 10,
            "key_pass_percentage": 55,
            "dribble_percentage": 75,
            "interception_percentage": 20,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "George Hirst": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 12,
            "clearance_percentage": 8,
            "key_pass_percentage": 30,
            "dribble_percentage": 60,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Nathan Broadhead": {
            "scoring_percentage": 65,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 12,
            "clearance_percentage": 8,
            "key_pass_percentage": 30,
            "dribble_percentage": 60,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Wolverhampton Wanderers": {
        "Max Kilman": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 65,
            "clearance_percentage": 70,
            "key_pass_percentage": 15,
            "dribble_percentage": 10,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Nelson Semedo": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 60,
            "clearance_percentage": 45,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Rayan Aït-Nouri": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 55,
            "clearance_percentage": 50,
            "key_pass_percentage": 35,
            "dribble_percentage": 25,
            "interception_percentage": 58,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Craig Dawson": {
            "scoring_percentage": 9,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 12,
            "tackle_percentage": 58,
            "clearance_percentage": 75,
            "key_pass_percentage": 18,
            "dribble_percentage": 12,
            "interception_percentage": 62,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "João Gomes": {
            "scoring_percentage": 20,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 70,
            "clearance_percentage": 40,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 65,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Mario Lemina": {
            "scoring_percentage": 25,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 65,
            "clearance_percentage": 35,
            "key_pass_percentage": 45,
            "dribble_percentage": 35,
            "interception_percentage": 60,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Matheus Nunes": {
            "scoring_percentage": 45,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 40,
            "clearance_percentage": 20,
            "key_pass_percentage": 55,
            "dribble_percentage": 65,
            "interception_percentage": 35,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Pablo Sarabia": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 55,
            "tackle_percentage": 25,
            "clearance_percentage": 10,
            "key_pass_percentage": 60,
            "dribble_percentage": 70,
            "interception_percentage": 20,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Matheus Cunha": {
            "scoring_percentage": 70,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 10,
            "clearance_percentage": 8,
            "key_pass_percentage": 35,
            "dribble_percentage": 75,
            "interception_percentage": 12,
            "special_position": "Striker",
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Pedro Neto": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 15,
            "clearance_percentage": 5,
            "key_pass_percentage": 55,
            "dribble_percentage": 80,
            "interception_percentage": 10,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    },
    "Bournemouth": {
        "Lloyd Kelly": {
            "scoring_percentage": 8,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 10,
            "tackle_percentage": 60,
            "clearance_percentage": 70,
            "key_pass_percentage": 15,
            "dribble_percentage": 10,
            "interception_percentage": 58,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Adam Smith": {
            "scoring_percentage": 12,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 35,
            "tackle_percentage": 55,
            "clearance_percentage": 45,
            "key_pass_percentage": 40,
            "dribble_percentage": 30,
            "interception_percentage": 50,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Marcos Senesi": {
            "scoring_percentage": 9,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 12,
            "tackle_percentage": 58,
            "clearance_percentage": 65,
            "key_pass_percentage": 18,
            "dribble_percentage": 12,
            "interception_percentage": 60,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Jack Stephens": {
            "scoring_percentage": 10,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 25,
            "tackle_percentage": 50,
            "clearance_percentage": 55,
            "key_pass_percentage": 30,
            "dribble_percentage": 20,
            "interception_percentage": 55,
            "position": "Defender",
            "red_card": False,
            "yellow_card": False
        },
        "Lewis Cook": {
            "scoring_percentage": 25,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 70,
            "clearance_percentage": 35,
            "key_pass_percentage": 45,
            "dribble_percentage": 30,
            "interception_percentage": 65,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Philip Billing": {
            "scoring_percentage": 55,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 40,
            "tackle_percentage": 50,
            "clearance_percentage": 25,
            "key_pass_percentage": 45,
            "dribble_percentage": 45,
            "interception_percentage": 40,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Ryan Christie": {
            "scoring_percentage": 45,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 50,
            "tackle_percentage": 35,
            "clearance_percentage": 15,
            "key_pass_percentage": 55,
            "dribble_percentage": 65,
            "interception_percentage": 30,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "David Brooks": {
            "scoring_percentage": 50,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 55,
            "tackle_percentage": 20,
            "clearance_percentage": 8,
            "key_pass_percentage": 60,
            "dribble_percentage": 75,
            "interception_percentage": 15,
            "position": "Midfielder",
            "red_card": False,
            "yellow_card": False
        },
        "Dominic Solanke": {
            "scoring_percentage": 70,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 30,
            "tackle_percentage": 15,
            "clearance_percentage": 10,
            "key_pass_percentage": 35,
            "dribble_percentage": 65,
            "interception_percentage": 12,
            "special_position": "Striker",
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        },
        "Justin Kluivert": {
            "scoring_percentage": 60,
            "shots_total": 0,
            "goals_total_match": 0,
            "assist_percentage": 45,
            "tackle_percentage": 20,
            "clearance_percentage": 5,
            "key_pass_percentage": 50,
            "dribble_percentage": 70,
            "interception_percentage": 15,
            "position": "Forward",
            "red_card": False,
            "yellow_card": False
        }
    }
}


goalkeepers = {
    "Arsenal": {"David Raya": {"save_percentage": 75, "saves": 89, "clean_sheets": 11}},
    "Liverpool": {"Alisson Becker": {"save_percentage": 78, "saves": 92, "clean_sheets": 12}},
    "Manchester City": {"Ederson": {"save_percentage": 76, "saves": 85, "clean_sheets": 13}},
    "Newcastle United": {"Nick Pope": {"save_percentage": 74, "saves": 88, "clean_sheets": 10}},
    "Manchester United": {"Andre Onana": {"save_percentage": 71, "saves": 82, "clean_sheets": 8}},
    "Chelsea": {"Robert Sanchez": {"save_percentage": 70, "saves": 78, "clean_sheets": 7}},
    "Brighton & Hove Albion": {"Bart Verbruggen": {"save_percentage": 72, "saves": 76, "clean_sheets": 8}},
    "Aston Villa": {"Emiliano Martinez": {"save_percentage": 75, "saves": 86, "clean_sheets": 9}},
    "Tottenham Hotspur": {"Guglielmo Vicario": {"save_percentage": 73, "saves": 84, "clean_sheets": 9}},
    "Brentford": {"Mark Flekken": {"save_percentage": 70, "saves": 75, "clean_sheets": 6}},
    "Crystal Palace": {"Sam Johnstone": {"save_percentage": 71, "saves": 79, "clean_sheets": 7}},
    "Everton": {"Jordan Pickford": {"save_percentage": 72, "saves": 83, "clean_sheets": 8}},
    "Fulham": {"Bernd Leno": {"save_percentage": 71, "saves": 81, "clean_sheets": 7}},
    "Bournemouth": {"Neto": {"save_percentage": 70, "saves": 77, "clean_sheets": 6}},
    "Nottingham Forest": {"Matt Turner": {"save_percentage": 69, "saves": 74, "clean_sheets": 5}},
    "West Ham United": {"Alphonse Areola": {"save_percentage": 71, "saves": 80, "clean_sheets": 7}},
    "Ipswich Town": {"Vaclav Hladky": {"save_percentage": 71, "saves": 75, "clean_sheets": 8}},
    "Southampton": {"Gavin Bazunu": {"save_percentage": 70, "saves": 73, "clean_sheets": 7}},
    "Leicester City": {"Mads Hermansen": {"save_percentage": 72, "saves": 76, "clean_sheets": 9}},
    "Wolverhampton Wanderers": {"Jose Sa": {"save_percentage": 72, "saves": 82, "clean_sheets": 7}}
}

stadiums = {
    "Arsenal": "The Emirates Stadium",
    "Liverpool": "Anfield",
    "Manchester City": "Etihad Stadium",
    "Manchester United": "Old Trafford",
    "Chelsea": "Stamford Bridge",
    "Tottenham Hotspur": "Tottenham Hotspur Stadium",
    "Brighton & Hove Albion": "Falmer Stadium",
    "Aston Villa": "Villa Park",
    "Newcastle United": "St James' Park",
    "Everton": "Goodison Park",
    "Brentford": "Gtech Community Stadium",
    "Fulham": "Craven Cottage",
    "Crystal Palace": "Selhurst Park",
    "Nottingham Forest": "City Ground",
    "West Ham United": "London Stadium",
    "Leicester City": "King Power Stadium",
    "Southampton": "St Mary's Stadium",
    "Ipswich Town": "Portman Road",
    "Wolverhampton Wanderers": "Molineux Stadium",
    "Bournemouth": "Vitality Stadium"
}

teams = ["Arsenal",
        "Newcastle United",
        "Manchester City",
        "Liverpool",
        "Tottenham Hotspur",
        "Manchester United",
        "Chelsea",
        "Brighton & Hove Albion",
        "Aston Villa",
        "Everton",
        "Brentford",
        "Fulham",
        "Crystal Palace",
        "Nottingham Forest",
        "West Ham United",
        "Leicester City",
        "Southampton",
        "Ipswich Town",
        "Wolverhampton Wanderers",
        "Bournemouth"]

global team_counter
global team_chosen
team_counter=1
team_chosen=False




counter=0
error_log_list=[]
def error_log(x="false"):
    if len(error_log_list) > 0:
        if x == "false":
            print("errors ::")
            print(error_log_list)
    else:
        error_log_list.append(x)




def interception_picker(x):
    list_special = []
    list_standard = []
    list_full = [(player_name, stats) for player_name, stats in outfield_ten[x].items()]
    for player_name, stats in outfield_ten[x].items():
        if isinstance(stats, dict) and stats.get("special_position") in ["Defender", "Defensive Midfielder"]:
            list_special.extend([player_name] * 3)
    for player_name, stats in outfield_ten[x].items():
        if isinstance(stats, dict):
            if stats.get("position") == "Defender":
                list_standard.extend([player_name] * 2)
            elif stats.get("position") == "Midfielder":
                list_standard.append(player_name)
    list_complete = [*list_special, *list_standard]
    return choice(list_complete) if list_complete else None


def goal_scoring_picker(x):
    list_special = []
    list_standard = []
    list_full_chosen = []
    list_full = [(player_name, stats) for player_name, stats in outfield_ten[x].items()]
    if list_full:
        list_full_chosen.append(choice(list_full))
    for player_name, stats in outfield_ten[x].items():
        if isinstance(stats, dict) and stats.get("special_position") == "Striker":
            list_special.extend([player_name] * 2)
    for player_name, stats in outfield_ten[x].items():
        if isinstance(stats, dict) and stats.get("position") == "Forward":
            list_standard.extend([player_name] * 2)
            if len(list_standard) >= 8:
                break
    list_complete = [*list_special, *list_standard, *[name for name, _ in list_full_chosen]]
    scorer=choice(list_complete)
    return scorer if list_complete else None





def goal_event(x="false",y="false"):
    global goal_team_a, goal_team_b
    percentage = choice(range(1, 101))
    if x=="false":
        team_scorer = choice(team_list)
        scorer = goal_scoring_picker(team_scorer)
    elif x != "false":
        team_scorer = x
        scorer = goal_scoring_picker(team_scorer)
        print(f"OH! {scorer} has a chance to score for {team_scorer}!")
    if team_scorer == team_a:
        team_opponent = team_b
        if goal_team_a > goal_team_b:
            check_correct_output_1 = "keep"
        else:
            check_correct_output_1 = "put"
    elif team_scorer == team_b:
        team_opponent = team_a
        if goal_team_b > goal_team_a:
            check_correct_output_1 = "keep"
        else:
            check_correct_output_1 = "put"
    try:
        player_percentage = outfield_ten[team_scorer][scorer]["scoring_percentage"]
        if percentage <= player_percentage:
            if team_scorer == team_a:
                goal_team_a += 1

                scoring_team=goal_team_a
                not_scoring_team=goal_team_b
            elif team_scorer == team_b:
                goal_team_b += 1
                scoring_team=goal_team_b
                not_scoring_team=goal_team_a
            if scoring_team > not_scoring_team:
                check=1
                if scoring_team == 1 and not_scoring_team == 0:
                    check=5
            elif scoring_team < not_scoring_team:
                check=2
            elif scoring_team == not_scoring_team:
                check=3
            else:
                check=4
            goal_check_dict={1 : (f"to {check_correct_output_1} {team_scorer} ahead"),
                            2 : (f"to get one back"),
                            3 : (f"to level it"),
                            4 : "wow",
                            5 : "to open the game"
                            }
            goal_check_output=goal_check_dict[check]
            print(f"GOAL!")
            outfield_ten[team_scorer][scorer]["goals_total_match"] = outfield_ten[team_scorer][scorer]["goals_total_match"] + 1
            save_choice=["top left","top right","bottom left","bottom right","centre"]
            save_choice=choice(save_choice)
            accuracy_or_power=["accuracy","power"]
            accuracy_or_power=choice(accuracy_or_power)
            match save_choice:
                case "top left":
                    match accuracy_or_power:
                        case "accuracy":
                            print(f"it was a well placed shot by {scorer} into the top left corner of the net {goal_check_output}")
                        case "power":
                            print(f"AND A ROCKET INTO THE TOP LEFT, {team_scorer.upper()} HAVE SCORED AND {str(scorer).upper()} HAS GOTTEN A GOAL {goal_check_output.upper()}")
                case "top right":
                    match accuracy_or_power:
                        case "accuracy":
                            print(f"it was a well placed shot by {scorer} into the top right corner of the net {goal_check_output}")
                        case "power":
                            print(f"AND A ROCKET INTO THE TOP RIGHT, {team_scorer.upper()} HAVE SCORED AND {str(scorer).upper()} HAS GOTTEN A GOAL {goal_check_output.upper()}")
                case "bottom left":
                    match accuracy_or_power:
                        case "accuracy":
                            print(f"it was a well placed shot by {scorer} into the bottom left corner of the net {goal_check_output}")
                        case "power":
                            print(f"AND A ROCKET INTO THE BOTTOM LEFT, {team_scorer.upper()} HAVE SCORED AND {str(scorer).upper()} HAS GOTTEN A GOAL {goal_check_output.upper()}")
                case "bottom right":
                    match accuracy_or_power:
                        case "accuracy":
                            print(f"it was a well placed shot by {scorer} into the bottom right corner of the net {goal_check_output}")
                        case "power":
                            print(f"AND A ROCKET INTO THE BOTTOM RIGHT, {team_scorer.upper()} HAVE SCORED AND {str(scorer).upper()} HAS GOTTEN A GOAL {goal_check_output.upper()}")
                case "centre":
                    match accuracy_or_power:
                        case "accuracy":
                            print(f"it was a well placed shot by {scorer} down the middle of the goal and through the keepers legs {goal_check_output}")
                        case "power":
                            print(f"AND A ROCKET DOWN THE MIDDLE, THERE WAS NO STOPPING THAT! {team_scorer.upper()} HAVE SCORED AND {str(scorer).upper()} HAS GOTTEN A GOAL {goal_check_output.upper()}")
        else:
            save_or_miss=["save","miss"]
            save_or_miss=choice(save_or_miss)
            if save_or_miss == "miss":
                miss_choice=["wide","over","chip"]
                accuracy_or_power=["accuracy","power"]
                miss_choice=choice(miss_choice)
                accuracy_or_power=choice(accuracy_or_power)
                match miss_choice:
                    case "wide":
                        match accuracy_or_power:
                            case "accuracy":
                                print(f"{scorer} sacrificed power went for placement but has just placed the ball wide off the target for {team_scorer}!")
                            case "power":
                                print(f"{scorer} sacrificed placement and went for power but has just blasted the ball wide off the target for {team_scorer}!")
                    case "over":
                        match accuracy_or_power:
                            case "accuracy":
                                print(f"{scorer} sacrificed power went for placement but has just placed the ball over the crossbar for {team_scorer}!")
                            case "power":
                                print(f"{scorer} sacrificed placement and went for power but has just blasted the ball over the crossbar for {team_scorer}!")
                    case "chip":
                        match accuracy_or_power:
                            case "accuracy":
                                print(f"{scorer} went for the chip, not a lot of power and {list(goalkeepers[team_opponent].keys())[0]} for {team_opponent} catches it with ease!")
                            case "power":
                                print(f"{scorer} (for {team_scorer}) went for the chip, a lot of power and sent it over the bar")
            elif save_or_miss == "save":
                goalkeeper = list(goalkeepers[team_opponent].keys())[0]
                save_choice=["top left","top right","bottom left","bottom right","centre"]
                save_choice=choice(save_choice)
                accuracy_or_power=["accuracy","power"]
                accuracy_or_power=choice(accuracy_or_power)
                match save_choice:
                    case "top left":
                        match accuracy_or_power:
                            case "accuracy":
                                print(f"{goalkeeper} for {team_opponent} flies to the top left and saves {scorer}'s well placed shot, close one, just not enough power!")
                            case "power":
                                print(f"{goalkeeper} for {team_opponent} flies to the top left and just saves {scorer}'s powerful shot! we all thought that was going in!")
                    case "top right":
                        match accuracy_or_power:
                            case "accuracy":
                                print(f"{goalkeeper} for {team_opponent} flies to the top right and saves {scorer}'s well placed shot, close one, just not enough power!")
                            case "power":
                                print(f"{goalkeeper} for {team_opponent} flies to the top right and just saves {scorer}'s powerful shot! we all thought that was going in!")
                    case "bottom left":
                        match accuracy_or_power:
                            case "accuracy":
                                print(f"{goalkeeper} for {team_opponent} dives to the bottom left and saves {scorer}'s well placed shot, close one, just not enough power!")
                            case "power":
                                print(f"{goalkeeper} for {team_opponent} dives to the bottom left and just saves {scorer}'s powerful shot! we all thought that was going in!")
                    case "bottom right":
                        match accuracy_or_power:
                            case "accuracy":
                                print(f"{goalkeeper} for {team_opponent} dives to the bottom right and saves {scorer}'s well placed shot, close one, just not enough power!")
                            case "power":
                                print(f"{goalkeeper} for {team_opponent} dives to the bottom right and just saves {scorer}'s powerful shot! we all thought that was going in!")
                    case "centre":
                        match accuracy_or_power:
                            case "accuracy":
                                print(f"{goalkeeper} for {team_opponent} with ease saves {scorer}'s poorly placed shot, which lacked any power, straight at the keeper!")
                            case "power":
                                print(f"{goalkeeper} for {team_opponent}  just saves {scorer}'s powerful shot down the middle with a leg block! {goalkeeper} almost got caught out there!")

    except KeyError as e:
        print(f"Error: Could not find scoring data for {scorer} - {e}")
######
######
def interception_event(x="false"):
    if x=="false":
        attacking_team = choice(team_list)
    else:
        attacking_team = x
    defending_team = team_b if attacking_team == team_a else team_a
    interceptor = interception_picker(defending_team)
    percentage = choice(range(1, 101))
    try:
        player_percentage = outfield_ten[defending_team][interceptor]["interception_percentage"]
        if percentage <= player_percentage:
            print(f"Interception! {interceptor} wins the ball for {defending_team}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                key_pass_event(defending_team)
        else:
            print(f"Failed interception attempt by {interceptor} of {defending_team}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                goal_event(attacking_team)
    except KeyError as e:
        print(f"Error: Could not find interception data for {interceptor} - {e}")
        return attacking_team

def dribble_event(x="false"):
    if x=="false":
        attacking_team = choice(team_list)
    else:
        attacking_team = x
    defending_team = team_b if attacking_team == team_a else team_a
    dribbler = choice([player for player, stats in outfield_ten[attacking_team].items() if stats.get("dribble_percentage")])
    percentage = choice(range(1, 101))
    try:
        player_percentage = outfield_ten[attacking_team][dribbler]["dribble_percentage"]
        if percentage <= player_percentage:
            print(f"Great dribble by {dribbler} of {attacking_team}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                goal_event(attacking_team)
        else:
            print(f"Failed dribble attempt by {dribbler} of {attacking_team}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                tackle_event(defending_team)
    except KeyError as e:
        print(f"Error: Could not find dribble data for {dribbler} - {e}")
        return attacking_team

def tackle_event(x="false"):
    if x=="false":
        attacking_team = choice(team_list)
    else:
        attacking_team = x

    defending_team = team_b if attacking_team == team_a else team_a
    tackler = choice([player for player, stats in outfield_ten[defending_team].items() if stats.get("tackle_percentage")])
    tackled=choice([player for player, stats in outfield_ten[attacking_team].items()])
    percentage = choice(range(1, 101))
    try:
        player_percentage = outfield_ten[defending_team][tackler]["tackle_percentage"]
        if percentage <= player_percentage:
            print(f"Great tackle by {tackler} of {defending_team} on {tackled}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                key_pass_event(defending_team)
        else:
            print(f"Failed tackle attempt by {tackler} of {defending_team} on {tackled}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                goal_event(attacking_team)
                chosen_event="True"
            if percentage <= 10 and chosen_event == "True":
                injury_event(a="tackle",w=tackler, x=defending_team, y=tackled , z=attacking_team)
    except KeyError as e:
        print(f"Error: Could not find tackle data for {tackler} - {e}")
        return attacking_team

def key_pass_event(x="false"):
    if x=="false":
        attacking_team = choice(team_list)
    else:
        attacking_team = x
    defending_team = team_b if attacking_team == team_a else team_a
    passer = choice([player for player, stats in outfield_ten[attacking_team].items() if stats.get("key_pass_percentage")])
    percentage = choice(range(1, 101))
    try:
        player_percentage = outfield_ten[attacking_team][passer]["key_pass_percentage"]
        if percentage <= player_percentage:
            print(f"Great key pass by {passer} of {attacking_team}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                goal_event(attacking_team)
        else:
            print(f"Failed key pass attempt by {passer} of {attacking_team}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                interception_event(defending_team)
    except KeyError as e:
        print(f"Error: Could not find key pass data for {passer} - {e}")
        return attacking_team

def clearance_event(x="false"):
    if x=="false":
        attacking_team = choice(team_list)
    else:
        attacking_team = x
    defending_team = team_b if attacking_team == team_a else team_a
    red_card_check = choice([player for player, stats in outfield_ten[defending_team].items() if stats.get("clearance_percentage") and stats.get("red_card") == False])
    clearance=red_card_check
    percentage = choice(range(1, 101))
    try:
        player_percentage = outfield_ten[defending_team][clearance]["clearance_percentage"]
        if percentage <= player_percentage:
            print(f"Great clearance by {clearance} of {defending_team}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                goal_event(attacking_team)
        else:
            print(f"Failed clearance attempt by {clearance} of {defending_team}")
            percentage=choice(range(1,101))
            if percentage <= 30:
                goal_event(attacking_team)
    except KeyError as e:
        print(f"Error: Could not find clearance data for {clearance} - {e}")
        return attacking_team












def injury_event(a="false",w="false",x="false",y="false",z="false"):
    """a = whatever the event was from for example tackles etc |
w = usually the person who committed the tackle, x = usually the team of the person who tackled,
y = usually the person who was tackled, and z is the team of who was tackled"""
    if a == "false":
        print(f"oh, something may be seriously wrong here for {w} of {x}\n hes went down and physios are coming on")
    elif a == "tackle":
        output_injury_context=f"a tackle on {y} of {z}\nit looks like in the stretch he's"
    who_was_injured_list=[1,2]
    who_was_injured=choice(who_was_injured_list)
    if who_was_injured == 1:
        percentage=choice(range(1,101))
        if percentage > 11:
            outfield_ten[x][w]["red_card"]=True
            injury_type = ["acl", "torn muscle", "broken bone", "pulled muscle"]
            injury_type_chosen=choice(injury_type)
            injury_place=["left leg", "right leg", "left thigh", "right thigh", "left calf", "right calf"]
            injury_place_chosen=choice(injury_place)
            match injury_type_chosen:
                case "acl":
                    match injury_place_chosen:
                        case "left leg":
                            injury_output=f"oooh thats a bad one\n when attempting {output_injury_context} he's torn his left acruciate ligament"
                        case "right leg":
                            injury_output=f"oooh thats a bad one\n when attempting {output_injury_context} he's torn his left acruciate ligament"
                        case _:
                            injury_place_2=["left leg", "right leg"]
                            injury_place_chosen_2=choice(injury_place_2)
                            match injury_place_chosen_2:
                                case "left leg":
                                    injury_output=f"oooh thats a bad one\n when attempting {output_injury_context} he's torn his left acruciate ligament"
                                case "right leg":
                                    injury_output=f"oooh thats a bad one\n when attempting {output_injury_context} he's torn his left acruciate ligament"
                                case _:
                                    injury_output=""
                                    error_log(f"error in injury event\nacl :: player[1] | {w}")
                                    injury_event()
                case "torn muscle":
                    match injury_place_chosen:
                        case "left leg":
                            injury_output=f"oooh no\noh no...\nit looks like while trying to commit to {output_injury_context} {y} he has pulled his left leg muscle"
                        case "right leg":
                            injury_output=f"oooh no\noh no...\nit looks like while trying to {output_injury_context} {y} he has pulled his right leg muscle"
                        case "left thigh":
                            injury_output=f"oooh no\noh no...\nit looks like while trying to {output_injury_context} {y} he has pulled his left thigh muscle"
                        case "right thigh":
                            injury_output=f"oooh no\noh no...\nit looks like while trying to {output_injury_context} {y} he has pulled his right thigh muscle"
                        case "left calf":
                            injury_output=f"oooh no\noh no...\nit looks like while trying to {output_injury_context} {y} he has pulled his left calf muscle"
                        case "right calf":
                            injury_output=f"oooh no\noh no...\nit looks like while trying to {output_injury_context} {y} he has pulled his right calf muscle"
                        case _:
                            injury_output=""
                            error_log(f"error in injury event\ntorn muscle :: player[1] | {w}")
                            injury_event()
                case "pulled muscle":
                    match injury_place_chosen:
                        case "left leg":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has torn his left leg muscle"
                        case "right leg":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has torn his right leg muscle"
                        case "left thigh":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has torn his left thigh muscle"
                        case "right thigh":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has torn his right thigh muscle"
                        case "left calf":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has torn his left calf muscle"
                        case "right calf":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has torn his right calf muscle"
                        case _:
                            injury_output=""
                            error_log(f"error in injury event\npulled muscle :: player[1] | {w}")
                            injury_event()
                case "broken bone":
                    match injury_place_chosen:
                        case "left leg":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has broke his left leg"
                        case "right leg":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has broke his right leg"
                        case "left thigh":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has broke his left thigh bone"
                        case "right thigh":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has broke his right thigh bone"
                        case "left calf":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has broke his left calf bone"
                        case "right calf":
                            injury_output=f"oooh no\noh no...\n it looks like while trying to {output_injury_context} {y} he has broke his right calf bone"
                        case _:
                            injury_output=""
                            error_log(f"error in injury event\nbroken bone :: player[1] | {w}")
                            injury_event()
        else:
            print("")
    elif who_was_injured == 2:
        if who_was_injured == 2:
            percentage=choice(range(1,101))
            output_injury_context="tackle"
            if percentage > 11:
                outfield_ten[z][y]["red_card"]=True
                injury_type = ["acl", "torn muscle", "broken bone", "pulled muscle"]
                injury_type_chosen=choice(injury_type)
                injury_place=["left leg", "right leg", "left thigh", "right thigh", "left calf", "right calf"]
                injury_place_chosen=choice(injury_place)
                match injury_type_chosen:
                    case "acl":
                        match injury_place_chosen:
                            case "left leg":
                                injury_output=f"oooh thats a bad one\n on the receiving end of a {output_injury_context} he's torn his left acruciate ligament"
                            case "right leg":
                                injury_output=f"oooh thats a bad one\n on the receiving end of a {output_injury_context} he's torn his left acruciate ligament"
                            case _:
                                injury_place_2=["left leg", "right leg"]
                                injury_place_chosen_2=choice(injury_place_2)
                                match injury_place_chosen_2:
                                    case "left leg":
                                        injury_output=f"oooh thats a bad one\n on the receiving end of a {output_injury_context} he's torn his left acruciate ligament"
                                    case "right leg":
                                        injury_output=f"oooh thats a bad one\n on the receiving end of a {output_injury_context} he's torn his left acruciate ligament"
                                    case _:
                                        injury_output=""
                                        error_log(f"error in injury event\nacl :: player[2] | {y}")
                                        injury_event()
                    case "torn muscle":
                        match injury_place_chosen:
                            case "left leg":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has torn his left leg muscle"
                            case "right leg":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has torn his right leg muscle"
                            case "left thigh":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has torn his left thigh muscle"
                            case "right thigh":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has torn his right thigh muscle"
                            case "left calf":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has torn his left calf muscle"
                            case "right calf":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has torn his right calf muscle"
                            case _:
                                injury_output=""
                                error_log(f"error in injury event\ntorn muscle :: player[2] | {y}")
                                injury_event()
                    case "pulled muscle":
                        match injury_place_chosen:
                            case "left leg":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has pulled his left leg muscle"
                            case "right leg":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has pulled his right leg muscle"
                            case "left thigh":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has pulled his left thigh muscle"
                            case "right thigh":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has pulled his right thigh muscle"
                            case "left calf":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has pulled his left calf muscle"
                            case "right calf":
                                injury_output=f"oooh no\noh no...\non the receiving end of a {output_injury_context} from {y} he has pulled his right calf muscle"
                            case _:
                                injury_output=""
                                error_log(f"error in injury event\npulled muscle :: player[2] | {y}")
                                injury_event()
                    case "broken bone":
                        match injury_place_chosen:
                            case "left leg":
                                injury_output=f"oooh no\noh no...\n it looks like while on the receiving end of a {output_injury_context} from {y} he has broke his left leg"
                            case "right leg":
                                injury_output=f"oooh no\noh no...\n it looks like while on the receiving end of a {output_injury_context} from {y} he has broke his right leg"
                            case "left thigh":
                                injury_output=f"oooh no\noh no...\n it looks like while on the receiving end of a {output_injury_context} from {y} he has broke his left thigh bone"
                            case "right thigh":
                                injury_output=f"oooh no\noh no...\n it looks like while on the receiving end of a {output_injury_context} from {y} he has broke his right thigh bone"
                            case "left calf":
                                injury_output=f"oooh no\noh no...\n it looks like while on the receiving end of a {output_injury_context} from {y} he has broke his left calf bone"
                            case "right calf":
                                injury_output=f"oooh no\noh no...\n it looks like while on the receiving end of a {output_injury_context} from {y} he has broke his right calf bone"
                            case _:
                                injury_output=""
                                error_log(f"error in injury event\nbroken bone :: player[2] | {y}")
                                injury_event()
    print(injury_output)













def game_events():
    chances=["goal",
            "interception",
            "dribble",
            "tackle",
            "key pass",
            "interception",
            "dribble",
            "tackle",
            "key pass",
            "interception",
            "dribble",
            "tackle",
            "key pass",
            "interception",
            "dribble",
            "tackle",
            "key pass",
            "clearance",
            "injury",
            "foul",
            "interception",
            "dribble",
            "tackle",
            "key pass",
            "interception",
            "dribble",
            "tackle",
            "key pass",
            "interception",
            "dribble",
            "tackle",
            "key pass",
            "interception",
            "dribble",
            "tackle",
            "key pass",
            "injury",
            "foul"
            ]
    chosen=choice(chances)
    if chosen == "goal":
        goal_event()
    elif chosen == "interception":
        interception_event()
    elif chosen == "dribble":
        dribble_event()
    elif chosen == "tackle":
        tackle_event()
    elif chosen == "key pass":
        key_pass_event()
    elif chosen == "clearance":
        clearance_event()
    else:
        checkout=0
        checkout+=1
        if checkout > 3:
            print("error in block 3292\ndef game_events():\n \nplease try again")
        game_events()


def main(x, y):
    global suffix
    global goal_team_a, goal_team_b
    goal_team_a=int(0)
    goal_team_b=int(0)
    derby=False
    premier_league_derbies = [
        ("Arsenal", "Tottenham"),
        ("Manchester United", "Manchester City"),
        ("Liverpool", "Everton"),
        ("Chelsea", "Tottenham"),
        ("Arsenal", "Chelsea"),
        ("West Ham United", "Tottenham"),
        ("Manchester United", "Liverpool"),
        ("Newcastle United", "Manchester United"),
        ("Aston Villa", "Birmingham City"),
        ("Brentford", "Fulham"),
        ("Brighton", "Crystal Palace"),
        ("Bournemouth", "Southampton"),
        ("Leicester City", "Nottingham Forest")
    ]
    if (x, y) in premier_league_derbies or (y, x) in premier_league_derbies:
        derby = True
    else:
        derby = False
    time = 0
    end_match = False
    print(f"its time to get ready for kickoff at {stadiums[x]}"); sleep(1)
    print("here on python sports we have a great match for you today"); sleep(1)
    print(f"its {x} vs {y}"); sleep(1)
    if derby == True:
        print("i hope you are all ready for the derby we have today"); sleep(1)
    print(f"the players are ready to go"); sleep(1)
    print(f"the fans are ready to go"); sleep(1)
    print(f"the managers are ready to go"); sleep(1)
    print("and the lineups are in"); sleep(1)
    print(f"for {x} we have the following players")
    for player, stats in goalkeepers[x].items():
        sleep(0.5)
        print(f"Goalkeeper: {player}")
    positions = {}
    for player, stats in outfield_ten[x].items():
        position = stats["position"]
        if position not in positions:
            positions[position] = []
        positions[position].append(player)
    for position, players_in_position in positions.items():
        print(f"{position}: ", end="")
        for player in players_in_position:
            sleep(0.5)
            print(player, end=" ")
        print()
    sleep(1)
    print(f"for {y} we have the following players")
    for player, stats in goalkeepers[y].items():
        sleep(0.5)
        print(f"Goalkeeper: {player}")
    positions = {}
    for player, stats in outfield_ten[y].items():
        position = stats["position"]
        if position not in positions:
            positions[position] = []
        positions[position].append(player)
    for position, players_in_position in positions.items():
        print(f"{position}: ", end="")
        for player in players_in_position:
            sleep(0.5)
            print(player, end=" ")
        print()
    sleep(1)
    print(f"and its kickoff at {stadiums[x]}")
    while not end_match:
        time += 1
        check = choice(range(1, 101))
        if derby == False:
            std_check=40
        elif derby == True:
            std_check=60
        try:
            if check <= std_check:
                game_events()
        except UnboundLocalError as error:
            print(f"{error}\ncontinuing with std::check as 40")
        if time == 90:  # Reached the 90th minute init
            ext_time = choice(range(1, 2))
            if ext_time == 1:
                check_time = choice(range(1, 11))
                check_time+=1
                while check_time != 0:
                    check_time-=1
                    ext_time_num_check = " "
                    time += 1
                    check = choice(range(1, 101))
                    if derby == True:
                        std_ext_time_check=80
                    elif derby == False:
                        std_ext_time_check=20
                    try:
                        if check <= std_ext_time_check:
                            game_events()
                    except UnboundLocalError as e:
                        print(f"{e}\nunbound std_ext_time_check\ncontinuing as 20")
                        std_ext_time_check=20
                        game_events()
                    if 10 <= time % 100 <= 20:
                        suffix = "th"
                    else:
                        last_digit = time % 10
                        if last_digit == 1:
                            suffix = "st"
                        elif last_digit == 2:
                            suffix = "nd"
                        elif last_digit == 3:
                            suffix = "rd"
                        else:
                            suffix = "th"
                    print(f"{time}{suffix} minute{ext_time_num_check}of added time")
                    end_match = True
            else:
                print("No added time")
            print(f"and the whistle is blown!\nthe match is over\nFinal score: {x} {goal_team_a} - {goal_team_b} {y}")
            if goal_team_a > goal_team_b:
                winner=x
            elif goal_team_a < goal_team_b:
                winner=y
            elif goal_team_a == goal_team_b:
                winner=choice([x , y]) 
            list_special = []
            list_standard = []
            list_full_chosen = []
            list_full = [(player_name, stats) for player_name, stats in outfield_ten[winner].items()]
            if list_full:
                list_full_chosen.append(choice(list_full))
            for player_name, stats in outfield_ten[winner].items():
                if isinstance(stats, dict) and stats.get("special_position") == "Striker":
                    list_special.extend([player_name] * 2)
            for player_name, stats in outfield_ten[winner].items():
                if isinstance(stats, dict) and stats.get("position") == "Forward":
                    list_standard.extend([player_name] * 2)
            list_complete = [*list_special, *list_standard, *[name for name, _ in list_full_chosen]]
            potm=choice(list_complete)
            if outfield_ten[winner][potm]["position"] == "Defender":
                potm_position="Defender"
            elif outfield_ten[winner][potm]["position"] == "Midfielder":
                potm_position="Midfielder"
            elif outfield_ten[winner][potm]["position"] == "Forward":
                potm_position="Forward"
            goal_value=outfield_ten[winner][potm]['goals_total_match']
            
            goal_value=goal_value*10
            goal_value_2=goal_value*2
            if potm_position ==  "Forward":
                try:
                    shots_total=choice(range(goal_value, (goal_value * 4)))
                    shots_total_on_target=choice(range(goal_value, shots_total))
                except IndexError:
                    shots_total=choice(range(0,10))
                    shots_total_on_target=choice(range(goal_value, shots_total))
            else:
                try:
                    shots_total=choice(range(goal_value, goal_value_2))
                    shots_total*=100
                    shots_total_on_target=choice(range(goal_value_2, shots_total))
                    shots_total_on_target*=100
                except IndexError:
                    try:
                        shots_total=choice(range(0,10))
                        shots_total_on_target=choice(range(goal_value, shots_total))
                        shots_total_on_target*=100
                        shots_total*=100
                    except IndexError:
                        shots_total=choice(range(0,10))
                        shots_total_on_target=choice(range(0, 10))
                        shots_total_on_target*=100
                        shots_total*=100
            if outfield_ten[winner][potm]["position"] == "Forward":
                shots_total+=choice(range(10, 30))
                shots_total_on_target+=choice(range(10, 20))
            if potm_position == "Midfielder":
                passes = choice(range(80,111))
                passing_accuracy=choice(range(85,101))
            else:
                passes=choice(range(50,111))
                passing_accuracy=choice(range(65,101))
            if potm_position == "Defender":
                tackles_=choice(range(30,110))
                blocks=choice(range(30,110))
            else:
                tackles_=choice(range(0,60))
                blocks=choice(range(0,30))
            categories = ['Goals Scored', 'shots total', 'Shots on target', 'Passes', 'passing accuracy', "tackles", "blocks"]
            values = [goal_value, shots_total, shots_total_on_target, passes, passing_accuracy,  tackles_, blocks]
            num_categories = len(categories)
            angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
            values += values[:1]
            angles += angles[:1]
            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
            ax.plot(angles, values, linewidth=2, linestyle='solid', label='player of the match')
            ax.fill(angles, values, alpha=0.25)
            ax.set_yticklabels([])  # Nee radial labels
            ax.set_xticks(angles[:-1])  # gets rid of that stupid last angle overlap
            ax.set_xticklabels(categories)
            plt.title(f"player of the match | {potm}", y=1.1)
            plt.show()
            #https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_bar.html
            error_log()
            exit()

def select_teams():
    global team_a
    global team_b
    team_a = None
    team_b = None
    team_chosen = False
    team_counter = 0

    print("Please select first team:")
    print("\n".join([f"{i+1}. {team}" for i, team in enumerate(teams)]))

    random_or_manual = int(input("Would you like to select teams manually (1) or randomly (2)? "))

    if random_or_manual == 2:
        team_a = choice(teams)
        team_b = choice(teams)
        while team_a == team_b:
            team_b = choice(teams)
        print(f"Teams selected: {team_a} vs {team_b}")
        return team_a, team_b

    while team_counter < 2:
        try:
            if team_counter == 0:
                print("\nSelect first team:")
            else:
                print("\nSelect second team:")

            team_decision = int(input("Enter your choice (1-20): "))
            if 1 <= team_decision <= 20:
                selected_team = teams[team_decision - 1]
                confirm = int(input(f"You have selected {selected_team}, is this correct? (1 for yes, 2 for no) "))

                if confirm == 1:
                    if not team_chosen:
                        team_a = selected_team
                        team_chosen = True
                        team_counter += 1
                    else:
                        if selected_team != team_a:
                            team_b = selected_team
                            team_counter += 1
                        else:
                            print("You have selected the same team twice, please select a different team")

        except ValueError:
            print("Please enter a valid number")
    return team_a, team_b


def start_menu():
    global team_list
    team_a, team_b = select_teams()
    if team_a and team_b:
        team_list = [team_a, team_b]
        main(team_a, team_b)





if os.path.isfile(r"D:\vscode work\football game\jsontest.json") == True:
    file_json = r"D:\vscode work\football game\jsontest.json"
elif os.path.isfile(r"G:\vscode work\football game\jsontest.json") == True:
    file_json = r"G:\vscode work\football game\jsontest.json"
else:
    print("file not found")
    fileNotFound=True
    while fileNotFound == True:
        try:
            home_or_college=int(input("are you in college (1) or at home (2)"))
        except ValueError as error:
            print(f"{error}\ntry again, you entered an incorrect data type...")
        finally:
            fileNotFound=False
    match home_or_college:
        case 1:
            file_json=(r"D:\vscode work\football game\jsontest.json")
        case 2:
            file_json=(r"G:\vscode work\football game\jsontest.json")
        case _:
            print("error line 1546")
if os.path.isfile(file_json) == False:
    with open(file_json, "w", encoding="utf-8") as js_file:
        dump(outfield_ten, js_file, indent=4, ensure_ascii=False)
        print("Dumped")
elif os.path.isfile(file_json) == True:
    print("file found")

start_menu()
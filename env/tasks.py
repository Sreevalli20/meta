TASKS = {
    "easy": {
        "ticket_id": 1,
        "message": "I forgot my password. Help me reset it.",
        "expected": ["reset link", "password reset"]
    },
    "medium": {
        "ticket_id": 2,
        "message": "My order hasn’t arrived yet and it's been 10 days.",
        "expected": ["track", "delay", "refund"]
    },
    "hard": {
        "ticket_id": 3,
        "message": "I was charged twice but only received one item.",
        "expected": ["refund", "double charge", "apology"]
    }
}

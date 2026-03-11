styles = {
    "dentist": {
        "tone": "trustworthy, clean, professional medical tone",
        "visual_style": "bright clinic interior, smiling patients, modern dental equipment",
        "marketing_focus": "family safety, healthy smiles, comfort",
    },
    "coffee shop": {
        "tone": "warm, cozy, lifestyle-oriented",
        "visual_style": "coffee steam, wooden interior, barista preparing drinks",
        "marketing_focus": "daily ritual, relaxation, community vibe",
    },
    "plumber": {
        "tone": "reliable, practical, problem-solving",
        "visual_style": "technician repairing pipes, home interior, tools",
        "marketing_focus": "fast service, trust, fixing urgent problems",
    },
    "restaurant": {
        "tone": "inviting, flavorful, vibrant",
        "visual_style": "chef plating food, warm lighting, people enjoying meals",
        "marketing_focus": "taste experience, atmosphere, social dining",
    },
    "retail": {
        "tone": "friendly, upbeat, promotional",
        "visual_style": "store interior, product displays, happy customers",
        "marketing_focus": "special offers, product variety, shopping experience",
    },
}


def get_industry_style(industry):

    industry = industry.lower()

    return styles.get(
        industry,
        {
            "tone": "professional and friendly",
            "visual_style": "local business environment",
            "marketing_focus": "customer benefits and trust",
        },
    )

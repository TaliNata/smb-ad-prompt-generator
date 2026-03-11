from industry_styles import get_industry_style


def build_prompt(business, industry, city, offer, audience):

    style = get_industry_style(industry)

    prompt = f"""
Create a structured template for a 12-second CTV advertisement.

Business: {business}
Industry: {industry}
Location: {city}
Offer: {offer}
Audience: {audience}

Brand tone:
{style['tone']}

Visual style:
{style['visual_style']}

Marketing focus:
{style['marketing_focus']}

Return in this format:

AD_SCRIPT:
...

SCENES:
1.
2.
3.

VOICEOVER:
...

CTA:
...
"""

    return prompt

# SMB Ad Prompt Generator

CLI tool for generating structured CTV advertisement templates for small businesses using LLMs.

## Features

- Prompt templating
- Industry-specific marketing styles
- Multi-model comparison
- OpenRouter API integration

## Example

Run:

python main.py

Enter business information and compare responses from multiple LLMs.

## Models tested

- GPT-4o-mini
- Claude 3 Haiku
- Llama 3.1

---
## Example Output


=== SMB Ad Prompt Generator ===

Business name: Mussels Jonny's restaurant
Industry: restaurant
City: New York
Offer: Pasta for Free to French Mussels
Target audience: wealthy middle age people

Generated Prompt:

Create a structured template for a 12-second CTV advertisement.

Business: Mussels Jonny's restaurant
Industry: restaurant
Location: New York
Offer: Pasta for Free to French Mussels
Audience: wealthy middle age people

Brand tone:
inviting, flavorful, vibrant

Visual style:
chef plating food, warm lighting, people enjoying meals

Marketing focus:
taste experience, atmosphere, social dining

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


=========== MODEL COMPARISON ===========


--- MODEL: openai/gpt-4o-mini ---

AD_SCRIPT:  
"Indulge in the taste of the sea at Mussels Jonny's. Enjoy our vibrant French Mussels and get a delicious pasta, free! Join the feast in the heart of New York!"  

SCENES:
1. Close-up of a chef expertly plating a colorful dish of French Mussels with warm lighting casting a glow on the food.
2. Elegant shots of wealthy diners laughing and clinking glasses over beautifully presented meals, immersed in a cozy atmosphere.
3. A final shot of a table filled with delectable dishes, capturing the vibrant social dining experience alongside a text overlay: "Free Pasta with French Mussels - Only at Mussels Jonny's."

VOICEOVER:
"Delight in flavors that transport you to the coast of France. Savor deeply and dine richly at Mussels Jonny's!"

CTA:
"Visit us today for your free pasta with every order of French Mussels!"

----------------------------------------


--- MODEL: anthropic/claude-3-haiku ---

AD_SCRIPT:

A vibrant, flavorful invitation to Mussels Jonny's in New York, where you can enjoy a complimentary pasta dish with every order of their renowned French mussels. 

SCENES:
1. A close-up shot of a chef expertly plating a dish of steaming mussels in a rich, creamy sauce.
2. The camera pans across a cozy, dimly lit dining room, showcasing the warm atmosphere and people enjoying their meals together.
3. A group of well-dressed, middle-aged friends are seated at a table, laughing and savoring their mussels and pasta dishes.

VOICEOVER:
Indulge in the taste of authentic French mussels at Mussels Jonny's, where every order comes with a complimentary pasta dish. Discover the vibrant flavors and inviting atmosphere that make our restaurant the perfect destination for a delightful dining experience.

CTA:
Visit Mussels Jonny's in New York and savor the taste of France. Enjoy a free pasta dish with every order of our renowned mussels. Reservations recommended.      

----------------------------------------


--- MODEL: meta-llama/llama-3.1-70b-instruct ---

Here is a structured template for a 12-second CTV advertisement for Mussels Jonny's restaurant:

**AD_SCRIPT:**

(0s-3s) Introduction to Mussels Jonny's restaurant in New York
(4s-6s) Highlight the offer: Pasta for Free with French Mussels
(7s-9s) Showcase the taste experience and atmosphere
(10s-12s) Call to action and invitation to dine

**SCENES:**

1. (0s-3s) Exterior shot of Mussels Jonny's restaurant in New York, with a warm and inviting glow.
2. (4s-6s) Close-up of a chef expertly plating a dish of French Mussels with a side of pasta.
3. (7s-9s) Cut to a bustling dining area with happy customers enjoying their meals and laughing together.

**VOICEOVER:**

"Savor the flavor of the city at Mussels Jonny's, where every bite is a taste experience. Indulge in our signature French Mussels, paired with a complimentary side of pasta. Join us for a vibrant and inviting dining atmosphere that's perfect for any occasion. Come taste the difference for yourself."

**CTA:**

"Visit Mussels Jonny's today and enjoy Pasta on us with the purchase of our French Mussels. Book your table now at [website URL or phone number]"

This template aims to capture the essence of Mussels Jonny's brand tone, visual style, and marketing focus, while showcasing the offer and inviting the target audience to experience the restaurant.

----------------------------------------

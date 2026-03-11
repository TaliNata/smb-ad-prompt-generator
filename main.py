from prompt_builder import build_prompt
from model_runner import run_model_comparison


def get_user_input():

    print("\n=== SMB Ad Prompt Generator ===\n")

    business = input("Business name: ")
    industry = input("Industry: ")
    city = input("City: ")
    offer = input("Offer: ")
    audience = input("Target audience: ")

    return business, industry, city, offer, audience


def main():

    # 1. Получаем данные
    business, industry, city, offer, audience = get_user_input()

    # 2. Создаем промпт
    prompt = build_prompt(business, industry, city, offer, audience)

    print("\nGenerated Prompt:\n")
    print(prompt)

    # 3. Сравнение моделей
    print("\n=========== MODEL COMPARISON ===========\n")

    run_model_comparison(prompt)


if __name__ == "__main__":
    main()

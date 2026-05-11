import time

print("=" * 40)
print("ТРЕНАЖЁР СКОРОСТИ ПЕЧАТИ")
print("=" * 40)

text = "привет мир как дела сегодня отличный день"

print("\nНапечатайте этот текст:")
print(f"\n>>> {text} <<<\n")

input("Нажмите Enter, когда будете готовы...")

start = time.time()
user_input = input("Ваш ввод: ")
end = time.time()

if user_input == text:
    print(f"\n✅ Отлично! Ваше время: {end - start:.2f} секунд")
else:
    print("\n❌ Ошибка! Текст не совпадает. Попробуйте ещё раз.")

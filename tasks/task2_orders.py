"""
Задание 2: Анализ данных о заказах из CSV-файла
- В CSV-файле содержатся данные о заказах: «Номер заказа», «Клиент», «Дата», «Сумма».
- Прочитайте данные из файла в DataFrame.
- Выведите первые десять строк.
- Определите количество заказов каждого клиента.
- Найдите максимальную и минимальную суммы заказов.
- Подсчитайте общую сумму всех заказов.
"""

from pathlib import Path
import pandas as pd


def run_task2():
    print("=" * 60)
    print("ЗАДАНИЕ 2: Анализ заказов из CSV-файла")
    print("=" * 60)

    # Путь к файлу с данными (поддерживает запуск как из корня проекта, так и из папки tasks)
    csv_path = Path(__file__).parent.parent / "data" / "orders.csv"
    if not csv_path.exists():
        # Если запускается прямо из текущей директории
        csv_path = Path("data/orders.csv")

    # 1. Читаем данные из CSV-файла
    orders_df = pd.read_csv(csv_path)

    # 2. Выводим первые 10 строк
    print("\n1. Первые 10 строк таблицы заказов:")
    print(orders_df.head(10))

    # 3. Количество заказов каждого клиента
    # Способ 1: value_counts() - самый лаконичный и быстрый способ в pandas
    orders_per_client = orders_df["Клиент"].value_counts()
    print("\n2. Количество заказов каждого клиента (через value_counts()):")
    print(orders_per_client)

    # Способ 2: groupby (также рассматривался на занятиях)
    orders_per_client_groupby = orders_df.groupby("Клиент")["Номер заказа"].count()
    print("\n   Альтернатива через groupby('Клиент').count():")
    print(orders_per_client_groupby)

    # 4. Максимальная и минимальная суммы заказов
    max_amount = orders_df["Сумма"].max()
    min_amount = orders_df["Сумма"].min()
    print(f"\n3. Максимальная сумма заказа: {max_amount:.2f}")
    print(f"   Минимальная сумма заказа: {min_amount:.2f}")

    # Дополнительно: найдем строки с этими заказами через idxmax() и idxmin()
    max_order = orders_df.loc[orders_df["Сумма"].idxmax()]
    min_order = orders_df.loc[orders_df["Сумма"].idxmin()]
    print(f"   Заказ с максимальной суммой: №{max_order['Номер заказа']} ({max_order['Клиент']}) на {max_order['Сумма']}")
    print(f"   Заказ с минимальной суммой: №{min_order['Номер заказа']} ({min_order['Клиент']}) на {min_order['Сумма']}")

    # 5. Общая сумма всех заказов
    total_amount = orders_df["Сумма"].sum()
    print(f"\n4. Общая сумма всех заказов: {total_amount:.2f}")

    return orders_df


if __name__ == "__main__":
    run_task2()

import converter  # Подключаем вашу программу

def test_american_to_metric():
    assert converter.american_to_metric(1, "inches") == 2.54
    assert converter.american_to_metric(2, "feet") == 60.96
    assert converter.american_to_metric(0, "inches") == 0

def test_metric_to_american():
    assert converter.metric_to_american(2.54, "centimeters") == 1
    assert converter.metric_to_american(30.48, "meters") == 1
    assert converter.metric_to_american(0, "centimeters") == 0

if __name__ == "__main__":
    test_american_to_metric()
    test_metric_to_american()
    print("Все тесты пройдены успешно!")

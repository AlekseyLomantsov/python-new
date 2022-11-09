# Система собирает информацию с датчиков, в не есть модуль логирования,
# который заносит в жунал все обращения к датчикам.
# В системе есть модуль, выполняющий обращения для получения данных с датчиков
# и модуль генерации html-представления.
# Запуск системы осуществляется из головного модуля.

# Выделим 5 модулей:
# 1 - сбор инф с датчиков (data_provider)
    # get_temperature(температура), get_preassure(давления), get_wind_speed(скорость ветра)

# 2 - логирование (logger)
    # temperature_logger, preassure_logger, wind_speed_logger

# 3 - UI (user_interface)
    # temperature_view, preassure_view, wind_speed_view

# 4 - html-генератор (html_creater)
    # create
# 5 - главный модуль (main)
    # ...

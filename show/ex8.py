formatter = "{} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("Раз", "два", "три", "четрые"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
            "Спят в конюшне пони,",
            "начал пес дремать,",
            "только мальчик Джонни",
            "не ложиться спать!"    
))
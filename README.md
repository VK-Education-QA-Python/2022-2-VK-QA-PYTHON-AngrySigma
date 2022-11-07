##Файлы для парсинга логов
###Bash
**get_lines.sh**<br/>
Собирает число строк в файле<br/>
`Number of requests in log file:<br/><число запросов>`
**get_request_methods.sh**<br/>
Собирает число запросов с каждым методом<br/>
`GET requests: <число запросов>`<br/>
`HEAD requests: <число запросов>`<br/>
`...`<br/>
**get_popular_requests.sh**<br/>
Собирает список из 10 самых популярных запросов<br/>
`Address: <url>, requests: <число запросов>`<br/>
`...`<br/>
**get_largest_400_requests.sh**<br/>
Собирает 5 самых больших по размеру из запросов, которые окончились ошибкой клиента<br/>
`Address: <url>`<br/>
`Status code: <код ответа>`<br/>
`Size: <размер запроса>`<br/>
`IP: <ip>`<br/>
`...`<br/>
**get_users_500.sh**
Собирает 5 IP, наибольшее число запросов с которых окончились ошибкой сервера<br/>
`IP: <ip> server errors:<число ошибок>`
`...`<br/>

###Python
Все названия соответствуют скриптам на bash<br/>
Все скрипты имеют возможность запуска с флагом --json для записи результатов в файл .json<br/>
**get_request_methods.py**<br/>
Словарь `{REQUEST_METHOD: NUMBER_OF_REQUESTS}`<br/>
**get_popular_requests.py**<br/>
OrderedDict `{URL: NUMBER_OF_REQUESTS}`<br/>
**get_users_500.py**<br/>
OrderedDict `{IP: NUMBER_OF_REQUESTS}`<br/>
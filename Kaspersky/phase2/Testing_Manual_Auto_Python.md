<img width="1253" alt="image" src="https://user-images.githubusercontent.com/58044383/233790787-246b808d-50eb-4476-a647-025acd3fae90.png">

### Задача 1.
1) Есть экранная форма, на которой есть поле ввода (по словам разрабочика - числовое поле) и некая (большая красная) кнопка, которая запускает обработку введенных данных
Как бы проверили корректность работы такой формы?

2) Есть консольная форма, с использованием которой приложение может подключаться к серверу (например, подключение к игровому серверу в онлайн игре). Команда подключения:
    connect %server_address%
Как бы вы проверяли корректность работы?

3) Есть веб сайт, на его странице есть форма ввода пути к файлу с резюме, которое будет использоваться потенциальными работодателями для оценки кандидатов, и кнопка Submit. Необходимо расписать набор проверок - как бы вы проверяли, что эта форма работает корректно

4) Есть веб сайт, на его странице есть форма ввода пути к файлу с картинкой, которая будет использоваться как аватар (например, на каком-либо форуме) и кнопка Submit. Необходимо расписать набор проверок - как бы вы проверяли, что эта форма работает корректно


### Задача 2.
Есть несколько Героев (скажем, N). У каждого Героя есть набор Сверхпособностей, закодированных целыми числами. И есть Миссия, для которой нужны M Героев, у которых есть предопределённые Сверхспособности. Для упрощения задачи примем, что M == N.


Примеры входных данных:

heroes = (("Илья М.", (1, 2, 3)),)

mission = (1,)

ответ: ("Илья М.",)



heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)

mission = (1, 2)

ответ: ("Алёша П.", "Илья М.",)



heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )), ("Добрыня Н.", (2, 3)))

mission = (1, 1, 2)

ответ: ("Илья М.", "Алёша П.", "Добрыня Н.")



heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)

mission = (1, 5)

ответ: ()


Задание: написать функцию, которая будет распределять Героев по ролям для Миссии, если это возможно.


### Задача 3.
Придумать и описать тестовые сценарии (тест кейсы) для https://developers.virustotal.com/reference/overview

Most popular API endpoints
Upload a file for scanning: analysis your file with 70+ antivirus products, 10+ dynamic analysis sandboxes and a myriad of other security tools to produce a threat score and relevant context to understand it.
Get a file report by hash: given a {md5, sha1, sha256} hash, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products, 10+ dynamic analysis sandboxes and a myriad of other security tools and datasets.
Scan URL: analysis your URL with 70+ antivirus products/blocklists and a myriad of other security tools to produce a threat score and relevant context to understand it.
Get a URL analysis report: given a URL, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.
Get a domain report: given a domain, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.
Get an IP address report: given an IP address, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.
В качестве клиента использовать один из вариантов:

·       [Postman](https://www.postman.com/downloads/) или Insomnia

·       Curl (https://curl.se/)

·       VT-PY (https://github.com/VirusTotal/vt-py)

·       VT-CLI (https://github.com/VirusTotal/vt-cli)

Формат тестового сценария:

Test case № ХХ: <Название сценария>

STEPS:

#

Action

Expected value

1




2




Дополнительное задание: автоматизировать один или несколько тестовых сценариев используя один из вариантов:

·       Python + pytest

·       C# + Nunit или MsTest

·       Скриптами в postman

·       PowerShell или Bash + curl или VT-CLI

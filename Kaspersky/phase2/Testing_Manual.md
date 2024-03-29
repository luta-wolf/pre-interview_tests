<img width="1724" alt="image" src="https://user-images.githubusercontent.com/58044383/233794618-d4df1935-b01f-491f-bd77-97f3e58bdc63.png">

## Задание 1.
Протестировать сайт с созданием клиента без активации продукта https://mdr.kaspersky.com/ .

Оформить тест кейсы. Указать какие техники тест дизайна применялись при написании тест кейса.

## Задание 2.
### Задача 1
Есть форма «Документы», которая позволяет загружать, редактировать и удалять документы в списке. Оператор может загрузить новый файл в список по кнопке «Добавить документ», при нажатии на которую открывается окно с полями Название, Описание и кнопкой загрузки файла. Файлы документов записываются в системную папку Documents -> Пользовательские документы. Также по кнопке «Изменить документ» можно отредактировать атрибуты и заменить ранее добавленный файл.

Список документов состоит из:
- Иконка с форматом файла;
- Название документа;
- Автор (пользователь, добавивший документ);
- Дата последнего изменения (с сортировкой);
- Размер файла.
Составьте список проверок (чеклист) для окна «Изменить документ».

### Задача 2
Протестируйте Login Form на https://demo.applitools.com/ - составьте тест-кейсы, а также оформите несколько баг-репортов найденных ошибок и замечаний.

Шаблон тест-кейса

	Title: Заголовок тест-кейса
	Precondition: Предварительные условия прохождения кейса (если необходимо)
	Step 1
	Action: Описание действия
	Expected Result: Ожидаемый результат
	…
	Step N
	Action:
	Expected Result:

Шаблон баг-репорта

	Title: Заголовок бага
	Environment/Precondition: Техническая информация, предварительные условия воспроизведения - версия программы, браузер, локализация и т.д. (если необходимо)
	Priority: Приоритет бага (от 1 до 4, где 1 – высокий приоритет, 4 – низкий)
	Steps:
	Сценарий воспроизведения по шагам
	1.
	…
	N.
	Actual Result: Фактический результат
	Expected Result: Ожидаемый результат
_P.S. Для наглядности можно добавить скриншоты_

### Задача 3
Разработчики закончили разработку новой версии приложения/продукта и
выдали ее Вам на проверку. При тестировании оно зависает.
Каковы будут ваши дальнейшие действия?

### Задача 4
Напишите ответы/команды на нижеперечисленные практические задачи по Linux.
1. Как узнать, как работает команда и какие у нее есть параметры?
Например, команда ls.
2. С помощью какой команды/команд можно изменить имя хоста в CentOS 7?
3. Создайте пользователя tester с UID=5000, паролем "Qwerty123!", и выставите ему в качестве shell "/bin/zsh". Затем создайте группу testgroup с GID=6000 и добавьте в нее пользователя tester так, чтобы его home-директория была /home/testgroup/tester
4. Пользователь tester должен иметь доступ к директории user и файлу abc.txt в другой директории, но они были созданы под рутом. Какими командами можно изменить владельца файла и папки на tester и проверить результат?
5. Проведите поиск всех файлов tхt-формата в каталоге /usr и скопируйте их в пользовательскую папку copies (попробуйте сделать 1 командой).Соедините содержимое всех этих файлов в один - аll.tхt
6. Создайте архив директории home/dir (не пустой, содержит какие-либо файлы) и узнайте его размер. Создайте сжатый архив той же папки. Удалите файлы, которые были ранее архивированы, а затем распакуйте архив в ту же папку.
7. Создайте файл check_rights.txt, наделите его полными правами. Запретите запись пользователям группы testgroup. Затем запретите всем остальным пользователям все, кроме чтения.


## Задание 3.
1. Скачать и научиться пользоваться текстовым редактором [KeyNote v.1.7.4.1](https://sourceforge.net/projects/keynote-newfeat/files/KeyNote-NewFeatures%20Binary/KeyNote%20NF%20%201.7.4/Release_1.7.4.1.zip/download) (Windows)
2. Протестировать основные пользовательские сценарии KeyNote `v.1.7.4.1`. Сделать описание обнаруженных ошибок в свободной форме.
3. Описать несколько тест кейсов для базового (Smoke) тестирования KeyNote `v.1.7.4.1`.

## Задание 4.
### Задача 1
Представь ситуацию: к тебе подходит твой руководитель (QA Lead) и ставит задачу протестировать кнопку. Ниже распиши, с чего ты начнешь?

### Задача 2
Представь ситуацию: команда разрабатывает веб-приложение с регистрацией и аутентификацией.

Твой рабочий график 10:00-19:00 (с перерывом в 60 минут), команда разработки передала тебе задачу на тестирование в 12:00, а релиз завтра в
10:00 – времени очень мало.

Задача, которую выполнили разработчики – как раз аутентификация. Ранее уже была разработана и протестирована регистрация (но тест-кейсы написать забыли, так бывает).

На текущий момент ограничились только регистрацией с электронной почтой, без двухфакторной аутентификации, без номера телефона и т.д. Просто почта и пароль, сложность пароля любая, символы пароля любые. На экране только поле ввода почты, поле ввода пароля, кнопки «Зарегистрироваться» и «Войти». Регистрация и аутентификация происходит на одном и том же экране,
используя одну из двух кнопок. После регистрации должно прийти письмо на регистрируемую почту об успешной регистрации.

Тест-кейсы заранее не разрабатывали, чек-лист тоже.

Ниже распиши, как будешь решать данную задачу?

### Задача 3
Представь ситуацию: ты тестируешь регистрацию в веб-приложении, используя браузер Chrome. Открываешь сайт, вводишь почту, вводишь пароль, жмешь «Зарегистрироваться» и тут появляется ошибка с кодом 400. Пробуешь еще раз – ошибка воспроизводится снова. Теперь необходимо оформить
баг-репорт на разработчика.

Ниже распиши, как будет выглядеть баг-репорт (по всем канонам оформления, и так, чтобы разработчику было достаточно информации) и какие
инструменты будешь использовать для логов/скриншотов и прочего. Из инструментов есть только браузер и встроенные приложения оконной операционной системы. В баг-репорт можно добавлять файлы вложениями.

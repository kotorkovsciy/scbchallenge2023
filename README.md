<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@1,300&family=Nunito:ital,wght@0,200;0,300;0,400;0,500;1,200;1,300;1,400;1,900&family=Roboto+Mono:wght@100&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@1,300&family=Nunito:ital,wght@0,200;0,300;0,400;0,500;1,200;1,300;1,400;1,900&family=Roboto+Mono:wght@100&display=swap" rel="stylesheet">
<img src="https://contestfiles.storage.yandexcloud.net/companies/86a6a31f4467a95b9020dad414fbf7e0/contests/871/8pu1xjeH_1681210748.webp">


<h1 style="font-family: Roboto Mono; text-align: center;">Команда: letter-k</h1>
<hr style="height:1px; color:black; background-color:gray">

<img src="https://drive.google.com/uc?export=view&id=1s9A9IAjZnzEEbT4MkYZWajShLFcSibvC">

<hr style="height:1px; color:black; background-color:gray">

<ul style="margin-top: 50px">
<li><a href="#visual">Визуальное описание функционала системы</a></li>
<li><a href="#stack">Описание используемого технологического стека 
и инструментов</a></li>
<li><a href="#db">Описание сервисов, сущностей БД, и других артефактов проекта</a></li>
<li><a href="#arh_fis">Описания архитектур системы физическая</a></li>
<li><a href="#arh_log">Описания архитектур системы логическая</a></li>

<li><a href="#safety">Описание решения с точки зрения безопасности</a></li>
<li><a href="#host">Как захостить проект</a></li>
</ul>

<hr style="height:1px; color:black; background-color:gray">

<p style="margin-top:50px; font-family: Merriweather; text-align: center;" id="visual">Визуальное описание функционала системы</p>
<a href="https://drive.google.com/file/d/1f9Boz0PfWSWgU2f03RFc9vKhFEpI6Odh/view?usp=drive_link"><img src="https://drive.google.com/uc?export=view&id=1f9Boz0PfWSWgU2f03RFc9vKhFEpI6Odh"></a>

<a href="https://drive.google.com/file/d/12E6a3xydc6kermYx6PETt7-4lXs1wKDM/view?usp=drive_link"><img style="margin-top:50px;" src="https://drive.google.com/uc?export=view&id=12E6a3xydc6kermYx6PETt7-4lXs1wKDM"></a>

<a href="https://drive.google.com/file/d/1AdC6QslcJ1KqB3axT71SqrIeEOGCMieQ/view?usp=drive_link"><img style="margin-top:50px;" src="https://drive.google.com/uc?export=view&id=1AdC6QslcJ1KqB3axT71SqrIeEOGCMieQ"></a>


<hr style="height:1px; color:black; background-color:gray">

<p style="margin-top:50px; font-family: Merriweather; text-align: center;" id="stack">Описание используемого технологического стека 
и инструментов</p>

<table class="iksweb">
	<tbody>
		<tr>
			<td colspan="2">Для разработки веб-приложений с использованием Django требуется следующий технологический стек и инструменты:</td>
		</tr>
		<tr>
			<td>Django</td>
			<td>Python-фреймворк высокого уровня, который облегчает создание веб-приложений. Django предоставляет мощные инструменты для управления базами данных, обработки URL-запросов, создания шаблонов и многое другое.
</td>
		</tr>
		<tr>
			<td>JavaScript (JS)</td>
			<td>Язык программирования, который используется для создания интерактивных элементов на стороне клиента веб-приложения. В связке с Django, JS может использоваться для добавления динамического поведения, отправки асинхронных запросов на сервер и взаимодействия с API.
</td>
		</tr>
		<tr>
			<td>HTML</td>
			<td>Язык разметки для определения структуры веб-страницы.
CSS: Язык таблиц стилей для оформления внешнего вида элементов на веб-странице.</td>
		</tr>
		<tr>
			<td>Cython</td>
			<td>Инструмент для ускорения функций, написанных на Python.
Request: Библиотека для выполнения запросов с сайта hh.</td>
		</tr>
		<tr>
			<td>Beautiful
Soup4
(bs4)
</td>
			<td>Библиотека для парсинга HTML и XML.
django-environ: Модуль для управления настройками Django из переменных окружения.</td>
		</tr>
	</tbody>
</table>

<hr style="height:1px; color:black; background-color:gray">

<p style="margin-top:50px; font-family: Merriweather; text-align: center;" id="db">Описание сервисов, сущностей БД, и других артефактов проекта
</p>

<table class="iksweb">
	<tbody>
		<tr>
			<td>django.contrib.admin
</td>
			<td>Это административный интерфейс Django, который предоставляет удобный способ управления моделями и данными в базе данных. Включает модель LogEntry для отслеживания действий пользователей.
</td>
		</tr>
		<tr>
			<td>django.contrib.auth
</td>
			<td>Этот сервис обеспечивает аутентификацию и авторизацию пользователей. Включает модели AbstractUser, Permission, Group и User для управления пользователями, разрешениями и группами.
</td>
		</tr>
		<tr>
			<td>django.contrib.contenttypes
</td>
			<td>Сервис, который обеспечивает отслеживание типов контента в приложениях Django. Включает модель ContentType для хранения информации о типах моделей.
</td>
		</tr>
		<tr>
			<td>django.contrib.sessions
</td>
			<td>Этот сервис отвечает за управление сеансами пользователей и хранение данных сеансов. Включает модели AbstractBaseSession и Session
</td>
		</tr>
		<tr>
			<td>jobportal
</td>
			<td>Сервис, разработанный в проекте jobportal. Включает модель UserProfile для хранения профилей пользователей и их ролей.
</td>
		</tr>
	</tbody>
</table>

<table class="iksweb">
	<tbody>
		<tr>
			<td>Модель</td>
			<td>Описание
</td>
		</tr>
		<tr>
			<td>LogEntry
</td>
			<td>Хранит информацию о действиях пользователей в административном интерфейсе. Содержит поля id, content_type, user, action_flag, action_time, change_message, object_id и object_repr. Связана с моделями User и ContentType через внешние ключи.
</td>
		</tr>
		<tr>
			<td>AbstractUser
</td>
			<td>Абстрактная модель, которая представляет пользователей. Включает поля date_joined, email, first_name, is_active, is_staff, is_superuser, last_login, last_name, password и username. Наследуется от моделей AbstractBaseUser и PermissionsMixin.
</td>
		</tr>
		<tr>
			<td>Permission
</td>
			<td>Представляет разрешения, которые могут быть назначены пользователям или группам. Содержит поля id, content_type, codename и name. Связана с моделью ContentType через внешний ключ
</td>
		</tr>
		<tr>
			<td>Group
</td>
			<td>Представляет группы пользователей. Содержит поля id и name. Связана с моделью Permission через поле permissions (ManyToManyField)
</td>
		</tr>
		<tr>
			<td>МUser
</td>
			<td>Представляет пользователей. Содержит поля id, date_joined, email, first_name, is_active, is_staff, is_superuser, last_login, last_name, password и username. Связана с моделями Group и Permission через соответствующие поля (ManyToManyField). Наследуется от модели AbstractUser.
</td>
		</tr>
		<tr>
			<td>ContentType
</td>
			<td>Хранит информацию о типах моделей. Содержит поля id, app_label и model.
</td>
		</tr>
		<tr>
			<td>AbstractBaseSession
</td>
			<td>Абстрактная модель, представляющая базовую информацию о с, truncated for brevity. пользовательской сессии. Содержит поля session_key, session_data, expire_date и session_id.
</td>
		</tr>
		<tr>
			<td>Session
</td>
			<td>Представляет конкретную пользовательскую сессию. Содержит поля session_key, session_data, expire_date и session_id. Наследуется от модели AbstractBaseSession.
</td>
		</tr>
		<tr>
			<td> UserProfile
</td>
			<td>Модель Хранит информацию о профилях пользователей и их ролях. Содержит поля id, user, role и bio. Связана с моделью User через внешний ключ.
</td>
		</tr>
	</tbody>
</table>

<a href="https://drive.google.com/file/d/18W34Kx7kl8xcqdl2z0RoukuNgMr5yE2L/view?usp=drive_link"><img style="margin-top:100px;" src="https://drive.google.com/uc?export=view&id=18W34Kx7kl8xcqdl2z0RoukuNgMr5yE2L"></a>

<table class="iksweb">
	<tbody>
		<tr>
			<td>Шаблоны (templates)
</td>
			<td>Файлы, содержащие HTML-код с вставками динамических данных, используемые для отображения пользовательского интерфейса.
</td>
		</tr>
		<tr>
			<td>URL-шаблоны (urls)
</td>
			<td>Файлы, которые связывают URL-адреса с соответствующими представлениями.
</td>
		</tr>
		<tr>
			<td>Формы (forms)
</td>
			<td>которые определяют поля и правила валидации для пользовательского ввода.
</td>
		</tr>
		<tr>
			<td>Статические файлы (static)
</td>
			<td>Ресурсы, такие как CSS-стили, JavaScript-скрипты, изображения, используемые в пользовательском интерфейсе.
</td>
		</tr>
		<tr>
			<td>Миграции (migrations)
</td>
			<td>Файлы, которые описывают изменения структуры базы данных, создаваемые и применяемые с помощью Django ORM.
</td>
		</tr>
		<tr>
			<td>Конфигурационные файлы (settings)
</td>
			<td> Файлы, которые содержат настройки проекта, такие как база данных, аутентификация, статические файлы и другие параметры.
</td>
		</tr>
		<tr>
			<td>Административный интерфейс</td>
			<td>Интерфейс, предоставляемый Django для управления моделями и данными в административной панели.
</td>
		</tr>
		<tr>
			<td colspan="2">Это лишь некоторые из основных сервисов, сущностей БД и артефактов проекта, которые могут присутствовать в Django-приложении. Реальный проект может содержать и другие компоненты в зависимости от его специфики и требований.
</td>
		</tr>
	</tbody>
</table>

<hr style="height:1px; color:black; background-color:gray">

<p style="margin-top:50px; font-family: Merriweather; text-align: center;" id="arh_fis">Описания архитектур системы физическая</p>

<table class="iksweb">
	<tbody>
		<tr>
			<td colspan="2">Физическая архитектура системы определяет физическое размещение компонентов и ресурсов системы.
</td>
		</tr>
		<tr>
			<td>Клиентские устройства
</td>
			<td>Компьютеры, мобильные устройства или другие устройства, на которых пользователи взаимодействуют с сервисом через веб-браузер или веб сайт
</td>
		</tr>
		<tr>
			<td>Веб-сервер
</td>
			<td>Сервер, который принимает запросы от клиентских устройств через протокол HTTP или HTTPS. Веб-сервер обрабатывает эти запросы и передает их в приложение Django для дальнейшей обработки
</td>
		</tr>
		<tr>
			<td>Django-приложение
</td>
			<td>Это ядро системы, которое содержит бизнес-логику, модели данных, представления и шаблоны. Django-приложение выполняет обработку запросов, взаимодействует с базой данных, формирует и возвращает ответы клиентским устройствам.
</td>
		</tr>
		<tr>
			<td>База данных
</td>
			<td>Django-приложение взаимодействует с базой данных для сохранения и извлечения данных. База данных может быть размещена на отдельном сервере или использовать облачные сервисы баз данных, такие как Amazon RDS или Google Cloud SQL.
</td>
		</tr>
		<tr>
			<td>Системы хранения файлов
</td>
			<td>Для хранения и обработки файлов, таких как загружаемые пользовательские изображения или документы, может использоваться отдельное хранилище файлов, такое как Amazon S3 или Google Cloud Storage
</td>
		</tr>
		<tr>
			<td>Внешние сервисы
</td>
			<td>В приложении могут быть интегрированы внешние сервисы, такие как платежные системы, системы уведомлений или сервисы аутентификации через социальные сети. Взаимодействие с этими сервисами может осуществляться через API.
</td>
		</tr>
	</tbody>
</table>

<p style="margin-top:50px; font-family: Merriweather; text-align: center;" id="arh_log">Описания архитектур системы логическая
</p>

<table class="iksweb">
	<tbody>
		<tr>
			<td colspan="2">Логическая архитектура системы определяет структуру и организацию компонентов и модулей приложения. Это общая логическая архитектура Django-приложения, которая основана на шаблоне проектирования MVC (Model-View-Controller).
</td>
		</tr>
		<tr>
			<td>Клиентские устройства
</td>
			<td>Модель представляет данные и бизнес-логику системы. Она определяет структуру и отношения между данными, а также методы для работы с этими данными. Модель в Django обычно представляется в виде классов Python, которые наследуются от базового класса модели Django
</td>
		</tr>
		<tr>
			<td>Представление (View)
</td>
			<td>Представление определяет, как данные из модели будут отображаться пользователю. Оно обрабатывает запросы от клиентских устройств, получает данные из модели, выполняет необходимую обработку и форматирование данных и передает их в шаблон для отображения.
</td>
		</tr>
		<tr>
			<td>Шаблон (Template)
</td>
			<td>Шаблон содержит HTML-код с вставками динамических данных. Он определяет, как данные будут отображаться пользователю. В шаблоне можно использовать переменные и управляющие конструкции для динамического формирования контента.
</td>
		</tr>
		<tr>
			<td>URL-маршрутизация
</td>
			<td>Django использует URL-шаблоны для связывания URL-адресов с соответствующими представлениями. URL-маршрутизация определяет, какой код будет выполнен при обращении к определенному URL-адресу
</td>
		</tr>
		<tr>
			<td>Формы (Forms)
</td>
			<td>Django предоставляет инструменты для создания и обработки веб-форм. Формы используются для сбора данных от пользователей и их валидации перед сохранением в базе данных.
</td>
		</tr>
		<tr>
			<td>Сервисы и утилиты
</td>
			<td>В приложении могут быть определены дополнительные службы и утилиты, которые выполняют специфические задачи, такие как отправка электронной почты, взаимодействие с API сторонних сервисов и другие.
</td>
		</tr>
	</tbody>
</table>

<hr style="height:1px; color:black; background-color:gray">

<p style="margin-top:50px; font-family: Merriweather; text-align: center;" id="safety">Описание решения с точки зрения безопасности</p>

<table class="iksweb">
	<tbody>
		<tr>
			<td colspan="2">Для обеспечения безопасности при разработке проекта, было уделено внимание следующим аспектам
</td>
		</tr>
		<tr>
			<td>Аутентификация и авторизация пользователей
</td>
			<td>Были использованы механизмы django для аутентификации и авторизации пользователей. Также хранения было осуществлено используя hash-функции для защиты от атак, таких как перебор паролей или словарные атаки 
</td>
		</tr>
		<tr>
			<td>Защита от атак
</td>
			<td>Для обеспечения безопасности  используется защита от атак, таких как XSS (межсайтовый скриптинг) и CSRF (межсайтовая подделка запроса). Для этого используется Django Forms и Django Templates, чтобы защитить приложение от XSS. Также используется Django CSRF, чтобы предотвратить CSRF-атаки.
</td>
		</tr>
		<tr>
			<td>Следование принципам безопасности разработки ПО
</td>
			<td>А также используется строго типизированный язык программирования для предотвращения ошибок типизации в коде, которые могут привести к уязвимостям.
</td>
		</tr>
	</tbody>
</table>

<hr style="height:1px; color:black; background-color:gray">

<p style="margin-top:50px; font-family: Merriweather; text-align: center;" id="host">Как захостить проект</p>

<h3 style="font-family: Tsukimi Rounded;">Windows</h3>

1. Запустить скрипт `compile_pars.ps1` (для этого нужно открыть PowerShell и ввести `.\compile_pars.ps1`).
2. Создать файл .env `New-Item -Path .env -ItemType file` и внести в него свои данные по примеру .env.example.
3. Запуск `python manage.py runserver`

<h3 style="font-family: Tsukimi Rounded;">Linux</h3>

1. Использовать makefile, для этого нужно ввести в терминале `make build`
2. Создать файл .env (`touch .env`) по примеру .env.example. внеся в него свои данные.
3. Запуск `make run`

<h3 style="font-family: Tsukimi Rounded;">Docker</h3>

1. Создать файл .env по примеру .env.example. внеся в него свои данные.
2. Запустите `docker-compose build`
3. Запуск `docker-compose up`

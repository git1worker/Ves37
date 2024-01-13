<?
 
if(isset($_POST["name"]))
{
        if(isset($_POST["name"]))
        {
                $name = $_POST["name"];
        }
        if(isset($_POST["email"]))
        {
                $email= $_POST["email"];
        }
        if(isset($_POST["msg"]))
        {
                $msg = $_POST["msg"];
        }
 
        if($name=="" or $email=="" or $msg=="")
        { // Проверяем на заполненность всех полей.
                echo "Пожалуйста, заполните все поля";
        }
        else
        {
                $ip=$_SERVER["REMOTE_ADDR"]; // Вычисляем ip пользователя
                $brose=$_SERVER["HTTP_USER_AGENT"]; // Вычисляем браузер пользователя
                $to = "vladim-b@mail.ru"; // Ваш email адрес
                $subject = "Сообщение c сайта ves37.ru"; // тема письма
                $headers .= "Content-Type: text/html;
                ";
                $headers .= "Отправитель: Посетитель сайта"; // Отправитель письма
                $message = "
                Сообщение c сайта ves37.ru
                Имя: $name<br>
                Email: $email<br>
                Текст: $msg<br><br>
 
                IP отправителя: $ip<br>
                Браузер отправителя: $brose<br>
                ";
 
                $send = mail($to, $subject, $message, $headers);
                if ($send == "true")
                {
                        echo "Ваше сообщение отправлено. Мы ответим вам в ближайшее время.";
                }
                else
                {
                        echo "Не удалось отправить, попробуйте снова!";
                }
        }
}
 
?>
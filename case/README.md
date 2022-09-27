
Kurulum:

Repodan kodlar çekilerek sırası önce Flask dockerfile ayağa kaldırılır.


Taskta kullanılan API den yararlınarak (#https://docs.bitexen.com/?python) Basic ir web sitesi yapıldı.


flask kurulum 

````
docker build ./ --tag bitexen  
docker run --restart always -d --network=host --name bitexendeploy bitexen 

````


Web Girişi:
mail:bitexen_challenge@gmail.com
Password:bitexen



Flask klasörünün içinde Deploy edilmeye hazır SSL siz apache config dosyası mevcuttur
Veritabanı Mysql kullanıldı.
Veriler her 5 snde bir çekilerek analiz edilip bir önceki gelen data ile kıyaslanarak bir değişiklik durumunda veritanabına yazar

Her gece saat 12 de gelen son veri veritabanına yazılır.

Haftalık ve Aylık veriler Gelen Günlük verilerin analizi sonucu ortalaması alınıp veritabanına yazılır.


Kodun sonlarına doğru RESTAPI karşılayacak bizi :)

Günlük,HAftalık ve aylık verilerini 
(  /v1/bitexen/daily/  
 /v1/bitexen/<string:data>/<string:day>/  
)
çekebilirsiniz. 
 
<string:data> kısmında haftalık mı aylık mı olduğunu örneğin 
/v1/bitexen/month/<string:day>
/v1/bitexen/weekly/<string:day>

<string:day>  kısmı haftalık bir cevap istiyorsanız ise yılın hangi ayının hangi haftası olduğunu
örneğin
/v1/bitexen/month/2022-04-02
haftalık bir cevap istiyorsanız
örneğin
/v1/bitexen/month/2022-04

sorularıyla yanıt alabilirsiniz.

2022-04-02

2022 => yılı temsil eder
04   => ayı temsil eder 
02   => oayın kaçıncı haftası olduğunu temsil eder.

Birtane kullanıcı kayıt olması için post methodu vardır.

data ={

    "mail":"test@gmail.com",
    "name_surname":"test",
    "password":"test"

}


FASTAPI kurulum 

````
docker-compose -f system.yml -p system up --build -d

````
Kurulumdansonra  http://localhost:5000/dosc sayfasından FastAPI nin sunmuş olduğu döküman sayfasına gidebilirsiniz.

Her 5 sn de bitexen apisini dinleyen code yapısı mevcuttur.
Günü,Haftayıve Ayı Veritabanına analiz ederek kaydeder.

SQLAlchemy ile Mysql veritabanı bağlantııs yapıldı.


Günlük,HAftalık ve aylık verilerini 
(  /v1/bitexen/daily/  
 /v1/bitexen/<string:data>/<string:day>/  
)
çekebilirsiniz. 

<string:data> kısmında haftalık mı aylık mı olduğunu örneğin 
/v1/bitexen/month/<string:day>
/v1/bitexen/weekly/<string:day>

<string:day>  kısmı haftalık bir cevap istiyorsanız ise yılın hangi ayının hangi haftası olduğunu
örneğin
/v1/bitexen/month/2022-04-02
haftalık bir cevap istiyorsanız
örneğin
/v1/bitexen/month/2022-04

sorularıyla yanıt alabilirsiniz.

2022-04-02

2022 => yılı temsil eder
04   => ayı temsil eder 
02   => oayın kaçıncı haftası olduğunu temsil eder.

Birtane kullanıcı kayıt olması için post methodu vardır.

data ={
    "mail":"test@gmail.com",
    "name_surname':'test",
    "password":"test"
}

data verisini alarak veritanabına yeni kullanıcı ekler.

Unit-Test kod kısmı FastAPI klasörünün içinde unit-test.py dosyasıdır.

 

### There is jwt token and base auth token user login, register, logout example in the project. 
### The project is also an IMDB demo

## JWT Authentication vs Token-based Authentication
What is the difference between Django REST framework built-in token-based authentication and JSON Web Tokens or JWT authentication?

Django REST Framework built-in token-based authentication uses a database table to make associations between users and random tokens.

There is no way you can determine a user from the token itself since it's purely random unless you query the database.

JWT is JSON data encoded using a secret key so the server doesn't need to query a database. It can retrieve the associated user from the token itself.

As a result, it's more efficient and scales better than DRF's built-in token system.

### TURKCE

Django REST çerçevesi yerleşik belirteç tabanlı kimlik doğrulama ile JSON Web Belirteçleri veya JWT kimlik doğrulaması arasındaki fark nedir?

Django REST Framework yerleşik belirteç tabanlı kimlik doğrulama, kullanıcılar ve rastgele belirteçler arasında ilişki kurmak için bir veritabanı tablosu kullanır.

Veritabanını sorgulamadığınız sürece, tamamen rastgele olduğundan, belirtecin kendisinden bir kullanıcı belirlemenin bir yolu yoktur.

JWT, gizli bir anahtar kullanılarak kodlanmış JSON verileridir, böylece sunucunun bir veritabanını sorgulamasına gerek kalmaz. İlişkili kullanıcıyı belirtecin kendisinden alabilir.

Sonuç olarak, daha verimlidir ve DRF'nin yerleşik jeton sisteminden daha iyi ölçeklenir.

### 1. Admin Access
* Admin Section: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

### 2. Accounts
* Registration: [http://127.0.0.1:8000/account/register/](http://127.0.0.1:8000/account/register/)
* Login: [http://127.0.0.1:8000/account/login/](http://127.0.0.1:8000/account/login/)
* Logout [http://127.0.0.1:8000/account/logout/](http://127.0.0.1:8000/account/logout/)

### 3. Stream Platforms
* GET and POST [http://127.0.0.1:8000/watch/stream/](http://127.0.0.1:8000/watch/stream/)
* PUT and DESTROY [http://127.0.0.1:8000/watch/stream/<int:streamplatform_id>/](http://127.0.0.1:8000/watch/stream/<int:streamplatform_id>/)

### 4. Watch List
* POST and GET [http://127.0.0.1:8000/watch/stream/](http://127.0.0.1:8000/watch/stream/)
* PUT and DESTROY [http://127.0.0.1:8000/watch/stream/<int:movie_id>/](http://127.0.0.1:8000/watch/stream/<movie_id>/)

### 5. Reviews
* Create Review For Specific Movie [http://127.0.0.1:8000/watch/<int:movie_id>/review-create/](http://127.0.0.1:8000/watch/4/review-create/)
* List all Reviews [http://127.0.0.1:8000/watch/<int:movie_id>/reviews/](http://127.0.0.1:8000/watch/4/reviews/)
* PUT and DESTROY [http://127.0.0.1:8000/watch/review/<int:review_id>/](http://127.0.0.1:8000/watch/review/1/)
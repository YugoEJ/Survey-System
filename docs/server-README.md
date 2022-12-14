## Mahshava

### System users
* django admin user: `mahshavaadmin`/`4S4uC3rfUlOFS3crETs`
* mahshava admin dummy user: `dummy-mahshava-admin`/`mahshava@dmin123!`
* mahshava admin dummy user: `dummy-shcool-admin`/`shcooladmin123`

### DB
#### Dump data
```
python .\manage.py dumpdata --database=core auth.group auth.user auth.user_groups > core\fixtures\core.json

python -Xutf8 .\manage.py dumpdata core.contact core.processsteps core.school core.schoolprocess core.task core.surveysresults core.relationshipnetworks_survey core.leadershipandorganizationalculture_survey core.willingnesstochange_survey --database=core --indent 4 --format json -o core\fixtures\appData.json

### Setup mahshava env
* Client
  * Run `npm install` from `code/client/mahshava`
* Server
  * Install 3rd parties: `pip install -r requirements.txt`
  * Run DB scripts from `build/db`
  * Run migration: `python manage.py migrate --database=core`
  * Populate Users DB: `python manage.py loaddata core --database=core`
  * Populate Data DB: `python manage.py loaddata appData --database=core`
  * Copy `build/.env/.env.dev` to `code/server/src/mahshava` and rename it to `.env`

### Setup surveys env
* Client
  * Run `npm install` from `code/client/surveys`
* Server
  * Run migration: `python manage.py migrate --database=core`
  * Populate DB: `python manage.py loaddata surveys`

#### Important information
+ Super user: admin/Ad_123456


#### POSTGRES on UBUNTU
+ **Refs**:
    + https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04
    + [install pgAdmin4](https://askubuntu.com/questions/831262/how-to-install-pgadmin-4-in-desktop-mode-on-ubuntu)
  
+ **Installation**:
    ```
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    ```
+ **Access to the Postgres Prompt**: 
    ```
    sudo -u postgres psql
    postgres=# \q // to quit the postgres prompt
    ```
+ **Create new user**: 
    ```
    sudo -u postgres createuser --interactive
    // Output
    Enter name of role to add: admin
    Shall the new role be a superuser? (y/n) y
    sudo -u postgres psql
    postgres=# ALTER USER admin WITH ENCRYPTED PASSWORD 'AD_123456'; // set password for user 'admin'
    createdb -O admin icdpreddb; // create new database for user 'admin'
    ```

+ **Install pgAdmin4**:
    + Install dependencies and pgAdmin4
        ```
        sudo apt-get install virtualenv python3-pip libpq-dev python3-dev
        virtualenv -p python3 pgadmin4
        cd pgadmin4
        source bin/activate
        pip3 install https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v3.3/pip/pgadmin4-3.3-py2.py3-none-any.whl
        ```
    + Open: `config_local.py` with `nano lib/python3.6/site-packages/pgadmin4/config_local.py` and edit with the following text (press Ctrl + Shilf + X to save):
        ```
        import os
        DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
        LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
        SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
        SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
        STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
        SERVER_MODE = False
        ```
    + Run pgAdmin4: `python3 lib/python3.6/site-packages/pgadmin4/pgAdmin4.py`
    + Access at: `http://localhost:5050` and exit with `Ctrl + C`
    
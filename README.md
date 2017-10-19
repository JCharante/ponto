# ponto
The bridge betwen my IoT devices &amp; services


# Environment Variables

ponto only requires `ponto_dba`, but `runTests.sh` requires `ponto_test_dba`.

If you want to run the tests on the same database as your development one, then that's all right.

```
$ export ponto_dba="mysql+pymysql://root:root@localhost/ponto?charset=utf8mb4"
$ export ponto_test_dba="mysql+pymysql://root:root@localhost/ponto?charset=utf8mb4"
```

# Testing

We use pytest to run out tests.

Please run `./runTests.sh` to run all the tests.

This script will run pytest, but override the value of `ponto_dba` with `ponto_test_dba`.

This allows you to have both `ponto_dba` and `ponto_test_dba` exported, without having to switch between them.

If you wish to run a single script, then the following will work just as well.

```bash
ponto_dba="$ponto_test_dba" python tests/test_create_account.py
```
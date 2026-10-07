# -*- coding: utf-8 -*-
"""Выкладка site/ на хостинг по SFTP со сверкой контрольных сумм.
Пароль только из переменных окружения (SFTP_HOST, SFTP_USER, SFTP_PASS, SFTP_BASE).
config.php (токен Telegram) никогда не загружается и не удаляется — он живёт только на сервере."""
import hashlib
import os
import pathlib
import sys
import time

import paramiko

ROOT = pathlib.Path(__file__).parent


def need(name):
    v = os.environ.get(name)
    if not v:
        sys.exit(f"Не задана переменная окружения {name}")
    return v


def connect(host, user, pwd):
    for attempt in range(4):
        try:
            c = paramiko.SSHClient()
            c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            c.connect(host, 22, user, pwd, timeout=30, banner_timeout=60, auth_timeout=40, allow_agent=False, look_for_keys=False)
            return c
        except Exception as e:  # сервер хостинга иногда отвечает не сразу
            print(f"попытка {attempt + 1} не удалась: {str(e)[:70]}")
            time.sleep(8)
    sys.exit("SSH недоступен")


def main():
    host, user, pwd, base = need("SFTP_HOST"), need("SFTP_USER"), need("SFTP_PASS"), need("SFTP_BASE")
    site = ROOT / "site"
    files = [(f, f.relative_to(site).as_posix()) for f in sorted(site.rglob("*")) if f.is_file() and f.name != "config.php"]
    c = connect(host, user, pwd)
    s = c.open_sftp()
    made = set()
    for f, rel in files:
        path = base
        for part in rel.split("/")[:-1]:
            path += "/" + part
            if path not in made:
                try:
                    s.mkdir(path)
                except IOError:
                    pass
                made.add(path)
        s.put(str(f), f"{base}/{rel}")
    remote = {}
    for i in range(0, len(files), 40):
        chunk = files[i:i + 40]
        _, out, _ = c.exec_command(f"cd {base} && md5sum " + " ".join(f"'{r}'" for _, r in chunk))
        for line in out.read().decode().splitlines():
            h, n = line.split(None, 1)
            remote[n.strip()] = h
    bad = [rel for f, rel in files if remote.get(rel) != hashlib.md5(f.read_bytes()).hexdigest()]
    print(f"загружено файлов: {len(files)}, расхождений: {len(bad)}", bad)
    s.close()
    c.close()
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

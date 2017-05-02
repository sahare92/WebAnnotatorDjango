Before starting anything:
-	Set the default charset of mysql to be UNICODE by adding the following lines to /etc/mysql/my.cnf
		[mysqld]
		skip-character-set-client-handshake
		character_set_client=utf8mb4
		character_set_server=utf8mb4
-	Add to python.py after #!/usr/bin/env..
		# -*- coding: utf-8 -*-
-	And to every python file that uses utf-8 that line too.

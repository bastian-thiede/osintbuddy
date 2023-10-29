
import os

from casdoor import AsyncCasdoorSDK

certificate = '''-----BEGIN CERTIFICATE-----
MIIE2TCCAsGgAwIBAgIDAeJAMA0GCSqGSIb3DQEBCwUAMCYxDjAMBgNVBAoTBWFk
bWluMRQwEgYDVQQDDAtjZXJ0X3Q4MDVwdzAeFw0yMzEwMjgwNTAzMTNaFw00MzEw
MjgwNTAzMTNaMCYxDjAMBgNVBAoTBWFkbWluMRQwEgYDVQQDDAtjZXJ0X3Q4MDVw
dzCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALuJO1TnSbUua1DgA9rW
1iJSSSsZCcBcrUEe46DY9EZH63K7d4gJdrT4lOPr/5cRrp7YWJ3/F0DnPMDlC4RH
aU8T2UQLNbP0DIqZdO8Y1QBueiuBPLdxj3k8TSn1RL+7r3ACm4g2m0VVldMAXzaX
RRqmuRetBz4RdfwAq7NZFs/mYmoLF5iFoWoniaG26Rsntk5Fxo5L0fgqjMKf6oQo
7WQ/hdtxmqrWggabON2oUdoi+guB1kGlJky6FXHmFKqLNsPjaXfwqRLqGSAkowGl
vJJYLQvLN9JuYxqcyyDT/wE7FiuLU/CT3mH9QTBPhzHrsklXGYdZdoG0UGimcTUG
0wubHaGDsarYdC9vFGFywyEe41ZBHLZt7RhzO/Mu3jKrP7KK31MYXwZo4bsKmgj1
UwirO4YSbw9ODko8RLSyR3Om5t3/XNH3VSla8VnkzDriHicCOTKmAnf+XdNgRiBd
fFb8BQdrVZ/Ua+lOQl0QlOsqzCMP2tjqmdQ4z1kwAT7QggA+iE8GC5GvOxw4BA4p
h6kQHPOX66c7NspvC++UdpxTm9NJxITU6ZMcAS9ZwSd8bk/jkMrHbjLggH1FIm6T
oJ7FYm/v31ZxXjr/TiM66lMHAfwmxoxirbOsu66IMWHCNbIMxYySmTNLE9vGSN9F
+x4PbBxyZtFfgtUZmoWrKNY9AgMBAAGjEDAOMAwGA1UdEwEB/wQCMAAwDQYJKoZI
hvcNAQELBQADggIBALt9bWjQgstTLcQSMUIRacKZ0/bP6OD6d4pk2WPYjrYJHWfp
BoRN7zW/zu7ztr4SpGD/CwC4Nib/vplcMDXNi2xDxK6sAOcwzSUD5IaAZpoFdluT
cYAXJ75ezXRhycl+aI2/R0effQiUDXp+9FmT6ENQ2NAw6JL29ih+ugDXh1/JJ+oV
gnZYEk47vyJLxOOCGNww4u75iRMC73DBO2rHkwXfR9IQxx1bPK+8CwqtO7ZQKV8v
THxlcrEbMWDRLOLrIuAOUwVOq725dLscFXPJuMbCNUjgsxFCL+MA5yFot8nf4DTW
yHfnd+lio0g83c6Xb3QaJtW5NJvIeeZ7Q66fh24kM7XiZZs1kzNYT2wTWTrJGyvm
6fT8SM5hy6xuoGmzEj6SiKiQHSzjd/gv4K2Wv3F4I+Zigxvx8LCHT3ETH18xPOB6
IJyOJjUDGY3o/T8DhVj0Fw5NHa/ujjx893rcdiYdiQnWZ9oBwDtlHDDtdEaGKrAr
OvJDjhG2J2X5IbXWc5fuTVoxhnjSuT/x2+3IBuWETKvjbno9/fTcUl9o2Y0ejTvf
iKFQ3TJfwBi51Pd3skzEJCE/C5Vzw03YrwO2Clx9iZRAv+drNn/vM++ch9+Ph3jQ
tyCMlYmLO/0DCB/PgEjqQyScFRH8mcMU2DYM5Z+PThlUvTtTMrXlZcIShcgi
-----END CERTIFICATE-----'''

class Config:
    CASDOOR_SDK = AsyncCasdoorSDK(
        endpoint='http://casdoor:8080',
        client_id='057e00c722b1f415196b',
        client_secret='17e86c4cd14e97ea968e3a08c9c8efcb8fdebf02',
        certificate=certificate,
        org_name='org_ob',
        application_name='application_ob',
    )
    REDIRECT_URI = 'http://localhost:3000/callback'
    SECRET_TYPE = 'filesystem'
    SECRET_KEY = os.urandom(24)
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Connector(ABC):
    host: str = "localhost"
    user: str = "ADMIN"
    password: str = "admin@123"
    db: str = "PUBLIC"


@dataclass
class PostgreSql(Connector):
    port: str = "5432"
    table: str = "default"

    def test(self):
        print(
            f"connection to oracle-db with host {self.host}, port {self.port}, user {self.user},"
            f"password {self.password},db {self.db}, table {self.table}"
        )


class OracleDb(Connector):
    def __init__(
        self,
        host: str = "localhost",
        user: str = "ADMIN",
        password: str = "admin@123",
        db: str = "PUBLIC",
        port: str = "1439",
        table: str = "temp",
    ):
        self.port = port
        self.table = table
        super().__init__(host=host, user=user, password=password, db=db)

    def test(self):
        print(
            f"connection to oracle-db with host {self.host}, port {self.port}, user {self.user},"
            f"password {self.password},db {self.db}, table {self.table}"
        )


class Connection:
    def __init__(self, connector: Connector) -> None:
        self.connector = connector

    def test_connection(self):
        self.connector.test()


def main():
    oracle_db = OracleDb(host="oracledb://", port="4559", table="oracle_default")
    postgres_connection = Connection(PostgreSql())
    oracle_connection = Connection(oracle_db)
    postgres_connection.test_connection()
    oracle_connection.test_connection()


if __name__ == "__main__":
    main()

import psycopg2 as pg

tdx_tickers="""CREATE TABLE IF NOT EXISTS tdx_tickers (
  ticker TEXT PRIMARY KEY,
  name TEXT,
  market SMALLINT
);
"""

tdx_klines="""CREATE TABLE IF NOT EXISTS tdx_klines (
  time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
  ticker TEXT,
  open NUMERIC,
  high NUMERIC,
  low NUMERIC,
  close NUMERIC,
  close_adj NUMERIC,
  volume NUMERIC,
  amount NUMERIC,
  FOREIGN KEY (ticker) REFERENCES tdx_tickers (ticker)
);
"""

mydata_tickers="""CREATE TABLE IF NOT EXISTS mydata_tickers (
  ticker TEXT PRIMARY KEY,
  name TEXT,
  exchange TEXT
);
"""

mydata_klines="""CREATE TABLE IF NOT EXISTS mydata_klines (
  time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
  ticker TEXT,
  open NUMERIC,
  high NUMERIC,
  low NUMERIC,
  close NUMERIC,
  close_adj NUMERIC,
  volume NUMERIC,
  amount NUMERIC,
  FOREIGN KEY (ticker) REFERENCES mydata_tickers (ticker)
);
"""

yf_tickers="""CREATE TABLE IF NOT EXISTS yf_tickers (
  ticker TEXT PRIMARY KEY,
  name TEXT,
  industry TEXT
);
"""

yf_klines="""CREATE TABLE IF NOT EXISTS yf_klines (
  time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
  ticker TEXT,
  open NUMERIC,
  high NUMERIC,
  low NUMERIC,
  close NUMERIC,
  close_adj NUMERIC,
  volume NUMERIC,
  FOREIGN KEY (ticker) REFERENCES yf_tickers (ticker)
);
"""

fmp_tickers="""CREATE TABLE IF NOT EXISTS fmp_tickers (
  ticker TEXT PRIMARY KEY,
  name TEXT,
  exchange_long TEXT,
  exchange TEXT
);
"""

fmp_klines="""CREATE TABLE IF NOT EXISTS fmp_klines (
  time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
  ticker TEXT,
  open NUMERIC,
  high NUMERIC,
  low NUMERIC,
  close NUMERIC,
  close_adj NUMERIC,
  volume NUMERIC,
  FOREIGN KEY (ticker) REFERENCES fmp_tickers (ticker)
);
"""

def create_table(connection:str,sql:str)->None:
    with pg.connect(connection) as conn:
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()

def create_tdx_tables(connection:str)->None:
    create_table(connection,tdx_tickers)
    create_table(connection,tdx_klines)

def create_mydata_tables(connection:str)->None:
    create_table(connection,mydata_tickers)
    create_table(connection,mydata_klines)

def create_yf_tables(connection:str)->None:
    create_table(connection,yf_tickers)
    create_table(connection,yf_klines)

def create_fmp_tables(connection:str)->None:
    create_table(connection,fmp_tickers)
    create_table(connection,fmp_klines)
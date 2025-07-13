CREATE DATABASE IF NOT EXISTS indian_stocks;

USE indian_stocks;

CREATE TABLE IF NOT EXISTS stocks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ticker VARCHAR(10),
  trade_date DATE,
  open_price FLOAT,
  high_price FLOAT,
  low_price FLOAT,
  close_price FLOAT,
  volume BIGINT
);a

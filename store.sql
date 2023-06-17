-- Adminer 4.8.1 MySQL 10.11.3-MariaDB dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS `store`;
CREATE DATABASE `store` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `store`;

DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` varchar(32) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL DEFAULT 0,
  `created` date NOT NULL DEFAULT current_timestamp(),
  `updated` date NOT NULL DEFAULT current_timestamp(),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

TRUNCATE `product`;
INSERT INTO `product` (`id`, `name`, `price`, `quantity`, `created`, `updated`) VALUES
('bO86N9xVuMssdkOF',	'Burger King',	20000,	3,	'2023-06-18',	'2023-06-14'),
('h6IEr6oum1P0swzs',	'Roti Isi Patty',	32000,	21,	'2023-06-11',	'2023-06-17'),
('JVaoL9a2liULjV4X',	'Sayur Bayam',	15000,	99999,	'2023-06-18',	'2023-06-14'),
('lN7yotSHHD5RbBMZ',	'Martabrak',	5000,	46,	'2023-06-18',	'2023-06-14'),
('zpa5q7ZAc5vqO0Zj',	'Sayur Asem',	16000,	99999,	'2023-06-18',	'2023-06-14');

-- 2023-06-17 22:41:15

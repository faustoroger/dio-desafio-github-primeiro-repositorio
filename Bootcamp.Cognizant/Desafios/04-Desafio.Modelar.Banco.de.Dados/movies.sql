-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: mysql-server
-- Tempo de geração: 15-Maio-2022 às 18:38
-- Versão do servidor: 8.0.28
-- versão do PHP: 8.0.15

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `movies-control`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `movies`
--

CREATE TABLE `movies` (
  `id` int NOT NULL,
  `type` int NOT NULL,
  `name` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `total_ep` int DEFAULT NULL,
  `atual_ep` int DEFAULT NULL,
  `last_view` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `movies`
--

INSERT INTO `movies` (`id`, `type`, `name`, `total_ep`, `atual_ep`, `last_view`) VALUES
(1, 0, 'Friends', 11, 1, '2021-05-15 19:25:17'),
(2, 1, 'Avengers', NULL, NULL, '2021-05-15 16:25:17'),
(3, 0, 'Todo mundo odeia o Chris', 20, 1, '2021-02-23 13:20:37'),
(5, 1, '300', NULL, NULL, '2022-05-15 22:02:09'),
(6, 1, '1917', NULL, NULL, '2022-05-15 17:08:56');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `movies`
--
ALTER TABLE `movies`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
SET FOREIGN_KEY_CHECKS=1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3316
-- Время создания: Мар 19 2023 г., 19:14
-- Версия сервера: 5.7.23
-- Версия PHP: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `vocabulary`
--

-- --------------------------------------------------------

--
-- Структура таблицы `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `bname` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `books`
--

INSERT INTO `books` (`id`, `bname`) VALUES
(1, 'Первый'),
(2, 'Десерты'),
(3, 'ппп'),
(4, 'fhfhfh'),
(5, 'ffhfh'),
(6, 'rtgrfghgv'),
(7, 'cdfghvbc');

-- --------------------------------------------------------

--
-- Структура таблицы `terms`
--

CREATE TABLE `terms` (
  `idterms` int(11) NOT NULL,
  `idbook` int(11) DEFAULT NULL,
  `name` text,
  `translate` text,
  `opisanie` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `terms`
--

INSERT INTO `terms` (`idterms`, `idbook`, `name`, `translate`, `opisanie`) VALUES
(1, 2, 'Cake', 'Тортик', 'вктвот сааьвы'),
(2, 1, 'пргнрпг', 'аув ы', 'укавс'),
(3, 1, 'ffff', 'dfghj', 'fgbhnm'),
(4, 1, 'ggg', 'ggg', 'ggg'),
(5, 1, 'jhgh', 'kjk', 'kjjk'),
(6, 1, 'kj', 'ghj', 'lkjbh'),
(7, 1, 'jjjj', 'jjj', 'jjj'),
(8, 1, 'jjj', 'jjj', 'jj'),
(9, 1, 'hh', 'hh', 'hh'),
(10, 1, 'skin', 'кожа', 'ММЫВ'),
(11, 1, 'Ass', 'ЗАДНИЦА', 'ПУПНГАГВ'),
(12, 1, 'H', 'H', 'H');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `terms`
--
ALTER TABLE `terms`
  ADD PRIMARY KEY (`idterms`),
  ADD KEY `idbook` (`idbook`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `terms`
--
ALTER TABLE `terms`
  MODIFY `idterms` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

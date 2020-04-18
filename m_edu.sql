-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- 主機: localhost:3306
-- 產生時間： 2020 年 04 月 18 日 17:03
-- 伺服器版本: 5.7.29-0ubuntu0.18.04.1
-- PHP 版本： 7.2.24-0ubuntu0.18.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `m_edu`
--

-- --------------------------------------------------------

--
-- 資料表結構 `admin`
--

CREATE TABLE `admin` (
  `username` varchar(50) CHARACTER SET utf8 NOT NULL,
  `password` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('stephanie', 123),
('mandy', 789),
('sandy', 111),
('peter', 111);

-- --------------------------------------------------------

--
-- 資料表結構 `materials`
--

CREATE TABLE `materials` (
  `ex_id` int(11) NOT NULL,
  `classname` varchar(50) NOT NULL,
  `grade` varchar(50) NOT NULL,
  `eximage` text NOT NULL,
  `ex` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `materials`
--

INSERT INTO `materials` (`ex_id`, `classname`, `grade`, `eximage`, `ex`) VALUES
(1, 'Online learning', 'K.2', 'kexbook01.png', 'freetrial_ex_k2.pdf'),
(2, 'Online learning', 'K.3', 'kexbook02.png', 'freetrial_ex_k3.pdf');

-- --------------------------------------------------------

--
-- 資料表結構 `reservation`
--

CREATE TABLE `reservation` (
  `reserve_no` int(11) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `school` varchar(255) NOT NULL,
  `grade` varchar(255) NOT NULL,
  `birth` varchar(255) NOT NULL,
  `tel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `reservation`
--

INSERT INTO `reservation` (`reserve_no`, `firstname`, `lastname`, `school`, `grade`, `birth`, `tel`) VALUES
(1, 'Tai Man', 'Chan', 'ABC Primary School', 'P.4', '03-04-2010', 987654321),
(2, 'Mandy', 'Lam', '123 Primary School', 'P.3', '18-01-2012', 912345678),
(3, 'Henry', 'Lam', '123 Primary School', 'P.1', '20-5-2014', 912345678),
(4, 'Siu Man', 'Wong', 'Z Primary School', 'P.6', '30-7-2008', 678912345),
(5, 'Yee Ching', 'Fan', 'Z Primary School', 'P.2', '23-2-2013', 934567891);

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `stname` varchar(50) CHARACTER SET utf8 NOT NULL,
  `password` int(11) NOT NULL,
  `tel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `user`
--

INSERT INTO `user` (`stname`, `password`, `tel`) VALUES
('Chan Tai Man', 123, 987654321),
('Lee Tai Man', 789, 987654321),
('Wu Tai Man', 111, 912345678),
('Chan Man', 111, 987654321),
('Fan Yee Ching', 888, 912345678),
('Sandy Lee', 0, 96789123),
('Candy', 0, 123456789);

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `materials`
--
ALTER TABLE `materials`
  ADD PRIMARY KEY (`ex_id`);

--
-- 資料表索引 `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`reserve_no`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `materials`
--
ALTER TABLE `materials`
  MODIFY `ex_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- 使用資料表 AUTO_INCREMENT `reservation`
--
ALTER TABLE `reservation`
  MODIFY `reserve_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

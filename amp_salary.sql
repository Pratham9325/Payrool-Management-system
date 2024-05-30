-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 30, 2024 at 01:44 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `EMS`
--

-- --------------------------------------------------------

--
-- Table structure for table `amp_salary`
--

CREATE TABLE `amp_salary` (
  `e_id` int(11) NOT NULL,
  `designation` text NOT NULL,
  `name` text NOT NULL,
  `age` text NOT NULL,
  `gender` text NOT NULL,
  `email` text NOT NULL,
  `hr_location` text NOT NULL,
  `dog` text NOT NULL,
  `dob` text NOT NULL,
  `experience` text NOT NULL,
  `proof_id` text NOT NULL,
  `contact` text NOT NULL,
  `status` text NOT NULL,
  `address` text NOT NULL,
  `month` text NOT NULL,
  `year` text NOT NULL,
  `basic_salary` text NOT NULL,
  `t_days` text NOT NULL,
  `absent_days` text NOT NULL,
  `medical` text NOT NULL,
  `convenient` text NOT NULL,
  `net_salary` text NOT NULL,
  `pf` text NOT NULL,
  `salary_receipt` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `amp_salary`
--

INSERT INTO `amp_salary` (`e_id`, `designation`, `name`, `age`, `gender`, `email`, `hr_location`, `dog`, `dob`, `experience`, `proof_id`, `contact`, `status`, `address`, `month`, `year`, `basic_salary`, `t_days`, `absent_days`, `medical`, `convenient`, `net_salary`, `pf`, `salary_receipt`) VALUES
(3, 'HJBVCG', 'JHBVGC', 'VCFX', '', 'HBJGVCFG', 'BVBCX', ' BV', 'JBHV', 'M NBV', 'BHVCG', 'JKHBVGCF', 'HBJGVHFC', 'HGFDS\n', 'DES', '30098', '645789', '31', '9', '800', '900', '663325.3', '4000', '3.txt'),
(7, '', '', '', 'Male', '', '', '', '', '', '', '', '', '\n', 'Dec', '2023', '8000', '31', '1', '300', '800', '3336.67', '4000', '7.txt'),
(12, '', '', '', 'Select', '', '', '', '', '', '', '', '', '\n', 'des', '2038', '874658726', '31', '7', '500', '100', '903813250.2', '400', '12.txt'),
(678, 'supervisor', 'mukeshbkankhare', '12', 'male', 'abcd123@gmail.com', 'jal', 'sady', '872382', 'ntg', 'adhar', '98736373838', 'busy', 'jalgaon 	\n', 'dec', '2003', '180000', '31', '4', '80', '340', '184596.0', '1200', '678.txt');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `amp_salary`
--
ALTER TABLE `amp_salary`
  ADD PRIMARY KEY (`e_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `amp_salary`
--
ALTER TABLE `amp_salary`
  MODIFY `e_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=679;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 25, 2025 at 04:15 AM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `findmystudio`
CREATE DATABASE findmystudio;

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_category`
--

DROP TABLE IF EXISTS `adminapp_tbl_category`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_category` (
  `categoryid` int(11) NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(25) NOT NULL,
  `categoryimage` varchar(100) NOT NULL,
  PRIMARY KEY (`categoryid`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_category`
--

INSERT INTO `adminapp_tbl_category` (`categoryid`, `categoryname`, `categoryimage`) VALUES
(1, 'Wedding', '6_m7BeQYm.jpeg'),
(4, 'Event & Party', 'Event__Party_ctzNZ4s.jpg'),
(5, 'Fashion & Modeling ', 'modeling.jpg'),
(6, 'Baby & Maternity', 'Baby__Maternity.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_district`
--

DROP TABLE IF EXISTS `adminapp_tbl_district`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_district` (
  `districtid` int(11) NOT NULL AUTO_INCREMENT,
  `districtname` varchar(25) NOT NULL,
  PRIMARY KEY (`districtid`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_district`
--

INSERT INTO `adminapp_tbl_district` (`districtid`, `districtname`) VALUES
(17, 'Ernakulam'),
(2, 'Kollam'),
(3, 'Idukki'),
(5, 'Kottayam'),
(11, 'Thiruvananthapuram'),
(7, 'Malappuram'),
(8, 'Wayanad'),
(9, 'Kozhikode'),
(10, 'Palakkadu'),
(12, 'Pathanamthitta'),
(13, 'Thrissur'),
(14, 'Kannur');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_location`
--

DROP TABLE IF EXISTS `adminapp_tbl_location`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_location` (
  `locationid` int(11) NOT NULL AUTO_INCREMENT,
  `locationname` varchar(25) NOT NULL,
  `districtid_id` int(11) NOT NULL,
  PRIMARY KEY (`locationid`),
  KEY `Adminapp_tbl_location_districtid_id_3bf5a552` (`districtid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_location`
--

INSERT INTO `adminapp_tbl_location` (`locationid`, `locationname`, `districtid_id`) VALUES
(23, 'Muvatupuzha', 17),
(10, 'Thodupuzha', 3),
(3, 'Adimali', 3),
(22, 'Aluva', 17),
(6, 'Pala', 5),
(7, 'Kanjirappaly', 5),
(24, 'Mananthavady', 8),
(21, 'Edapp', 17),
(11, 'Kattapana', 3),
(12, 'Adichanalloor', 2),
(13, 'Karunagappally', 2),
(14, 'Elampalloor', 2),
(15, 'Neyyattinkara', 11),
(16, 'Kattakada', 11),
(17, 'Varkala', 11),
(18, 'Tirur', 7),
(19, 'Manjeri', 7),
(20, 'Kottakkal', 7);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=77 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tbl_login', 7, 'add_tbl_login'),
(26, 'Can change tbl_login', 7, 'change_tbl_login'),
(27, 'Can delete tbl_login', 7, 'delete_tbl_login'),
(28, 'Can view tbl_login', 7, 'view_tbl_login'),
(29, 'Can add tbl_district', 8, 'add_tbl_district'),
(30, 'Can change tbl_district', 8, 'change_tbl_district'),
(31, 'Can delete tbl_district', 8, 'delete_tbl_district'),
(32, 'Can view tbl_district', 8, 'view_tbl_district'),
(33, 'Can add tbl_location', 9, 'add_tbl_location'),
(34, 'Can change tbl_location', 9, 'change_tbl_location'),
(35, 'Can delete tbl_location', 9, 'delete_tbl_location'),
(36, 'Can view tbl_location', 9, 'view_tbl_location'),
(37, 'Can add tbl_category', 10, 'add_tbl_category'),
(38, 'Can change tbl_category', 10, 'change_tbl_category'),
(39, 'Can delete tbl_category', 10, 'delete_tbl_category'),
(40, 'Can view tbl_category', 10, 'view_tbl_category'),
(41, 'Can add tbl_studio', 11, 'add_tbl_studio'),
(42, 'Can change tbl_studio', 11, 'change_tbl_studio'),
(43, 'Can delete tbl_studio', 11, 'delete_tbl_studio'),
(44, 'Can view tbl_studio', 11, 'view_tbl_studio'),
(45, 'Can add tbl_customer', 12, 'add_tbl_customer'),
(46, 'Can change tbl_customer', 12, 'change_tbl_customer'),
(47, 'Can delete tbl_customer', 12, 'delete_tbl_customer'),
(48, 'Can view tbl_customer', 12, 'view_tbl_customer'),
(49, 'Can add tbl_work', 13, 'add_tbl_work'),
(50, 'Can change tbl_work', 13, 'change_tbl_work'),
(51, 'Can delete tbl_work', 13, 'delete_tbl_work'),
(52, 'Can view tbl_work', 13, 'view_tbl_work'),
(53, 'Can add tbl_workimage', 14, 'add_tbl_workimage'),
(54, 'Can change tbl_workimage', 14, 'change_tbl_workimage'),
(55, 'Can delete tbl_workimage', 14, 'delete_tbl_workimage'),
(56, 'Can view tbl_workimage', 14, 'view_tbl_workimage'),
(57, 'Can add tbl_package', 15, 'add_tbl_package'),
(58, 'Can change tbl_package', 15, 'change_tbl_package'),
(59, 'Can delete tbl_package', 15, 'delete_tbl_package'),
(60, 'Can view tbl_package', 15, 'view_tbl_package'),
(61, 'Can add tbl_request', 16, 'add_tbl_request'),
(62, 'Can change tbl_request', 16, 'change_tbl_request'),
(63, 'Can delete tbl_request', 16, 'delete_tbl_request'),
(64, 'Can view tbl_request', 16, 'view_tbl_request'),
(65, 'Can add tbl_payment', 17, 'add_tbl_payment'),
(66, 'Can change tbl_payment', 17, 'change_tbl_payment'),
(67, 'Can delete tbl_payment', 17, 'delete_tbl_payment'),
(68, 'Can view tbl_payment', 17, 'view_tbl_payment'),
(69, 'Can add feedback', 18, 'add_feedback'),
(70, 'Can change feedback', 18, 'change_feedback'),
(71, 'Can delete feedback', 18, 'delete_feedback'),
(72, 'Can view feedback', 18, 'view_feedback'),
(73, 'Can add tbl_feedback', 18, 'add_tbl_feedback'),
(74, 'Can change tbl_feedback', 18, 'change_tbl_feedback'),
(75, 'Can delete tbl_feedback', 18, 'delete_tbl_feedback'),
(76, 'Can view tbl_feedback', 18, 'view_tbl_feedback');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `customerapp_tbl_feedback`
--

DROP TABLE IF EXISTS `customerapp_tbl_feedback`;
CREATE TABLE IF NOT EXISTS `customerapp_tbl_feedback` (
  `feedbackid` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) NOT NULL,
  `rating` int(11) NOT NULL,
  `customerid_id` int(11) NOT NULL,
  `packageid_id` int(11) NOT NULL,
  PRIMARY KEY (`feedbackid`),
  KEY `Customerapp_feedback_customerid_id_27e394da` (`customerid_id`),
  KEY `Customerapp_feedback_packageid_id_e2c0ea05` (`packageid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customerapp_tbl_feedback`
--

INSERT INTO `customerapp_tbl_feedback` (`feedbackid`, `description`, `rating`, `customerid_id`, `packageid_id`) VALUES
(1, 'Good', 4, 5, 7),
(3, 'Excellent', 5, 5, 7),
(4, 'good', 4, 5, 7);

-- --------------------------------------------------------

--
-- Table structure for table `customerapp_tbl_payment`
--

DROP TABLE IF EXISTS `customerapp_tbl_payment`;
CREATE TABLE IF NOT EXISTS `customerapp_tbl_payment` (
  `paymentid` int(11) NOT NULL AUTO_INCREMENT,
  `iamount` decimal(8,2) NOT NULL,
  `tamount` decimal(8,2) NOT NULL,
  `status` varchar(25) NOT NULL,
  `paymentdate` date NOT NULL,
  `requestid_id` int(11) NOT NULL,
  `camount` decimal(8,2) NOT NULL,
  PRIMARY KEY (`paymentid`),
  KEY `Customerapp_tbl_payment_requestid_id_7c404abc` (`requestid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customerapp_tbl_payment`
--

INSERT INTO `customerapp_tbl_payment` (`paymentid`, `iamount`, `tamount`, `status`, `paymentdate`, `requestid_id`, `camount`) VALUES
(5, '50000.00', '100000.00', 'Paid', '2025-03-05', 6, '5000.00'),
(4, '50000.00', '100000.00', 'Paid', '2025-03-04', 5, '5000.00'),
(6, '50000.00', '100000.00', 'Paid', '2025-03-05', 7, '5000.00'),
(7, '50000.00', '100000.00', 'Paid', '2025-03-12', 8, '5000.00'),
(9, '50500.00', '101000.00', 'Paid', '2025-03-14', 11, '5050.00'),
(10, '32500.00', '65000.00', 'Paid', '2025-03-21', 13, '3250.00'),
(11, '5000.00', '10000.00', 'Paid', '2025-03-24', 16, '500.00'),
(12, '5000.00', '10000.00', 'Paid', '2025-03-24', 15, '500.00'),
(13, '5000.00', '10000.00', 'Paid', '2025-03-24', 17, '500.00');

-- --------------------------------------------------------

--
-- Table structure for table `customerapp_tbl_request`
--

DROP TABLE IF EXISTS `customerapp_tbl_request`;
CREATE TABLE IF NOT EXISTS `customerapp_tbl_request` (
  `requestid` int(11) NOT NULL AUTO_INCREMENT,
  `requireddate` date NOT NULL,
  `noofdays` bigint(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  `status` varchar(25) NOT NULL,
  `remark` varchar(100) NOT NULL,
  `customerid_id` int(11) NOT NULL,
  `packageid_id` int(11) NOT NULL,
  `aamount` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`requestid`),
  KEY `Customerapp_tbl_request_customerid_id_b641bfaa` (`customerid_id`),
  KEY `Customerapp_tbl_request_packageid_id_b4b04bd1` (`packageid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customerapp_tbl_request`
--

INSERT INTO `customerapp_tbl_request` (`requestid`, `requireddate`, `noofdays`, `description`, `status`, `remark`, `customerid_id`, `packageid_id`, `aamount`) VALUES
(15, '2025-03-25', 1, 'dteytrth', 'Paid', '', 5, 7, '0.00'),
(14, '2025-03-25', 1, 'shoot', 'Booked', '', 6, 8, NULL),
(13, '2025-03-22', 2, '22-03-2025:Wedding\r\n24_03-2025:Reception', 'Paid', '', 5, 6, '5000.00'),
(11, '2025-03-20', 3, '20/03/2025- Pre wedding shoot, 22/03/2025-Wedding, 24/03/2025-Post wedding shoot', 'Paid', '', 5, 4, '1000.00'),
(12, '2025-03-15', 3, 'bjhbhj', 'Booked', '', 5, 4, NULL),
(16, '2025-03-28', 2, 'fguh', 'Paid', '', 5, 7, '0.00'),
(17, '2025-03-26', 1, 'dvauda', 'Paid', '', 5, 7, '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'Guestapp', 'tbl_login'),
(8, 'Adminapp', 'tbl_district'),
(9, 'Adminapp', 'tbl_location'),
(10, 'Adminapp', 'tbl_category'),
(11, 'Guestapp', 'tbl_studio'),
(12, 'Guestapp', 'tbl_customer'),
(13, 'Studioapp', 'tbl_work'),
(14, 'Studioapp', 'tbl_workimage'),
(15, 'Studioapp', 'tbl_package'),
(16, 'Customerapp', 'tbl_request'),
(17, 'Customerapp', 'tbl_payment'),
(18, 'Customerapp', 'tbl_feedback');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Guestapp', '0001_initial', '2025-01-08 08:46:21.205410'),
(2, 'contenttypes', '0001_initial', '2025-01-08 08:46:21.237334'),
(3, 'auth', '0001_initial', '2025-01-08 08:46:21.381661'),
(4, 'admin', '0001_initial', '2025-01-08 08:46:21.422441'),
(5, 'admin', '0002_logentry_remove_auto_add', '2025-01-08 08:46:21.431333'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2025-01-08 08:46:21.442089'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-01-08 08:46:21.470672'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-01-08 08:46:21.491542'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-01-08 08:46:21.507787'),
(10, 'auth', '0004_alter_user_username_opts', '2025-01-08 08:46:21.516154'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-01-08 08:46:21.531124'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-01-08 08:46:21.537730'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-01-08 08:46:21.546297'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-01-08 08:46:21.561326'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-01-08 08:46:21.577930'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-01-08 08:46:21.592832'),
(17, 'auth', '0011_update_proxy_permissions', '2025-01-08 08:46:21.601840'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-01-08 08:46:21.617362'),
(19, 'sessions', '0001_initial', '2025-01-08 08:46:21.634624'),
(20, 'Guestapp', '0002_tbl_login_status', '2025-01-08 08:49:44.309539'),
(21, 'Adminapp', '0001_initial', '2025-01-08 10:29:01.753733'),
(22, 'Adminapp', '0002_tbl_location', '2025-01-13 04:38:27.300612'),
(23, 'Adminapp', '0003_tbl_category', '2025-01-13 05:55:08.820907'),
(24, 'Guestapp', '0003_tbl_studio', '2025-01-24 04:52:49.625940'),
(25, 'Guestapp', '0004_tbl_customer', '2025-01-24 06:43:31.702373'),
(26, 'Guestapp', '0005_rename_customrname_tbl_customer_customername', '2025-01-24 07:17:47.857057'),
(27, 'Studioapp', '0001_initial', '2025-01-29 10:15:03.909035'),
(28, 'Studioapp', '0002_tbl_workimage', '2025-01-29 17:21:10.343247'),
(29, 'Studioapp', '0003_rename_image_tbl_workimage_image1_and_more', '2025-01-30 08:35:31.557352'),
(30, 'Studioapp', '0004_tbl_work_studioid', '2025-01-30 09:26:43.965928'),
(31, 'Studioapp', '0005_tbl_package', '2025-01-31 08:47:22.284255'),
(32, 'Studioapp', '0006_alter_tbl_package_amount', '2025-01-31 09:04:47.351303'),
(33, 'Guestapp', '0006_tbl_studio_simage', '2025-02-03 05:08:22.133923'),
(34, 'Customerapp', '0001_initial', '2025-02-13 09:41:57.693550'),
(35, 'Customerapp', '0002_tbl_payment', '2025-02-18 10:17:04.000971'),
(36, 'Customerapp', '0003_tbl_payment_camount_alter_tbl_request_noofdays', '2025-02-19 05:20:55.202325'),
(37, 'Customerapp', '0004_tbl_request_aamount', '2025-03-13 08:24:30.739634'),
(38, 'Studioapp', '0007_tbl_work_workimg', '2025-03-13 08:43:36.586652'),
(39, 'Customerapp', '0005_feedback', '2025-03-24 06:30:45.038519'),
(40, 'Customerapp', '0006_rename_feedback_tbl_feedback', '2025-03-24 06:32:58.746980');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('088ggfxc7llu6w7u6ovw4dlxbon2v99l', 'eyJsb2dpbmlkIjoxMH0:1tfxdR:uwm_50vEfy4lKf4lCu3CCCA3Yo-v18BQ4tYaS4jkJN0', '2025-02-20 08:53:21.173328'),
('fu1reugc5b7h5lyb4k6rlgtndvcfsc4e', 'eyJsb2dpbmlkIjoyNH0:1twcc3:Njf8AOh4JxiMPX8JU0qbkMQVjF3Yw8C4Eh8OpZrSOs8', '2025-04-07 07:52:47.847391');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_customer`
--

DROP TABLE IF EXISTS `guestapp_tbl_customer`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_customer` (
  `customerid` int(11) NOT NULL AUTO_INCREMENT,
  `customername` varchar(25) NOT NULL,
  `address` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `pincode` bigint(20) NOT NULL,
  `regdate` date NOT NULL,
  `locationid_id` int(11) NOT NULL,
  `loginid_id` int(11) NOT NULL,
  PRIMARY KEY (`customerid`),
  KEY `Guestapp_tbl_customer_locationid_id_8bc86094` (`locationid_id`),
  KEY `Guestapp_tbl_customer_loginid_id_3521d725` (`loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_customer`
--

INSERT INTO `guestapp_tbl_customer` (`customerid`, `customername`, `address`, `email`, `phone`, `pincode`, `regdate`, `locationid_id`, `loginid_id`) VALUES
(6, 'Anna', 'Urumpil(H)', 'annaroy823@gmail.com', 8590322756, 686513, '2025-03-12', 7, 27),
(5, 'Jaiden gill Jose', 'Nedumkallel (H)', 'jaidengillj@gmail.com', 6238831069, 686671, '2025-03-04', 10, 24);

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_login`
--

DROP TABLE IF EXISTS `guestapp_tbl_login`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `role` varchar(25) NOT NULL,
  `status` varchar(25) NOT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_login`
--

INSERT INTO `guestapp_tbl_login` (`loginid`, `username`, `password`, `role`, `status`) VALUES
(1, 'admin', 'admin', 'admin', 'conformed '),
(26, 'insight', 'insight', 'studio', 'Accepted'),
(27, 'anna', 'anna', 'customer', 'confirmed'),
(25, 'moments', 'moments', 'studio', 'Accepted'),
(24, 'jaidengill', 'jaidengill', 'customer', 'confirmed'),
(22, 'framehunt', 'framehunt', 'studio', 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_studio`
--

DROP TABLE IF EXISTS `guestapp_tbl_studio`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_studio` (
  `studioid` int(11) NOT NULL AUTO_INCREMENT,
  `studioname` varchar(25) NOT NULL,
  `address` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `landmark` varchar(25) NOT NULL,
  `idproof` varchar(100) NOT NULL,
  `pincode` bigint(20) NOT NULL,
  `regdate` date NOT NULL,
  `locationid_id` int(11) NOT NULL,
  `loginid_id` int(11) NOT NULL,
  `simage` varchar(100) NOT NULL,
  PRIMARY KEY (`studioid`),
  KEY `Guestapp_tbl_studio_locationid_id_cd55f9c1` (`locationid_id`),
  KEY `Guestapp_tbl_studio_loginid_id_81b35d48` (`loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_studio`
--

INSERT INTO `guestapp_tbl_studio` (`studioid`, `studioname`, `address`, `email`, `phone`, `landmark`, `idproof`, `pincode`, `regdate`, `locationid_id`, `loginid_id`, `simage`) VALUES
(11, 'Insight wedding Company', '204-Bulding', 'insightwedding@gmail.com', 7036271890, 'Hospital jn', 'id-card-6368832_1280_TaeE4lY.png', 690518, '2025-03-11', 13, 26, '1_XKBLmgl.jpeg'),
(9, 'Frame Hunt', '245-street', 'jaidengillj@gmail.com', 6238831069, 'Gov.LP School', 'id-card-6368832_1280_myuRX4n.png', 686666, '2025-03-04', 23, 22, 'guesthome_t7IXP2i.jpg'),
(10, 'Moments', 'City Building', 'moments@gmail.com', 6829875690, 'Post office', 'id-card-6368832_1280_AVHc66I.png', 686670, '2025-03-04', 23, 25, 'home_vsiQUYJ.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `studioapp_tbl_package`
--

DROP TABLE IF EXISTS `studioapp_tbl_package`;
CREATE TABLE IF NOT EXISTS `studioapp_tbl_package` (
  `packageid` int(11) NOT NULL AUTO_INCREMENT,
  `packagename` varchar(25) NOT NULL,
  `description` varchar(400) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `category_id_id` int(11) NOT NULL,
  `studioid_id` int(11) NOT NULL,
  PRIMARY KEY (`packageid`),
  KEY `Studioapp_tbl_package_category_id_id_a7a0d947` (`category_id_id`),
  KEY `Studioapp_tbl_package_studioid_id_6b0fbeea` (`studioid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studioapp_tbl_package`
--

INSERT INTO `studioapp_tbl_package` (`packageid`, `packagename`, `description`, `amount`, `category_id_id`, `studioid_id`) VALUES
(7, 'Basic', 'A short & sweet session with 10 edited photos, 1 outfit change, and a cozy indoor or outdoor setting.', '10000.00', 6, 11),
(6, 'Basic Packagess', 'Our Basic Wedding Package offers elegant and simple photography coverage for your special day. It includes capturing the ceremony, candid moments, and family portraits. You\'ll receive a collection of high-resolution, beautifully edited images — perfect for couples seeking quality memories at an affordable price.\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n', '60000.00', 1, 10),
(4, 'Basic Package', 'A Studio Basic Package typically includes fundamental services and equipment for a recording or production session at an affordable rate.', '100000.00', 1, 9),
(8, 'Standard ', ' A well-rounded session with 20 edited photos, 2 outfit changes, themed props, and a personalized touch.', '20000.00', 6, 11),
(9, 'Premium', 'A complete experience with 35 edited photos, 3 outfit changes, customized themes, family portraits, and creative styling.', '25000.00', 6, 11);

-- --------------------------------------------------------

--
-- Table structure for table `studioapp_tbl_work`
--

DROP TABLE IF EXISTS `studioapp_tbl_work`;
CREATE TABLE IF NOT EXISTS `studioapp_tbl_work` (
  `workid` int(11) NOT NULL AUTO_INCREMENT,
  `workname` varchar(25) NOT NULL,
  `description` varchar(400) NOT NULL,
  `category_id_id` int(11) NOT NULL,
  `studioid_id` int(11) NOT NULL,
  `workimg` varchar(100) NOT NULL,
  PRIMARY KEY (`workid`),
  KEY `Studioapp_tbl_work_category_id_id_ba9a29db` (`category_id_id`),
  KEY `Studioapp_tbl_work_studioid_id_289baec6` (`studioid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studioapp_tbl_work`
--

INSERT INTO `studioapp_tbl_work` (`workid`, `workname`, `description`, `category_id_id`, `studioid_id`, `workimg`) VALUES
(11, 'Arun & Anu', 'Capturing the beautiful union of Arun and Anu, their wedding was a heartfelt celebration filled with love, joy, and cherished moments. From the vibrant ceremonies to the emotional vows, every frame tells a story of their journey together.', 1, 10, 'moonwedlock-20240926-0001.heic'),
(10, 'sandeep', 'groom to be', 1, 9, 'banner2_0tt64Qd.jpg'),
(12, 'Evan ', 'A photoshoot done for new born Evan.', 6, 11, 'an_vogue_wedding-20240926-0007.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `studioapp_tbl_workimage`
--

DROP TABLE IF EXISTS `studioapp_tbl_workimage`;
CREATE TABLE IF NOT EXISTS `studioapp_tbl_workimage` (
  `workimageid` int(11) NOT NULL AUTO_INCREMENT,
  `image1` varchar(100) NOT NULL,
  `work_id_id` int(11) NOT NULL,
  `image2` varchar(100) NOT NULL,
  `image3` varchar(100) NOT NULL,
  `image4` varchar(100) NOT NULL,
  `image5` varchar(100) NOT NULL,
  `image6` varchar(100) NOT NULL,
  PRIMARY KEY (`workimageid`),
  KEY `Studioapp_tbl_workimage_work_id_id_c5e914ac` (`work_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studioapp_tbl_workimage`
--

INSERT INTO `studioapp_tbl_workimage` (`workimageid`, `image1`, `work_id_id`, `image2`, `image3`, `image4`, `image5`, `image6`) VALUES
(4, 'tuesdaylights-20240926-0002.jpg', 11, 'tuesdaylights-20240926-0007.jpg', 'tuesdaylights-20240926-0005.jpg', 'tuesdaylights-20240926-0003.jpg', 'tuesdaylights-20240926-0009.jpg', 'tuesdaylights-20240926-0008.jpg'),
(5, 'an_vogue_wedding-20240926-0005.jpg', 12, 'an_vogue_wedding-20240926-0006.jpg', 'an_vogue_wedding-20240926-0007_bjfhyc6.jpg', 'an_vogue_wedding-20240926-0008.jpg', 'an_vogue_wedding-20240926-0009.jpg', 'an_vogue_wedding-20240926-0006_Q6hm7A0.jpg');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

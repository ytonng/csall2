CREATE DATABASE  IF NOT EXISTS `tourism information kiosk` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tourism information kiosk`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: tourism information kiosk
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attractions`
--

DROP TABLE IF EXISTS attractions;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE attractions (
  attractions_id int NOT NULL AUTO_INCREMENT,
  attractions_name varchar(100) NOT NULL,
  `description` text NOT NULL,
  attractions_price double NOT NULL,
  PRIMARY KEY (attractions_id),
  UNIQUE KEY attractions_id (attractions_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attractions`
--

LOCK TABLES attractions WRITE;
/*!40000 ALTER TABLE attractions DISABLE KEYS */;
/*!40000 ALTER TABLE attractions ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS booking;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE booking (
  order_id int NOT NULL AUTO_INCREMENT,
  order_date date NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (order_id),
  UNIQUE KEY order_id (order_id),
  KEY user_id (user_id),
  CONSTRAINT booking_ibfk_1 FOREIGN KEY (user_id) REFERENCES `user` (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES booking WRITE;
/*!40000 ALTER TABLE booking DISABLE KEYS */;
/*!40000 ALTER TABLE booking ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals`
--

DROP TABLE IF EXISTS deals;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE deals (
  deals_id int NOT NULL AUTO_INCREMENT,
  discount decimal(4,2) NOT NULL,
  promocode varchar(20) NOT NULL,
  attractions_id int NOT NULL,
  PRIMARY KEY (deals_id),
  UNIQUE KEY deals_id (deals_id),
  KEY attractions_id (attractions_id),
  CONSTRAINT deals_ibfk_1 FOREIGN KEY (attractions_id) REFERENCES attractions (attractions_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals`
--

LOCK TABLES deals WRITE;
/*!40000 ALTER TABLE deals DISABLE KEYS */;
/*!40000 ALTER TABLE deals ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favourite`
--

DROP TABLE IF EXISTS favourite;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE favourite (
  fav_id int NOT NULL AUTO_INCREMENT,
  user_id int NOT NULL,
  attractions_id int NOT NULL,
  PRIMARY KEY (fav_id),
  UNIQUE KEY fav_id (fav_id),
  KEY user_id (user_id),
  KEY attractions_id (attractions_id),
  CONSTRAINT favourite_ibfk_1 FOREIGN KEY (user_id) REFERENCES `user` (user_id),
  CONSTRAINT favourite_ibfk_2 FOREIGN KEY (attractions_id) REFERENCES attractions (attractions_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favourite`
--

LOCK TABLES favourite WRITE;
/*!40000 ALTER TABLE favourite DISABLE KEYS */;
/*!40000 ALTER TABLE favourite ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_details`
--

DROP TABLE IF EXISTS order_details;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE order_details (
  order_details_id int NOT NULL AUTO_INCREMENT,
  quantities int NOT NULL,
  order_id int NOT NULL,
  attractions_id int NOT NULL,
  PRIMARY KEY (order_details_id),
  UNIQUE KEY order_details_id (order_details_id),
  KEY order_id (order_id),
  KEY attractions_id (attractions_id),
  CONSTRAINT order_details_ibfk_1 FOREIGN KEY (order_id) REFERENCES booking (order_id),
  CONSTRAINT order_details_ibfk_2 FOREIGN KEY (attractions_id) REFERENCES attractions (attractions_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_details`
--

LOCK TABLES order_details WRITE;
/*!40000 ALTER TABLE order_details DISABLE KEYS */;
/*!40000 ALTER TABLE order_details ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS payment;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE payment (
  payment_id int NOT NULL AUTO_INCREMENT,
  order_id int NOT NULL,
  payment_method varchar(50) NOT NULL,
  payment_amount double NOT NULL,
  PRIMARY KEY (payment_id),
  UNIQUE KEY payment_id (payment_id),
  KEY order_id (order_id),
  CONSTRAINT payment_ibfk_1 FOREIGN KEY (order_id) REFERENCES booking (order_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES payment WRITE;
/*!40000 ALTER TABLE payment DISABLE KEYS */;
/*!40000 ALTER TABLE payment ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trip`
--

DROP TABLE IF EXISTS trip;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE trip (
  trip_id int NOT NULL AUTO_INCREMENT,
  attractions_id int NOT NULL,
  notes text,
  `date` date NOT NULL,
  expenses decimal(9,2) NOT NULL,
  total_expenses decimal(9,2) NOT NULL,
  PRIMARY KEY (trip_id),
  UNIQUE KEY trip_id (trip_id),
  KEY attractions_id (attractions_id),
  CONSTRAINT trip_ibfk_1 FOREIGN KEY (attractions_id) REFERENCES attractions (attractions_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trip`
--

LOCK TABLES trip WRITE;
/*!40000 ALTER TABLE trip DISABLE KEYS */;
/*!40000 ALTER TABLE trip ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS user;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  user_id int NOT NULL AUTO_INCREMENT,
  user_name varchar(50) NOT NULL,
  user_role varchar(50) NOT NULL,
  gender varchar(10) NOT NULL,
  passport_num varchar(20) NOT NULL,
  email varchar(150) NOT NULL,
  contact_number varchar(20) NOT NULL,
  `Password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (user_id),
  UNIQUE KEY user_id (user_id),
  UNIQUE KEY user_name (user_name),
  UNIQUE KEY passport_num (passport_num),
  UNIQUE KEY email (email)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES user WRITE;
/*!40000 ALTER TABLE user DISABLE KEYS */;
INSERT INTO user VALUES (2,'Steven','User','Male','A00000000','steven@gmail.com','012-3456789','008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601');
/*!40000 ALTER TABLE user ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-09 20:36:39

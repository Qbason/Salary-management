-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 78.157.187.16    Database: salarymanagement
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `contract`
--

DROP TABLE IF EXISTS `contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contract` (
  `id_contract` int unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(40) NOT NULL,
  `startingdate` date NOT NULL,
  `expirationdate` date NOT NULL,
  `companyname` varchar(100) NOT NULL,
  `dayjob` varchar(8) DEFAULT NULL,
  `hourlyrate` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id_contract`),
  CONSTRAINT `contract_ibfk_1` FOREIGN KEY (`id_contract`) REFERENCES `employee` (`id_employee`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract`
--

LOCK TABLES `contract` WRITE;
/*!40000 ALTER TABLE `contract` DISABLE KEYS */;
INSERT INTO `contract` VALUES (1,'Umowa zlecenie','2021-07-17','2021-07-17','ALARMANDIA','1/2',19.30),(20,'Umowa o prace na czas nieokreślony','2012-12-20','2012-12-20','elowina','1/2',15.20),(21,'Umowa o prace na czas nieokreślony','2012-12-20','2012-12-20','elowina','1/2',15.20),(22,'Umowa o prace na czas nieokreślony','2012-12-20','2012-12-20','elowkoa','1/4',15.20),(23,'Umowa o prace na czas nieokreślony','2012-12-20','2012-12-20','elowina','1/4',15.20),(24,'Umowa o prace na czas nieokreślony','2012-12-20','2012-12-20','elowina','1/4',15.20),(25,'Umowa o prace na czas nieokreślony','2012-12-20','2012-12-20','Elowina','1/4',15.20);
/*!40000 ALTER TABLE `contract` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-25 16:04:31

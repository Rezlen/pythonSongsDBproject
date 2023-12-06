-- MySQL dump 10.16  Distrib 10.1.48-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.48-MariaDB-0+deb9u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `downloads`
--

DROP TABLE IF EXISTS `downloads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `downloads` (
  `DownlID` varchar(0) DEFAULT NULL,
  `SongID` varchar(0) DEFAULT NULL,
  `MemberID` varchar(0) DEFAULT NULL,
  `Date` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `downloads`
--

LOCK TABLES `downloads` WRITE;
/*!40000 ALTER TABLE `downloads` DISABLE KEYS */;
/*!40000 ALTER TABLE `downloads` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `members` (
  `MemberID` varchar(0) DEFAULT NULL,
  `Firstname` varchar(0) DEFAULT NULL,
  `Lastname` varchar(0) DEFAULT NULL,
  `Email` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `songs` (
  `SongID` smallint(6) DEFAULT NULL,
  `Title` varchar(37) DEFAULT NULL,
  `Artist` varchar(14) DEFAULT NULL,
  `Genre` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES (1,'Dance','Ams','Coding'),(2,'1984','John Smith','comedy'),(3,'The Catcher in the Rye','David Thompson','adventure'),(4,'1984','Emily Johnson','romance'),(5,'1984','David Thompson','drama'),(6,'The Lord of the Rings','Emily Johnson','drama'),(7,'The Hunger Games','Michael Davis','adventure'),(8,'The Great Gatsby','David Thompson','action'),(9,'The Catcher in the Rye','David Thompson','sci-fi'),(10,'The Hobbit','Michael Davis','mystery'),(11,'1984','Michael Davis','comedy'),(12,'To Kill a Mockingbird','Michael Davis','adventure'),(13,'The Lord of the Rings','John Smith','sci-fi'),(14,'The Great Gatsby','Emma Wilson','action'),(15,'To Kill a Mockingbird','Michael Davis','fantasy'),(16,'Harry Potter and the Sorcerer\'s Stone','Emily Johnson','thriller'),(17,'1984','Emma Wilson','mystery'),(18,'The Great Gatsby','John Smith','drama'),(19,'The Lord of the Rings','Emma Wilson','mystery'),(20,'Harry Potter and the Sorcerer\'s Stone','Emily Johnson','adventure'),(21,'The Catcher in the Rye','Michael Davis','adventure'),(22,'The Great Gatsby','John Smith','fantasy'),(23,'1984','Michael Davis','mystery'),(24,'The Lord of the Rings','Emma Wilson','romance'),(25,'1984','Emily Johnson','horror'),(26,'The Lord of the Rings','John Smith','fantasy'),(27,'The Great Gatsby','Michael Davis','mystery'),(28,'Harry Potter and the Sorcerer\'s Stone','Emily Johnson','horror'),(29,'The Catcher in the Rye','Emily Johnson','mystery'),(30,'The Catcher in the Rye','John Smith','horror'),(31,'Pride and Prejudice','Emily Johnson','romance'),(32,'1984','John Smith','action'),(33,'The Da Vinci Code','Michael Davis','thriller'),(34,'Pride and Prejudice','John Smith','drama'),(35,'Harry Potter and the Sorcerer\'s Stone','Emma Wilson','horror'),(36,'The Da Vinci Code','Emma Wilson','fantasy'),(37,'The Hobbit','David Thompson','romance'),(38,'Harry Potter and the Sorcerer\'s Stone','John Smith','sci-fi'),(39,'To Kill a Mockingbird','Michael Davis','mystery'),(40,'The Hobbit','Emma Wilson','thriller'),(41,'The Hunger Games','Michael Davis','fantasy'),(42,'Harry Potter and the Sorcerer\'s Stone','Emma Wilson','action'),(43,'The Great Gatsby','Michael Davis','adventure'),(44,'The Hunger Games','David Thompson','mystery'),(45,'The Da Vinci Code','Emily Johnson','fantasy'),(46,'The Lord of the Rings','Emma Wilson','drama'),(47,'The Da Vinci Code','Emma Wilson','romance'),(48,'The Great Gatsby','Emily Johnson','mystery'),(49,'1984','David Thompson','drama'),(50,'The Da Vinci Code','Emily Johnson','mystery'),(51,'The Lord of the Rings','Emma Wilson','adventure'),(52,'The Lord of the Rings','John Smith','horror'),(53,'To Kill a Mockingbird','Emily Johnson','fantasy'),(54,'The Hobbit','Emily Johnson','drama'),(55,'Harry Potter and the Sorcerer\'s Stone','Emma Wilson','comedy'),(56,'The Great Gatsby','Emma Wilson','action'),(57,'The Great Gatsby','John Smith','comedy'),(58,'The Catcher in the Rye','David Thompson','action'),(59,'The Lord of the Rings','Emily Johnson','horror'),(60,'To Kill a Mockingbird','David Thompson','drama'),(61,'The Great Gatsby','Emma Wilson','romance'),(62,'Pride and Prejudice','John Smith','action'),(63,'The Catcher in the Rye','Emma Wilson','sci-fi'),(64,'The Great Gatsby','Emily Johnson','horror'),(65,'The Lord of the Rings','Emily Johnson','mystery'),(66,'Pride and Prejudice','David Thompson','fantasy'),(67,'1984','David Thompson','adventure'),(68,'Harry Potter and the Sorcerer\'s Stone','John Smith','sci-fi'),(69,'The Catcher in the Rye','David Thompson','comedy'),(70,'The Hunger Games','David Thompson','thriller'),(71,'1984','Emma Wilson','adventure'),(72,'Harry Potter and the Sorcerer\'s Stone','Emma Wilson','action'),(73,'The Hunger Games','Michael Davis','mystery'),(74,'To Kill a Mockingbird','John Smith','thriller'),(75,'Pride and Prejudice','Emma Wilson','action'),(76,'Pride and Prejudice','Michael Davis','romance'),(77,'1984','Emma Wilson','action'),(78,'1984','John Smith','adventure'),(79,'Harry Potter and the Sorcerer\'s Stone','Emma Wilson','horror'),(80,'The Da Vinci Code','Michael Davis','adventure'),(81,'The Hobbit','Michael Davis','romance'),(82,'The Da Vinci Code','David Thompson','sci-fi'),(83,'The Hunger Games','Emma Wilson','fantasy'),(84,'To Kill a Mockingbird','Michael Davis','adventure'),(85,'Harry Potter and the Sorcerer\'s Stone','Emma Wilson','sci-fi'),(86,'The Catcher in the Rye','John Smith','horror'),(87,'The Great Gatsby','Michael Davis','romance'),(88,'Pride and Prejudice','Emma Wilson','comedy'),(89,'The Catcher in the Rye','Emily Johnson','adventure'),(90,'The Da Vinci Code','Michael Davis','romance'),(91,'The Hunger Games','Emily Johnson','mystery'),(92,'The Da Vinci Code','Emma Wilson','adventure'),(93,'1984','John Smith','mystery'),(94,'The Hobbit','John Smith','comedy'),(95,'The Catcher in the Rye','Michael Davis','thriller'),(96,'Pride and Prejudice','David Thompson','romance'),(97,'The Lord of the Rings','Emily Johnson','horror'),(98,'Pride and Prejudice','David Thompson','fantasy'),(99,'The Catcher in the Rye','David Thompson','fantasy'),(100,'The Hobbit','Emily Johnson','adventure');
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sqlite_sequence`
--

DROP TABLE IF EXISTS `sqlite_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sqlite_sequence` (
  `name` varchar(5) DEFAULT NULL,
  `seq` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sqlite_sequence`
--

LOCK TABLES `sqlite_sequence` WRITE;
/*!40000 ALTER TABLE `sqlite_sequence` DISABLE KEYS */;
INSERT INTO `sqlite_sequence` VALUES ('songs',3002);
/*!40000 ALTER TABLE `sqlite_sequence` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-11 11:56:59

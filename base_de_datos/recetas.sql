CREATE DATABASE  IF NOT EXISTS `esquema_recetas` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `esquema_recetas`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: esquema_recetas
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `recetas`
--

DROP TABLE IF EXISTS `recetas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recetas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(200) NOT NULL,
  `instructions` text NOT NULL,
  `date` varchar(80) NOT NULL,
  `under` tinyint NOT NULL,
  `usuario_id` int NOT NULL,
  `created_at` varchar(45) NOT NULL,
  `updated_at` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_recetas_usuarios_idx` (`usuario_id`),
  CONSTRAINT `fk_recetas_usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetas`
--

LOCK TABLES `recetas` WRITE;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` VALUES (1,'Hamburguesas','Hamburguesas caseras','- Cocinar la carne\r\n- Freír papas','2021-01-15',1,1,'2022-03-15 18:30:42','2022-03-15 18:30:42'),(2,'Tallarines','tallarines rojos','-Cocer la pasta\r\n-Preparar la salsa de tomate','2018-04-18',0,2,'2022-03-15 18:33:16','2022-03-15 18:33:16'),(3,'Hotcakes','hotcakes con fruta','-Mezclar leche, huevos y harina\r\n-Picar fruta','2017-08-02',1,3,'2022-03-15 18:36:30','2022-03-15 18:36:30');
/*!40000 ALTER TABLE `recetas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(200) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Patricia ','Betancor','patyb@gmail.com','$2b$12$awT7bxIhBxB.9lY3Q5T0bO.Qm0zBUSBrLBrTa7rgKEs6AMCzBxfuK','2022-03-15 09:30:14','2022-03-15 09:30:14'),(2,'Juan','Sierra','juansierra@gmail.com','$2b$12$5mfBjTcEUpVLAppMThEFg.UzMcNTrhqnkGFXQDIx5o8ueU7eat8qq','2022-03-15 09:33:30','2022-03-15 09:33:30'),(3,'Susana','Morales','sumorales@gmail.com','$2b$12$CflUhHipexQvSrEq.3HtK.XMF.rJe1N0fKLfyiQ2OXFCj5nqvUQPe','2022-03-15 09:35:42','2022-03-15 09:35:42');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-15 18:37:46

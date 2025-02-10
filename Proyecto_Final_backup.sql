-- MySQL dump 10.13  Distrib 8.0.41, for Linux (x86_64)
--
-- Host: localhost    Database: Proyecto_Final
-- ------------------------------------------------------
-- Server version	8.0.41-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CitaMedica`
--

DROP TABLE IF EXISTS `CitaMedica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CitaMedica` (
  `codigo_cita` int NOT NULL AUTO_INCREMENT,
  `estado` enum('EN_ESPERA','AGENDADA','FINALIZADA','CANCELADA') NOT NULL DEFAULT 'EN_ESPERA',
  `motivo` text,
  `observaciones` text,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `iden_paciente` int DEFAULT NULL,
  `iden_odontologo` int DEFAULT NULL,
  `cod_historial` int DEFAULT NULL,
  `cod_diagnostico` int DEFAULT NULL,
  PRIMARY KEY (`codigo_cita`),
  UNIQUE KEY `fecha` (`fecha`,`hora`),
  KEY `iden_paciente` (`iden_paciente`),
  KEY `iden_odontologo` (`iden_odontologo`),
  CONSTRAINT `CitaMedica_ibfk_1` FOREIGN KEY (`iden_paciente`) REFERENCES `Persona` (`identificacion`),
  CONSTRAINT `CitaMedica_ibfk_2` FOREIGN KEY (`iden_odontologo`) REFERENCES `Odontologo` (`identificacion_odon`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CitaMedica`
--

LOCK TABLES `CitaMedica` WRITE;
/*!40000 ALTER TABLE `CitaMedica` DISABLE KEYS */;
INSERT INTO `CitaMedica` VALUES (3,'EN_ESPERA','ninguno','adkjfald','2025-02-21','10:30:00',6,7,NULL,NULL),(4,'EN_ESPERA','lkjaflds','dsanfdsadsa','2025-02-21','21:11:00',5,7,NULL,NULL),(5,'EN_ESPERA','Muelas','Caries','2025-02-07','19:15:00',6,7,NULL,NULL);
/*!40000 ALTER TABLE `CitaMedica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cuenta`
--

DROP TABLE IF EXISTS `Cuenta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cuenta` (
  `identificacion` int NOT NULL,
  `usuario` varchar(50) DEFAULT NULL,
  `contrasena` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`identificacion`),
  UNIQUE KEY `usuario` (`usuario`),
  CONSTRAINT `Cuenta_ibfk_1` FOREIGN KEY (`identificacion`) REFERENCES `Persona` (`identificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cuenta`
--

LOCK TABLES `Cuenta` WRITE;
/*!40000 ALTER TABLE `Cuenta` DISABLE KEYS */;
INSERT INTO `Cuenta` VALUES (5,'alexis','hola123'),(6,'alexis2','hola123'),(7,'alexis3','hola123'),(17,'emilio','emilioj89');
/*!40000 ALTER TABLE `Cuenta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Diagnostico`
--

DROP TABLE IF EXISTS `Diagnostico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Diagnostico` (
  `codigo_diagnostico` int NOT NULL AUTO_INCREMENT,
  `descripcion` text,
  `examen` text,
  `cod_cita` int DEFAULT NULL,
  PRIMARY KEY (`codigo_diagnostico`),
  KEY `cod_cita` (`cod_cita`),
  CONSTRAINT `Diagnostico_ibfk_1` FOREIGN KEY (`cod_cita`) REFERENCES `CitaMedica` (`codigo_cita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Diagnostico`
--

LOCK TABLES `Diagnostico` WRITE;
/*!40000 ALTER TABLE `Diagnostico` DISABLE KEYS */;
/*!40000 ALTER TABLE `Diagnostico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HistorialMedico`
--

DROP TABLE IF EXISTS `HistorialMedico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `HistorialMedico` (
  `codigo_historial` int NOT NULL AUTO_INCREMENT,
  `patologias_pasadas` text,
  `alergias` text,
  `tratamiento` text,
  PRIMARY KEY (`codigo_historial`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HistorialMedico`
--

LOCK TABLES `HistorialMedico` WRITE;
/*!40000 ALTER TABLE `HistorialMedico` DISABLE KEYS */;
INSERT INTO `HistorialMedico` VALUES (1,'PUTOS','lkjdsalkjfdslkja','lkjdsafljalkjdslkjfdsads');
/*!40000 ALTER TABLE `HistorialMedico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Odontologo`
--

DROP TABLE IF EXISTS `Odontologo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Odontologo` (
  `identificacion_odon` int NOT NULL,
  `codigo_licencia` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`identificacion_odon`),
  UNIQUE KEY `codigo_licencia` (`codigo_licencia`),
  CONSTRAINT `Odontologo_ibfk_1` FOREIGN KEY (`identificacion_odon`) REFERENCES `Persona` (`identificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Odontologo`
--

LOCK TABLES `Odontologo` WRITE;
/*!40000 ALTER TABLE `Odontologo` DISABLE KEYS */;
INSERT INTO `Odontologo` VALUES (7,'ACK2025');
/*!40000 ALTER TABLE `Odontologo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Persona`
--

DROP TABLE IF EXISTS `Persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Persona` (
  `identificacion` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `celular` varchar(20) DEFAULT NULL,
  `cod_historial` int DEFAULT NULL,
  `id_rol` int DEFAULT NULL,
  PRIMARY KEY (`identificacion`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `celular` (`celular`),
  KEY `cod_historial` (`cod_historial`),
  KEY `id_rol` (`id_rol`),
  CONSTRAINT `Persona_ibfk_1` FOREIGN KEY (`cod_historial`) REFERENCES `HistorialMedico` (`codigo_historial`),
  CONSTRAINT `Persona_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `Rol` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Persona`
--

LOCK TABLES `Persona` WRITE;
/*!40000 ALTER TABLE `Persona` DISABLE KEYS */;
INSERT INTO `Persona` VALUES (5,'Jonnatan Mauricio','Roman Avila','2005-04-26','prueba@gmail.com','09932413',NULL,3),(6,'Alexis Vinicio','Roman Avila','2005-04-26','prueba2@gmail.com','099324134',NULL,1),(7,'Alexis Vinicio','Roman Avila','2005-04-26','prueba3@gmail.com','0993241345',NULL,2),(17,'Emilio Ramiro','Jaramillo Chamba','2006-04-27','emilio@gmail.com','09932888888',NULL,2);
/*!40000 ALTER TABLE `Persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Receta`
--

DROP TABLE IF EXISTS `Receta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Receta` (
  `codigo_receta` int NOT NULL AUTO_INCREMENT,
  `dosis` text,
  `medicamento` text,
  `cod_diagnostico` int DEFAULT NULL,
  PRIMARY KEY (`codigo_receta`),
  KEY `cod_diagnostico` (`cod_diagnostico`),
  CONSTRAINT `Receta_ibfk_1` FOREIGN KEY (`cod_diagnostico`) REFERENCES `Diagnostico` (`codigo_diagnostico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Receta`
--

LOCK TABLES `Receta` WRITE;
/*!40000 ALTER TABLE `Receta` DISABLE KEYS */;
/*!40000 ALTER TABLE `Receta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rol`
--

DROP TABLE IF EXISTS `Rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rol` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `descripcion` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rol`
--

LOCK TABLES `Rol` WRITE;
/*!40000 ALTER TABLE `Rol` DISABLE KEYS */;
INSERT INTO `Rol` VALUES (1,'Admin','Administrador del sistema'),(2,'Odontologo','Odontologo propietario del sistema'),(3,'Paciente','Rol base de los pacientes');
/*!40000 ALTER TABLE `Rol` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-10 12:35:51

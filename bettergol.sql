CREATE DATABASE  IF NOT EXISTS `bettergol`;
USE `bettergol`;

--
-- Table structure for table `codigos`
--

DROP TABLE IF EXISTS `codigos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `codigos` (
  `id_codigo` varchar(45) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `bool1` tinyint(1) DEFAULT NULL,
  `bool2` tinyint(1) DEFAULT NULL,
  `int1` int DEFAULT NULL,
  `int2` int DEFAULT NULL,
  `string1` varchar(255) DEFAULT NULL,
  `string2` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
;

--
-- Dumping data for table `codigos`
--

LOCK TABLES `codigos` WRITE;
/*!40000 ALTER TABLE `codigos` DISABLE KEYS */;
/*!40000 ALTER TABLE `codigos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfiles`
--

DROP TABLE IF EXISTS `perfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perfiles` (
  `id_perfil` int NOT NULL AUTO_INCREMENT,
  `perfil` varchar(45) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `bool1` tinyint(1) DEFAULT NULL,
  `bool2` tinyint DEFAULT NULL,
  `int1` int DEFAULT NULL,
  `int2` int DEFAULT NULL,
  `string1` varchar(255) DEFAULT NULL,
  `string2` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_perfil`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfiles`
--

LOCK TABLES `perfiles` WRITE;
/*!40000 ALTER TABLE `perfiles` DISABLE KEYS */;
INSERT INTO `perfiles` VALUES (1,'Administrador','2022-10-26 21:46:51','2022-10-26 21:46:51',NULL,NULL,NULL,NULL,NULL,NULL),(2,'Usuario','2022-10-26 21:46:51','2022-10-26 21:46:51',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `perfiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `dni` varchar(255) NOT NULL,
  `celular` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `terminos` varchar(45) NOT NULL,
  `recuperarpsw` tinyint DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `perfiles_id_perfil` int NOT NULL,
  `codigo` varchar(255) DEFAULT NULL,
  `bool1` tinyint(1) DEFAULT NULL,
  `bool2` tinyint(1) DEFAULT NULL,
  `bool3` tinyint(1) DEFAULT NULL,
  `int1` int DEFAULT NULL,
  `int2` int DEFAULT NULL,
  `int3` int DEFAULT NULL,
  `string1` varchar(255) DEFAULT NULL,
  `string2` varchar(255) DEFAULT NULL,
  `string3` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  KEY `fk_usuarios_perfiles1_idx` (`perfiles_id_perfil`),
  CONSTRAINT `fk_usuarios_perfiles1` FOREIGN KEY (`perfiles_id_perfil`) REFERENCES `perfiles` (`id_perfil`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Admin','Admin','0','0992720315','bettergol593@gmail.com','$2b$12$xEWuW53XuqyMbDWxWFaOO.WnDFF983suwFMKboRX.B8EPlnE7IWby','aceptado',0,'2022-10-26 21:47:32','2022-10-26 21:47:32',1,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;


--
-- Table structure for table `pronosticos`
--

DROP TABLE IF EXISTS `pronosticos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pronosticos` (
  `id_pronostico` int NOT NULL AUTO_INCREMENT,
  `usuarios_id_usuario` int NOT NULL,
  `A1` varchar(255) DEFAULT NULL,
  `B2` varchar(255) DEFAULT NULL,
  `C1` varchar(255) DEFAULT NULL,
  `D2` varchar(255) DEFAULT NULL,
  `E1` varchar(255) DEFAULT NULL,
  `F2` varchar(255) DEFAULT NULL,
  `G1` varchar(255) DEFAULT NULL,
  `H2` varchar(255) DEFAULT NULL,
  `A2` varchar(255) DEFAULT NULL,
  `B1` varchar(255) DEFAULT NULL,
  `C2` varchar(255) DEFAULT NULL,
  `D1` varchar(255) DEFAULT NULL,
  `E2` varchar(255) DEFAULT NULL,
  `F1` varchar(255) DEFAULT NULL,
  `G2` varchar(255) DEFAULT NULL,
  `H1` varchar(255) DEFAULT NULL,
  `A1B2` varchar(255) DEFAULT NULL,
  `C1D2` varchar(255) DEFAULT NULL,
  `E1F2` varchar(255) DEFAULT NULL,
  `G1H2` varchar(255) DEFAULT NULL,
  `A2B1` varchar(255) DEFAULT NULL,
  `C2D1` varchar(255) DEFAULT NULL,
  `E2F1` varchar(255) DEFAULT NULL,
  `G2H1` varchar(255) DEFAULT NULL,
  `O1O2` varchar(255) DEFAULT NULL,
  `O3O4` varchar(255) DEFAULT NULL,
  `O5O6` varchar(255) DEFAULT NULL,
  `O7O8` varchar(255) DEFAULT NULL,
  `SEMI1` varchar(255) DEFAULT NULL,
  `SEMI2` varchar(255) DEFAULT NULL,
  `PS1PS2` varchar(255) DEFAULT NULL,
  `final` varchar(255) DEFAULT NULL,
  `segundo` varchar(255) DEFAULT NULL,
  `cuarto` varchar(255) DEFAULT NULL,
  `puntos` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `bool1` tinyint(1) DEFAULT NULL,
  `bool2` tinyint(1) DEFAULT NULL,
  `int1` int DEFAULT NULL,
  `int2` int DEFAULT NULL,
  `string1` varchar(255) DEFAULT NULL,
  `string2` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_pronostico`),
  KEY `fk_pronosticos_usuarios1_idx` (`usuarios_id_usuario`),
  CONSTRAINT `fk_pronosticos_usuarios1` FOREIGN KEY (`usuarios_id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pronosticos`
--

LOCK TABLES `pronosticos` WRITE;
/*!40000 ALTER TABLE `pronosticos` DISABLE KEYS */;
INSERT INTO `pronosticos` VALUES (1,1,'A1','B2','C1','D2','E1','F2','G1','H2','A2','B1','C2','D1','E2','F1','G2','H1','A1B2','C1D2','E1F2','G1H2','A2B1','C2D1','E2F1','G2H1','O1O2','O3O4','O5O6','O7O8','SEMI1','SEMI2','PS1PS2','final','segundo','cuarto',NULL,'2022-10-26 21:48:11','2022-10-26 21:48:11',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `pronosticos` ENABLE KEYS */;
UNLOCK TABLES;



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-26 21:48:51
